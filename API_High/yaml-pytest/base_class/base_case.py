import pytest
class BaseCase:
    def catch(self, b: object, _except: object, status_code: object) -> object:
        # 异常的错误 抛出
        # 期待的错误 跳出
        # 正常的流程 放过
        if b:
            return

        if _except['code'] == status_code['code']:
            pytest.xfail(reason="期待的错误:"+_except['msg'])
        else:
            assert 1 == 2, status_code['msg']
