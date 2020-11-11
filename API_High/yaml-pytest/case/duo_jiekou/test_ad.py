import sys

import allure
import pytest

sys.path.append("..")
from util.util import Util
from decimal import Decimal
from const import status_code, bs_code
from base_class import base_case
from action import otc


class TestRecharge(base_case.BaseCase):

    @allure.story("出售广告")
    @allure.title("出售广告--快速匹配--交易完成--交易流程")
    # pay_type 1 支付宝  2 微信 3 银行卡
    @pytest.mark.parametrize(
        "ad_type,coin_name,pay_type,pay_info,amount,min_limit,max_limit,merchant_order_currency,_except", [(
                1, "USDT", 3,
                {
                    "bank_code": "256",
                    "otc_ader_name": "ds",
                    "bank_branch": "cs",
                    "bank_name": "fc",
                    "bankstr": "(****6)"},
                "1000", "1",
                "100", "50",
                status_code.EXCEPT_SUCCESS)])
    def test_buy_ad(self, first_ad_action, merchant_action, admin_action, ad_type, coin_name, pay_type, pay_info,
                    amount, min_limit, max_limit, merchant_order_currency, _except):

        old_merchant_info = merchant_action.get_finance(coin_name)
        # 商户发起广告
        identify_info = first_ad_action.get_identify_info()
        self.catch(identify_info['data']['LV1_result']['type'] == bs_code.IDENTIFY_SUCCESS, _except, status_code.IDENTIFY_LV1_OFF)
        ad_list_info = first_ad_action.get_ad_list()

        # 如果有买入广告 全部撤销
        self.catch(ad_list_info['status_code'] == 200, _except, status_code.NETWORK_EX)
        for item in ad_list_info['data']["list"]:
            if item['otc_ad_type'] == ad_type and (
                    item['otc_ad_status'] == bs_code.AD_ON or item['otc_ad_status'] == bs_code.AD_OFF or item['otc_ad_status'] == 0):
                rsp = first_ad_action.update_ad_status(item['otc_ad_id'], bs_code.AD_CANCEL)
                self.catch(rsp['status_code'] == 200, _except, status_code.NETWORK_EX)
        # pay_type 1 支付宝  2 微信 3 银行卡
        # 发起一个出售广告 检查自己的支付方式
        pay_list = first_ad_action.get_pay_info_list()
        self.catch(pay_list['status_code'] == 200, _except, status_code.NETWORK_EX)
        pay_status = False
        for item in pay_list['data']['list']:
            if item['otc_ad_account_type'] == pay_type and item['otc_account_status'] == bs_code.PAY_ON:
                pay_status = True
                break
        if not pay_status:
            rsp = first_ad_action.add_pay_type(pay_type, pay_info, bs_code.PAY_ON)
            self.catch(rsp['status_code'] == 200, _except, status_code.NETWORK_EX)
        is_blank, is_alipay, is_wechatpay = 0, 0, 0

        if pay_type == 1:
            is_alipay = 2
        elif pay_type == 2:
            is_wechatpay = 2
        else:
            is_blank = 2

        old_finance_info = first_ad_action.get_finance()

        ad_rsp = first_ad_action.create_ad(coin_name, ad_type, amount, min_limit, max_limit, is_bank=is_blank,
                                           is_alipay=is_alipay, is_wechatpay=is_wechatpay)
        self.catch(ad_rsp['status_code'] == 200, _except, status_code.CREATE_AD_FAILED)

        # 商户检查资产变化
        added_finance = first_ad_action.get_finance()
        self.catch(Util.get_list_ele(added_finance['data']['list'], 'coin_name', coin_name)['amount'] ==
                   Util.get_list_ele(old_finance_info['data']['list'], 'coin_name', coin_name)['amount'], _except,
                   status_code.ASSETS_EX)
        self.catch(Decimal(
            Util.get_list_ele(added_finance['data']['list'], 'coin_name', coin_name)['available_amount']) - Decimal(
            Util.get_list_ele(old_finance_info['data']['list'], 'coin_name', coin_name)[
                'available_amount']) == -Decimal(amount), _except, status_code.ASSETS_EX)

        # 企业发起订单
        order_info = merchant_action.create_order(pay_type, 1, coin_name, merchant_order_currency)
        self.catch(order_info['status_code'] == 200, _except, status_code.MERCHANT_CREATE_OR_FAILED)
        # 商户找到订单
        ##存在订单延时状态显示机制--策略组--自动派单设置 目前跳过
        status = False
        for i in range(15):
            ad_list = first_ad_action.get_order_list()
            self.catch(ad_list['status_code'] == 200, _except, status_code.NETWORK_EX)
            for data in ad_list['data']:
                if data['OrderNumber'] == order_info['data']['order_number']:
                    status = True
                    break
            if status:
                break
        # 找到订单
        self.catch(status, _except, status_code.ORDER_NOT_FOUND)
        order_info = Util.get_list_ele(first_ad_action.get_order_list()['data'], "OrderNumber",
                                       order_info['data']['order_number'])
        self.catch(order_info['order_status'] == bs_code.ORDER_WAIT_MATE, _except, status_code.ORDER_STATUS_EX)
        # 商户抢单
        rob_rsp = first_ad_action.ader_rob_order(order_info['OrderNumber'])
        self.catch(rob_rsp['status_code'] == 200, _except, status_code.ORDER_ROB_EX)
        # 企业平台确认打款
        pay_info = merchant_action.get_ad_pay_info(rob_rsp['data']['otc_transac_id'])
        self.catch(pay_info['status_code'] == 200, _except, status_code.NETWORK_EX)
        rsp = merchant_action.confirm_order(rob_rsp['data']['otc_transac_id'],
                                            pay_info['data']['list'][0]['otc_ad_account_id'], order_info['OrderNumber'])
        self.catch(rsp['status_code'] == 200, _except, status_code.MERCHANT_CONFIRM_ORDER_EX)
        # 商户确认放币
        allow_rsp = first_ad_action.allow_order(rob_rsp['data']['otc_transac_id'])
        self.catch(allow_rsp['status_code'] == 200, _except, status_code.ORDER_FINISH_EX)
        order_info = Util.get_list_ele(first_ad_action.get_order_list()['data'], "OrderNumber",
                                       order_info['OrderNumber'])
        self.catch(order_info['order_status'] == bs_code.ORDER_SUCCESS, _except, status_code.ORDER_STATUS_EX)
        # 以上过程包含订单状态变化检查

        # 开启资产检验

        # 商户个人资产检查
        tran_list = first_ad_action.get_transac_list()
        tran_info = Util.get_list_ele(tran_list['data']['list'], "otc_transac_id", rob_rsp['data']['otc_transac_id'])
        finish_finance = first_ad_action.get_finance()
        finish_coin_finance = Util.get_list_ele(finish_finance['data']['list'], "coin_name", coin_name)
        added_coin_finance = Util.get_list_ele(added_finance['data']['list'], "coin_name", coin_name)
        self.catch(Decimal(finish_coin_finance['amount']) - Decimal(added_coin_finance['amount']) == Decimal(
            Util.sub_number(-(Decimal(merchant_order_currency) / Decimal(tran_info['unin_price'])), 10)), _except,
                   status_code.FINANCE_EX)
        self.catch(finish_coin_finance['available_amount'] == added_coin_finance['available_amount'], _except,
                   status_code.FINANCE_EX)
        # 商户订单记录检查 上面流程已覆盖

        # 企业平台资产检查
        ratio = admin_action.admin_get_merchant_info(merchant_action.user_name)
        self.catch(ratio['status_code'] == 200 and len(ratio['data']['list']) > 0, _except,
                   status_code.ADMIN_GET_MERCHANT_INFO_FAILED)

        merchant_add_finance = Decimal(
            Util.sub_number((Decimal(merchant_order_currency) / Decimal(tran_info['unin_price'])), 10)) * (
                                       1 - Decimal(ratio['data']['list'][0]['platfrom_ratio']) * Decimal(0.01))

        new_merchant_finance = merchant_action.get_finance(coin_name)
        self.catch(new_merchant_finance, _except, status_code.NETWORK_EX)

        self.catch(Decimal(new_merchant_finance['amount']) - Decimal(old_merchant_info['amount']) == Decimal(
            Util.sub_number(merchant_add_finance, 10)), _except, status_code.MERCHANT_FINANCE_EX)
        self.catch(Decimal(new_merchant_finance['available_amount']) - Decimal(
            old_merchant_info['available_amount']) == Decimal(Util.sub_number(merchant_add_finance, 10)), _except,
                   status_code.MERCHANT_FINANCE_EX)

        # 总后台记录检查
        list = admin_action.admin_get_transac_list(order_info["OrderNumber"])
        self.catch(list['status_code'] == 200 and len(list['data']['list']) > 0, _except, status_code.NETWORK_EX)

        # 广告剩余数量 广告总数量检查
        new_ad_info = first_ad_action.get_ad_list()
        self.catch(new_ad_info['status_code'] == 200, _except, status_code.NETWORK_EX)

        action_ad = Util.get_list_ele(new_ad_info['data']['list'], 'otc_ad_id', ad_rsp['data']['otc_ad_id'])
        self.catch(action_ad, _except, status_code.TARGET_AD_NOT_FOUND)
        self.catch(Util.rand_eq(Util.mi(amount, action_ad['amount']),
                                Util.di(merchant_order_currency, rob_rsp['data']['unin_price'])), _except,
                   status_code.AD_SURPLUS_EX)
        self.catch(Util.rand_eq(Util.mi(amount, action_ad['available_amount']),
                                Util.di(merchant_order_currency, rob_rsp['data']['unin_price'])), _except,
                   status_code.AD_SURPLUS_EX)

    @allure.title("商户创建订单")
    def test_merchant_aa(self, merchant_action):
        res = merchant_action.create_order(1, 1, "USDT", "10")
        print(res)

    @allure.title("添加支付方式")  # type 3 银行卡
    @pytest.mark.parametrize("type,account_info,status,_except", [(3, {"bank_code": "46797249", "otc_ader_name": "张波",
                                                                       "bank_branch": "哈哈哈", "bank_name": "支行",
                                                                       "bankstr": "(****7249)"}, 2,
                                                                   status_code.EXCEPT_SUCCESS), ("abc", {
        "bank_code": "46797249", "bank_branch": "哈哈哈", "bank_name": "支行", "bankstr": "(****7249)"}, 2,
                                                                                                 status_code.PAY_INFO_EX)])
    def test_add_pay_info(self, first_ad_action, type, account_info, status, _except):
        rsp = first_ad_action.add_pay_type(type, account_info, status)
        self.catch(rsp['status_code'] == 200, _except, status_code.PAY_INFO_EX)
        list = first_ad_action.get_pay_info_list()
        self.catch(list['status_code'] == 200, _except, status_code.NETWORK_EX)
        last_add = list['data']['list'][len(list['data']['list']) - 1]
        if not (last_add['otc_ad_account_type'] == type and status == last_add['otc_account_status']):
            self.catch(False, _except, status_code.PAY_INFO_LIST_CHECK_EX)


    @allure.story("购买广告")
    @allure.title("购买广告--快速匹配--交易完成--交易流程")
    @pytest.mark.parametrize(
        "ad_type,coin_name,pay_type,pay_info,amount,min_limit,max_limit,merchant_order_currency,_except",
        [(
                2, "USDT", 3,
                {
                    "bank_code": "256",
                    "otc_ader_name": "ds",
                    "bank_branch": "cs",
                    "bank_name": "fc",
                    "bankstr": "(****6)"},
                "1000", "1",
                "100", "50",
                status_code.EXCEPT_SUCCESS)])
    def test_sell_ad(self, first_ad_action, merchant_action, admin_action, ad_type, coin_name, pay_type, pay_info,
                     amount, min_limit, max_limit, merchant_order_currency, _except):
        old_merchant_coin_finance = merchant_action.get_finance(coin_name)
        # 商户发起广告
        identify_info = first_ad_action.get_identify_info()
        self.catch(identify_info['data']['LV1_result']['type'] == "1", _except, status_code.IDENTIFY_LV1_OFF)
        ad_list_info = first_ad_action.get_ad_list()

        # 如果有买入广告 全部撤销
        self.catch(ad_list_info['status_code'] == 200, _except, status_code.NETWORK_EX)
        for item in ad_list_info['data']["list"]:
            if item['otc_ad_type'] == ad_type and (
                    item['otc_ad_status'] == bs_code.AD_ON or item['otc_ad_status'] == bs_code.AD_OFF or item['otc_ad_status'] == 0):
                rsp = first_ad_action.update_ad_status(item['otc_ad_id'], bs_code.AD_CANCEL)
                self.catch(rsp['status_code'] == 200, _except, status_code.NETWORK_EX)
        # 发起一个购买 检查自己的支付方式
        pay_list = first_ad_action.get_pay_info_list()
        self.catch(pay_list['status_code'] == 200, _except, status_code.NETWORK_EX)
        pay_status = False
        for item in pay_list['data']['list']:
            if item['otc_ad_account_type'] == pay_type and item['otc_account_status'] == bs_code.PAY_ON:
                pay_status = True
                break
        if not pay_status:
            rsp = first_ad_action.add_pay_type(pay_type, pay_info, 1)
            self.catch(rsp['status_code'] == 200, _except, status_code.NETWORK_EX)
        is_blank, is_alipay, is_wechatpay = 0, 0, 0

        if pay_type == 1:
            is_alipay = 2
        elif pay_type == 2:
            is_wechatpay = 2
        else:
            is_blank = 2

        old_ader_finance_info = first_ad_action.get_finance()

        ad_rsp = first_ad_action.create_ad(coin_name, ad_type, amount, min_limit, max_limit, is_bank=is_blank,
                                           is_alipay=is_alipay, is_wechatpay=is_wechatpay)
        self.catch(ad_rsp['status_code'] == 200, _except, status_code.CREATE_AD_FAILED)

        #企业添加支付方式 并开启
        pay_add_rsp = merchant_action.add_pay_info(pay_type,pay_info,bs_code.PAY_INFO_ON)
        self.catch(pay_add_rsp['status_code']==200,_except,status_code.MERCHANT_PAY_INFO_ADD_EX)

        # 企业发起订单
        order_info = merchant_action.create_refund( coin_name, merchant_order_currency,pay_info,pay_type)
        self.catch(order_info['status_code'] == 200, _except, status_code.MERCHANT_CREATE_OR_FAILED)
        created_order_coin_finance = merchant_action.get_finance(coin_name)

        # 商户找到订单
        ##存在订单延时状态显示机制--策略组--自动派单设置 目前跳过
        status = False
        for i in range(15):
            ad_list = first_ad_action.get_order_list()
            self.catch(ad_list['status_code'] == 200, _except, status_code.NETWORK_EX)
            for data in ad_list['data']:
                if data['OrderNumber'] == order_info['data']['order_number']:
                    status = True
                    break
            if status:
                break
        # 找到订单
        self.catch(status, _except, status_code.ORDER_NOT_FOUND)
        order_info = Util.get_list_ele(first_ad_action.get_order_list()['data'], "OrderNumber",
                                       order_info['data']['order_number'])
        self.catch(order_info['order_status'] == bs_code.ORDER_WAIT_MATE, _except, status_code.ORDER_STATUS_EX)

        rob_rsp = first_ad_action.ader_rob_order(order_info['OrderNumber'])
        self.catch(rob_rsp['status_code']==200,_except,status_code.ORDER_ROB_EX)

        # 企业平台资产检查 可用余额减少 总量不变
        coin_num = Util.di(merchant_order_currency, rob_rsp['data']['unin_price'])
        # 获取商户提币手续费
        merchant_fee_info = admin_action.admin_get_merchant_info(merchant_action.user_name)
        diff_finance = -coin_num*Util.add(1,float(merchant_fee_info['data']['list'][0]['platfrom_refund_ratio'])/100)
        self.catch(Util.eq(created_order_coin_finance['amount'], old_merchant_coin_finance['amount']), _except,
                   status_code.MERCHANT_FINANCE_EX)
        self.catch(Util.rand_eq(
            Util.mi(created_order_coin_finance['available_amount'], old_merchant_coin_finance['available_amount']
                    ), diff_finance), _except, status_code.MERCHANT_FINANCE_EX)

        #双方确认流程 包括检查订单状态
        confirm_rsp = first_ad_action.confirm_pay(rob_rsp['data']['otc_transac_id'])
        self.catch(confirm_rsp['status_code']==200,_except,status_code.CONFIRM_ORDER_EX)

        allow_rsp = merchant_action.allow_order(rob_rsp['data']['otc_transac_id'],order_info['OrderNumber'])
        self.catch(allow_rsp['status_code'] == 200, _except, status_code.ORDER_FINISH_EX)
        order_info = Util.get_list_ele(first_ad_action.get_order_list()['data'], "OrderNumber",
                                       order_info['OrderNumber'])
        self.catch(order_info['order_status'] == bs_code.ORDER_SUCCESS, _except, status_code.ORDER_STATUS_EX)

        finish_merchant_coin_finance = merchant_action.get_finance(coin_name)

        # # 此时总量减少 可用减少
        self.catch(Util.rand_eq(Util.mi(finish_merchant_coin_finance['amount'], old_merchant_coin_finance['amount']),diff_finance), _except,
                   status_code.MERCHANT_FINANCE_EX)
        self.catch(Util.rand_eq(
            Util.mi(finish_merchant_coin_finance['available_amount'], old_merchant_coin_finance['available_amount'],
                    ), diff_finance), _except, status_code.MERCHANT_FINANCE_EX)


        finish_ader_finance_info = first_ad_action.get_finance()
        old_ader_coin_finance_info = Util.get_list_ele(old_ader_finance_info['data']['list'],"coin_name",coin_name)
        finish_ader_coin_finance_info = Util.get_list_ele(finish_ader_finance_info['data']['list'],"coin_name",coin_name)
        ##商户资产检查
        self.catch(Util.rand_eq(Util.mi(finish_ader_coin_finance_info['amount'],old_ader_coin_finance_info['amount']),Util.di(merchant_order_currency,rob_rsp['data']['unin_price'])),_except,status_code.ASSETS_EX)
        self.catch(Util.rand_eq(Util.mi(finish_ader_coin_finance_info['available_amount'],old_ader_coin_finance_info['available_amount']),Util.di(merchant_order_currency,rob_rsp['data']['unin_price'])),_except,status_code.ASSETS_EX)

        # 总后台记录检查
        list = admin_action.admin_get_withdraw_transac_list(order_info["OrderNumber"])
        self.catch(list['status_code'] == 200 and len(list['data']['list']) > 0, _except, status_code.NETWORK_EX)

        # 广告剩余数量 广告总数量检查
        new_ad_info = first_ad_action.get_ad_list()
        self.catch(new_ad_info['status_code'] == 200, _except, status_code.NETWORK_EX)

        action_ad = Util.get_list_ele(new_ad_info['data']['list'], 'otc_ad_id', ad_rsp['data']['otc_ad_id'])
        self.catch(action_ad, _except, status_code.TARGET_AD_NOT_FOUND)
        self.catch(Util.rand_eq(Util.mi(amount,action_ad['amount']),Util.di(merchant_order_currency,rob_rsp['data']['unin_price'])),_except,status_code.AD_SURPLUS_EX)
        self.catch(Util.rand_eq(Util.mi(amount,action_ad['available_amount']),Util.di(merchant_order_currency,rob_rsp['data']['unin_price'])),_except,status_code.AD_SURPLUS_EX)