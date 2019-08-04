#pytest执行用例方法
import pytest
#1.执行单个用例
pytest.main(["-v","test_case/urse_admin/test_a.py::test_123"])
#2.执行一个python文件
pytest.main(["-v","test_case/urse_admin/test_a.py"])
#3.执行一个包里面所以python文件
pytest.main(["-v","test_case/urse_admin/"])
#4.执行全部用例
pytest.main(["-v"])
#5.执行指定的用例