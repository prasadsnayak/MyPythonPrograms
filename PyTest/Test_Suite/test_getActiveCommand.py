import pytest
import sys
sys.path.append('../')

from Lib.include_file import include_class
from Lib.include_file import setup_class


@pytest.fixture(scope="module")
def test_setup():
    init = setup_class()
    #global client
    client = init.Session(init.session, init.WSDL_URL, init.proxy, init.ssl_cert, init.WSDL_USERNAME, init.WSDL_PASSWORD)
    #global setup
    setup = include_class()
    #yield
    yield from (setup, client)
    print('Test Completed')

def test_getActiveCommand_valid(test_setup):
    print(setup.Userinfo_valid)
    res = client.service.getActiveCommand(setup.Userinfo_valid, setup.nodeId)
    assert res['boxSerialNumber'] == 4004000310
    assert res['nodeId'] == setup.nodeId



def test_getActiveCommand_nouserinfo(test_setup):
    Nouser_info = "Error: 1, Description: UserInfo Not Provided-Userid and Password mandatory"
    try:
        res = client.service.getActiveCommand(setup.nousername, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Nouser_info in excp['message']
        assert res

def test_getActiveCommand_invaliduser(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getActiveCommand(setup.invalidusrname, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getActiveCommand_invalidpassword(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getActiveCommand(setup.invalidpasswd, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getActiveCommand_nonodeid(test_setup):
    No_nodeid = "Error: 109, Description: Node ID is required"
    try:
        res = client.service.getActiveCommand(setup.Userinfo_valid,)
    except Exception as exception:
        excp = exception.__dict__
        res = No_nodeid in excp['message']
        assert res

def test_getActiveCommand_invalidnode(test_setup):
    Invalid_nodeid = "Error: 110, Description: Node id is invalid"
    try:
        res = client.service.getActiveCommand(setup.Userinfo_valid, setup.invalidnodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_nodeid in excp['message']
        assert res

def test_getActiveCommand_norecords(test_setup):
    norecords = "Error: 111, Description: No records found"
    try:
        res = client.service.getActiveCommand(setup.Userinfo_valid, setup.norecordnodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = norecords in excp['message']
        assert res