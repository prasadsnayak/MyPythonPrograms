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


def test_getAlarmsBasedOnStates_Open(test_setup):
    res = client.service.getAlarmsBasedOnStates(setup.Userinfo_valid, setup.nodeId, setup.alarmstate_Open, setup.startdate, setup.enddate )
    print(res)
    assert res[0]['state']== 'OPEN'
    assert res[0]['nodeid'] == setup.nodeId

def test_getAlarmsBasedOnStates_Open_N(test_setup):
    res = client.service.getAlarmsBasedOnStates(setup.Userinfo_valid, setup.nodeId, setup.alarmstate_Open, setup.startdate, setup.enddate)
    assert res[0]['state']!= 'CLOSED'
    assert res[0]['nodeid'] == setup.nodeId

def test_getAlarmsBasedOnStates_nouserinfo(test_setup):
    Nouser_info = "Error: 1, Description: UserInfo Not Provided-Userid and Password mandatory"
    try:
        res = client.service.getAlarmsBasedOnStates(setup.nousername,setup.nodeId, setup.alarmstate_Open, setup.startdate, setup.enddate)
    except Exception as exception:
        excp = exception.__dict__
        res = Nouser_info in excp['message']
        assert res

def test_getAlarmsBasedOnStates_invaliduser(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getAlarmsBasedOnStates(setup.invalidusrname, setup.nodeId, setup.alarmstate_Open, setup.startdate, setup.enddate)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getAlarmsBasedOnStates_invalidpassword(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getAlarmsBasedOnStates(setup.invalidpasswd, setup.nodeId, setup.alarmstate_Open, setup.startdate, setup.enddate)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getAlarmsBasedOnStates_datanotfound(test_setup):
    Nodata = "Error: 33, Description: Data Not Found For The Supplied Date Range"
    try:
        res = client.service.getAlarmsBasedOnStates(setup.Userinfo_valid, setup.nodeId, setup.alarmstate_Open, setup.nodata_startdate, setup.nodata_enddate)
    except Exception as exception:
        excp = exception.__dict__
        res = Nodata in excp['message']
        assert res

def test_getAlarmsBasedOnStates_date_endgtstart(test_setup):
    enddateerror = "Error: 21, Description: Ending date should be after starting Date"
    try:
        res = client.service.getAlarmsBasedOnStates(setup.Userinfo_valid, setup.nodeId, setup.alarmstate_Open, setup.startdate, setup.invalidenddate)
    except Exception as exception:
        excp = exception.__dict__
        res = enddateerror in excp['message']
        assert res

def test_getAlarmsBasedOnStates_invalidalarmstate(test_setup):
    invalidalarmstate = "Error: 16 Invalid alarm state list"
    try:
        res = client.service.getAlarmsBasedOnStates(setup.Userinfo_valid, setup.nodeId, setup.alarmstate_invalid, setup.startdate, setup.enddate)
    except Exception as exception:
        excp = exception.__dict__
        res = invalidalarmstate in excp['message']
        assert res