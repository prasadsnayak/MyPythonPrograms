import pytest

import sys
sys.path.append('../')

from Lib.include_file import include_class
from Lib.include_file import setup_class

@pytest.fixture()
def test_setup():
    init = setup_class()
    global client
    client = init.Session(init.session, init.WSDL_URL, init.proxy, init.ssl_cert, init.WSDL_USERNAME, init.WSDL_PASSWORD)
    global setup
    setup = include_class()
    yield
    print('Test Completed')


def test_getBaselogicAPIVersion_validuser(test_setup):
    res = client.service.getBaselogicAPIVersion(setup.Userinfo_valid)
    assert res == '1.1.0'

def test_getBaselogicAPIVersion_invaliduser(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getBaselogicAPIVersion(setup.invalidusrname)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getBaselogicAPIVersion_invalidpassword(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getBaselogicAPIVersion(setup.invalidpasswd)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getBaselogicAPIVersion_Nousername(test_setup):
    Nouser_info = "Error: 1, Description: UserInfo Not Provided-Userid and Password mandatory"
    try:
        res = client.service.getBaselogicAPIVersion(setup.nousername)
    except Exception as exception:
        excp = exception.__dict__
        res = Nouser_info in excp['message']
        assert res

def test_getBaselogicAPIVersion_Nopassword(test_setup):
    Nouser_info = "Error: 1, Description: UserInfo Not Provided-Userid and Password mandatory"
    try:
        res = client.service.getBaselogicAPIVersion(setup.nopsswd)
    except Exception as exception:
        excp = exception.__dict__
        res = Nouser_info in excp['message']
        assert res