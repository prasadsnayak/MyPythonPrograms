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


def test_setControlCommand_valid(test_setup):
    res = client.service.setControlCommand(setup.Userinfo_valid, setup.commandId_On, setup.nodeId)
    assert res == 0

def test_setControlCommand_nouserinfo(test_setup):
    Nouser_info = "Error: 1, Description: UserInfo Not Provided-Userid and Password mandatory"
    try:
        res = client.service.setControlCommand(setup.nousername, setup.commandId_Auto, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Nouser_info in excp['message']
        assert res


def test_setControlCommand_invaliduser(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.setControlCommand(setup.invalidusrname, setup.commandId_Auto, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_setControlCommand_invalidpassword(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.setControlCommand(setup.invalidpasswd, setup.commandId_Auto, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_setControlCommand_invalidcmdId(test_setup):
    Invalid_cmmdId = "Error: 8, Description: Invalid Command ID Provided"
    try:
        res = client.service.setControlCommand(setup.Userinfo_valid, setup.invalidcmdId, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_cmmdId in excp['message']
        assert res

def test_setControlCommand_invalidnode(test_setup):
    Invalid_nodeid = "Error: 110, Description: Node id is invalid"
    try:
        res = client.service.setControlCommand(setup.Userinfo_valid, setup.commandId_Auto, setup.invalidnodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_nodeid in excp['message']
        assert res