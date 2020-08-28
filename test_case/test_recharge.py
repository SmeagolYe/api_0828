import unittest
from common.httpRequest import HttpRequest
from common.dir_config import *
from ddt import ddt, data
from common.do_excel import DoExcel
from common import replace
from common.do_mysql import DoMysql


@ddt
class TestRecharge(unittest.TestCase):
    excel = DoExcel(case_dir, "recharge")
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        print("begin")
        cls.request = HttpRequest()
        cls.mysql = DoMysql()

    @classmethod
    def tearDownClass(cls):
        cls.request.close()
        cls.mysql.close()
        print("over")

    @data(*cases)
    def test_recharge(self, case):
        if case.sql is not None:
            sql = eval(case.sql)['sql1']
            print(sql)
            sql_result = self.mysql.fetchone(sql)
            print(sql_result)
            before_recharge = float(sql_result["LeaveAmount"])
            print(before_recharge)

        case.data = replace.replace(case.data)
        resp = self.request.request(method=case.method, url=case.url, data=case.data)
        try:
            self.assertEqual(resp.json()["code"], str(case.expected_response))
            self.excel.write_back(case.case_id+1, resp.text, "PASS")
            if case.sql is not None:
                sql = eval(case.sql)["sql1"]
                sql_result = self.mysql.fetchone(sql)
                after_recharge = float(sql_result["LeaveAmount"])
                print(after_recharge)
                recharge_amount = float(eval(case.data)["amount"])
                print(recharge_amount)

                self.assertEqual(before_recharge + recharge_amount, after_recharge)
        except AssertionError as e:
            self.excel.write_back(case.case_id+1, resp.text, "FAIL")
            raise e