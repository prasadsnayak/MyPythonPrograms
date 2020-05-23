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


def test_getAlarmsBasedOnSeverity_ALL(test_setup):
    res = client.service.getAlarmsBasedOnSeverity(setup.Userinfo_valid, setup.nodeId, setup.alarmseverity_ALL, setup.startdate, setup.enddate)
    print(res)

def test_getAlarmsBasedOnSeverity_FIVE(test_setup):
    res = client.service.getAlarmsBasedOnSeverity(setup.Userinfo_valid, setup.nodeId, setup.alarmseverity_FIVE, setup.startdate, setup.enddate)
    print(res)