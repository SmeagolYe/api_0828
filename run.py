import unittest
from common.dir_config import *
import HTMLTestReportCN

suite = unittest.defaultTestLoader.discover(case_file_dir, "test_*.py")

with open(report_dir + "/report.html", "wb+") as file:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=file, title="测试报告", description="QQ音乐", tester="叶婷")
    runner.run(suite)