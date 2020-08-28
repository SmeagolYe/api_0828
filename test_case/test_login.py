import unittest
from common.httpRequest import HttpRequest
from common.do_excel import DoExcel
from common.dir_config import *
from ddt import ddt, data
from common import replace
import os
from common import logger


mylogger = logger.get_logger(os.path.split(__file__)[1])

@ddt
class TestLogin(unittest.TestCase):
    excel = DoExcel(case_dir, "login")
    cases = excel.get_cases()

    def setUp(self):
        mylogger.info("前置")
        self.request = HttpRequest()

    def tearDown(self):
        self.request.close()
        mylogger.info("后置")

    @data(*cases)
    def test_login(self, case):
        mylogger.info("执行第{0}条用例：{1}".format(case.case_id, case.title))
        case.data = replace.replace(case.data)
        resp = self.request.request(method=case.method, url=case.url, data=case.data)
        try:
            self.assertEqual(resp.text, case.expected_response)
            self.excel.write_back(case.case_id+1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_back(case.case_id+1, resp.text, "FAIL")
            mylogger.error("报错了，{0}".format(e))
            raise e
        mylogger.info("结束测试第{0}条用例：{1}".format(case.case_id, case.title))
