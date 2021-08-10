# 
# For consistancy we run this for our unit tests
# 
import pytest

retcode = pytest.main(['--junitxml','test-reports/tests.xml'])