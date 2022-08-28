import pytest

from common.yaml_util import clear_yaml


# 在所有的接口执行之前执行，清楚的是extract文件的内容，这个文件是存放token的，因为每个接口都要使用，所以放在共文件中
@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_yaml()
