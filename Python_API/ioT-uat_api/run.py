'''
@Author: xiaomin
@Date: 2020-04-26 15:42:52
@LastEditTime: 2020-05-11 11:30:05
@LastEditors: xiaomin
@Description: 
@FilePath: \ioT-uat\run.py
'''
import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from HTMLTestRunner import HTMLTestRunner
import unittest
import time,os

if __name__ == "__main__":
    test_dir='\\ioT-uat\\Testcase'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

    now=time.strftime('%Y-%m-%d %H_%M_%S')
    #定义报告存放路径
    filename='\\ioT-uat\\Report\\report'+now+'result.html'
    fp=open(filename,'wb')
    #定义测试报告
    runner=HTMLTestRunner(stream=fp,title='uat_硬件云2.0api业务流程测试报告',description='用例执行情况:')
    runner.run(discover,rerun=0, save_last_run=False)
    fp.close()