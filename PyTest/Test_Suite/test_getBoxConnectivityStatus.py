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


def test_getBoxConnectivityStatus_valid(test_setup):
    res = client.service.getBoxConnectivityStatus(setup.Userinfo_valid, setup.nodeId)
    assert res['boxNodeId'] == setup.nodeId
    assert res['boxConnectivityStatus']== 'ACTIVE' or res['boxConnectivityStatus']=='DOWN' or res['boxConnectivityStatus']=='INACTIVE'

def test_getBoxConnectivityStatus_nouserinfo(test_setup):
    Nouser_info = "Error: 1, Description: UserInfo Not Provided-Userid and Password mandatory"
    try:
        res = client.service.getBoxConnectivityStatus(setup.nousername, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Nouser_info in excp['message']
        assert res

def test_getBoxConnectivityStatus_invaliduser(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getBoxConnectivityStatus(setup.invalidusrname, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getBoxConnectivityStatus_invalidpassword(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getBoxConnectivityStatus(setup.invalidpasswd, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getBoxConnectivityStatus_nonodeid(test_setup):
    No_nodeid = "Error: 109, Description: Node ID is required"
    try:
        res = client.service.getBoxConnectivityStatus(setup.Userinfo_valid,)
    except Exception as exception:
        excp = exception.__dict__
        res = No_nodeid in excp['message']
        assert res

def test_getBoxConnectivityStatus_invalidnode(test_setup):
    Invalid_nodeid = "Error: 110, Description: Node id is invalid"
    try:
        res = client.service.getBoxConnectivityStatus(setup.Userinfo_valid,setup.invalidnodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_nodeid in excp['message']
        assert res

def test_getBoxConnectivityStatus_nonboxnodeid(test_setup):
    nonbox_nodeId = "Error: 278, Description: Box Node id invalid"
    try:
        res = client.service.getBoxConnectivityStatus(setup.Userinfo_valid,setup.nonboxId)
    except Exception as exception:
        excp = exception.__dict__
        res = nonbox_nodeId in excp['message']
        assert res