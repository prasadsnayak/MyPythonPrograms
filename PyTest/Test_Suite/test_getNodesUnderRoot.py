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


def test_getNodesUnderRoot_valid(test_setup):
    res = client.service.getNodesUnderRoot(setup.Userinfo_valid)
    #assert res[0]['nodeID'] == setup.rootnodeId or res[1]['nodeID'] == setup.nonboxId
    assert res[0]['nodeName'] == 'Tunnel_Bangalore' or res[1]['nodeName'] == 'Bore1'
    assert res[0]['treeLevel'] == 2 or res[1]['treeLevel'] == 3
    print(res)

def test_getUserDetails_invaliduser(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getUserDetails(setup.invalidusrname)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res