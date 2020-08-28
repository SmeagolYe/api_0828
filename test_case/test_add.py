import unittest
from common import replace
from common.httpRequest import HttpRequest
from common.do_excel import DoExcel
from ddt import ddt, data
from common.dir_config import *


@ddt
class TestAdd(unittest.TestCase):
    excel = DoExcel(case_dir, "add")
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.request = HttpRequest()

    @classmethod
    def tearDownClass(cls):
        cls.request.close()

    @data(*cases)
    def test_add(self, case):
        case.data = replace.replace(case.data)
        resp = self.request.request(method=case.method, url=case.url, data=case.data)
        try:
            self.assertEqual(str(case.expected_response), resp.json()["code"])
            self.excel.write_back(case.case_id+1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_back(case.case_id+1, resp.text, "FAIL")
            raise e