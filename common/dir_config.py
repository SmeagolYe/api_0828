import os

current_file_dir = os.path.abspath(__file__)
common_dir = os.path.split(current_file_dir)[0]
base_dir = os.path.split(common_dir)[0]

case_dir = os.path.join(base_dir, "test_data", "cases.xlsx")
global_config_dir = os.path.join(base_dir, "config", "global.conf")
online_config_dir = os.path.join(base_dir, "config", "online.conf")
test_config_dir = os.path.join(base_dir, "config", "test.conf")

logs_dir = os.path.join(base_dir, "logs", "case.log")

report_dir = os.path.join(base_dir, "reports")

case_file_dir = os.path.join(base_dir, "test_case")