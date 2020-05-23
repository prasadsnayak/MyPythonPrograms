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

def test_getTwilightProgramList_valid(test_setup):
    res = client.service.getTwilightProgramList(setup.Userinfo_valid, setup.rootnodeId)
    assert res['statusCode'] == 0 or res['statusMessage'] == 'success'
    print(res)

def test_getTwilightProgramList_invaliduser(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getTwilightProgramList(setup.invalidusrname, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getTwilightProgramList_invalidpassword(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getTwilightProgramList(setup.invalidpasswd, setup.nodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getTwilightProgramList_nonodeid(test_setup):
    No_nodeid = "Error: 109, Description: Node ID is required"
    try:
        res = client.service.getTwilightProgramList(setup.Userinfo_valid,setup.NonodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = No_nodeid in excp['message']
        assert res

def test_getTwilightProgramList_invalidnode(test_setup):
    Invalid_nodeid = "Error: 110, Description: Node id is invalid"
    try:
        res = client.service.getTwilightProgramList(setup.Userinfo_valid,setup.invalidnodeId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_nodeid in excp['message']
        assert res

def test_getTwilightProgramList_nonboxnodeid(test_setup):
    nonbox_nodeId = "Error: 278, Description: Box Node id invalid"
    try:
        res = client.service.getTwilightProgramList(setup.Userinfo_valid,setup.nonboxId)
    except Exception as exception:
        excp = exception.__dict__
        res = nonbox_nodeId in excp['message']
        assert res