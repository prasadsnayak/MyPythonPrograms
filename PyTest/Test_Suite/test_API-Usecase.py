import time
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

def test_API_Usecase_SwitchingOperation_ON(test_setup):
    res = client.service.getNodesUnderRoot(setup.Userinfo_valid)
    x = len(res)
    for i in range(x):
        if res[i]['nodeName'] == setup.rootnodeName:
            nodeid = res[i]['nodeID']
            res1 = client.service.getAllSubNodes(setup.Userinfo_valid, nodeid)
            print(res1)
            y = len(res1)

            for j in range(y):
                if ('boxID' in res1[j]) and (res1[j]['nodeName'] == setup.masterNode):
                    boxNodeId = res1[j]['nodeID']
                    print(boxNodeId)
                    res2 = client.service.setControlCommand(setup.Userinfo_valid, setup.commandId_On, boxNodeId)
                    time.sleep(10)
                    if not res2:
                        res3 = client.service.getActiveCommand(setup.Userinfo_valid, boxNodeId)
                        assert res3['commandId'] == setup.commandId_On
                        exit

def test_API_Usecase_SwitchingOperation_OFF(test_setup):
    res = client.service.getNodesUnderRoot(setup.Userinfo_valid)
    x = len(res)
    for i in range(x):
        if res[i]['nodeName'] == setup.rootnodeName:
            nodeid = res[i]['nodeID']
            res1 = client.service.getAllSubNodes(setup.Userinfo_valid, nodeid)
            print(res1)
            y = len(res1)

            for j in range(y):
                if ('boxID' in res1[j]) and (res1[j]['nodeName'] == setup.masterNode):
                    boxNodeId = res1[j]['nodeID']
                    print(boxNodeId)
                    res2 = client.service.setControlCommand(setup.Userinfo_valid, setup.commandId_Off, boxNodeId)
                    time.sleep(10)
                    if not res2:
                        res3 = client.service.getActiveCommand(setup.Userinfo_valid, boxNodeId)
                        assert res3['commandId'] == setup.commandId_Off
                        exit

def test_API_Usecase_SwitchingOperation_SCENE1(test_setup):
    res = client.service.getNodesUnderRoot(setup.Userinfo_valid)
    x = len(res)
    for i in range(x):
        if res[i]['nodeName'] == setup.rootnodeName:
            nodeid = res[i]['nodeID']
            res1 = client.service.getAllSubNodes(setup.Userinfo_valid, nodeid)
            print(res1)
            y = len(res1)

            for j in range(y):
                if ('boxID' in res1[j]) and (res1[j]['nodeName'] == setup.masterNode):
                    boxNodeId = res1[j]['nodeID']
                    print(boxNodeId)
                    res2 = client.service.setControlCommand(setup.Userinfo_valid, setup.commandId_Scene1, boxNodeId)
                    time.sleep(10)
                    if not res2:
                        res3 = client.service.getActiveCommand(setup.Userinfo_valid, boxNodeId)
                        assert res3['commandId'] == setup.commandId_Scene1
                        exit