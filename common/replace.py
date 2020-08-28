import re
from common.config import *


class Context:
    loan_id = None


def replace(data):
    pattern = "#(.*?)#"
    while re.search(pattern, data):
        m = re.search(pattern, data)
        g = m.group(1)
        try:
            v = config.get("data", g)
        except configparser.NoOptionError as e:
            if hasattr(Context, g):
                v = getattr(Context, g)
            else:
                print("找不到laon_id参数化的值")
                raise e

        data = re.sub(pattern, v, data, count=1)

    return data
