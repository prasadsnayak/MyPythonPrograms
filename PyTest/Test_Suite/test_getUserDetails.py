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


def test_getUserDetails_valid(test_setup):
    Language_ID = 17
    Language = 'English (United Kingdom)'
    timezone = "GMT +05:30 Chennai, Kolkata, Mumbai, New Delhi"
    timezone_id = 67
    res = client.service.getUserDetails(setup.Userinfo_valid)
    assert res['languageID'] == Language_ID
    assert res['timeZoneDescription'] == timezone
    assert res['timeZoneID'] == timezone_id
    assert res['userLocale'] == Language

def test_getUserDetails_nouserinfo(test_setup):
    Nouser_info = "Error: 1, Description: UserInfo Not Provided-Userid and Password mandatory"
    try:
        res = client.service.getUserDetails(setup.nousername)
    except Exception as exception:
        excp = exception.__dict__
        res = Nouser_info in excp['message']
        assert res

def test_getUserDetails_invaliduser(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getUserDetails(setup.invalidusrname)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getUserDetails_invalidpassword(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getUserDetails(setup.invalidpasswd)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res