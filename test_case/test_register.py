import unittest
from common.httpRequest import HttpRequest
from common.do_mysql import DoMysql
from ddt import ddt, data
from common.do_excel import DoExcel
from common.dir_config import *


@ddt
class TestRegister(unittest.TestCase):
    excel = DoExcel(case_dir, "register")
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.request = HttpRequest()
        cls.mysql = DoMysql()

    @classmethod
    def tearDownClass(cls):
        cls.request.close()
        cls.mysql.close()

    @data(*cases)
    def test_register(self, case):
        if case.data.find("register_mobile"):
            sql = "select max(mobilephone) from future.member"

            register_mobile = int(self.mysql.fetchone(sql)["max(mobilephone)"]) + 100
            case.data = case.data.replace("register_mobile", str(register_mobile))
            print(case.data)

        resp = self.request.request(method=case.method, url=case.url, data=case.data)

        try:
            self.assertEqual(resp.text, case.expected_response)
            self.excel.write_back(case.case_id+1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_back(case.case_id+1, resp.text, "FAIL")
            raise e