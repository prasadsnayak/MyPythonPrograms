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

def test_getCustomerScenes_valid(test_setup):
    res = client.service.getCustomerScenes(setup.Userinfo_valid)
    assert (res[0]['commandId'] == 1 and res[0]['commandName'] == 'ON')
    assert (res[1]['commandId'] == 2 and res[1]['commandName'] == 'OFF')
    assert (res[2]['commandId'] == 5 and res[2]['commandName'] == 'SCENE1')
    assert (res[3]['commandId'] == 6 and res[3]['commandName'] == 'SCENE2')
    assert (res[4]['commandId'] == 7 and res[4]['commandName'] == 'SCENE3')
    assert (res[5]['commandId'] == 8 and res[5]['commandName'] == 'SCENE4')
    assert (res[6]['commandId'] == 9 and res[6]['commandName'] == 'SCENE5')
    assert (res[7]['commandId'] == 10 and res[7]['commandName'] == 'SCENE6')
    assert (res[8]['commandId'] == 11 and res[8]['commandName'] == 'SCENE7')
    assert (res[9]['commandId'] == 12 and res[9]['commandName'] == 'SCENE8')
    assert (res[10]['commandId'] == 13 and res[10]['commandName'] == 'SCENE9')
    assert (res[11]['commandId'] == 14 and res[11]['commandName'] == 'SCENE10')
    assert (res[12]['commandId'] == 15 and res[12]['commandName'] == 'SCENE11')
    assert (res[13]['commandId'] == 16 and res[13]['commandName'] == 'SCENE12')

def test_getCustomerScenes_invaliduser(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getCustomerScenes(setup.invalidusrname)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getCustomerScenes_invalidpassword(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getCustomerScenes(setup.invalidpasswd)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getCustomerScenes_nousername(test_setup):
    Nouser_info = "Error: 1, Description: UserInfo Not Provided-Userid and Password mandatory"
    try:
        res = client.service.getCustomerScenes(setup.nousername)
    except Exception as exception:
        excp = exception.__dict__
        res = Nouser_info in excp['message']
        assert res