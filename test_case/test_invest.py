import unittest
from common.do_excel import DoExcel
from common.httpRequest import HttpRequest
from common.dir_config import *
from common.config import *
from ddt import ddt, data
from common.do_mysql import DoMysql
from common import replace


@ddt
class TestInvest(unittest.TestCase):
    excel = DoExcel(case_dir, "invest")
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
    def test_invest(self, case):
        case.data = replace.replace(case.data)
        resp = self.request.request(method=case.method, url=case.url, data=case.data)

        try:
            self.assertEqual(str(case.expected_response), resp.json()["code"])
            self.excel.write_back(case.case_id+1, resp.text, "PASS")

            if resp.json()["msg"] == "加标成功":
                sql = "select id from future.loan where memberId = 1231 order by id desc limit 1"
                loan_id = self.mysql.fetchone(sql)["id"]
                setattr(replace.Context, "loan_id", str(loan_id))

        except AssertionError as e:
            self.excel.write_back(case.case_id+1, resp.text, "FAIL")
            raise e