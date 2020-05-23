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

def test_getTwilightProgram_valid(test_setup):
    setup = include_file.include_class()
    res = client.service.getTwilightProgramList(setup.Userinfo_valid, setup.nonboxId)
    programId = res['program'][0]['programId']
    res = client.service.getTwilightProgram(setup.Userinfo_valid, programId)
    assert res['statusCode'] == 0 or res['statusMessage'] == 'success'
    assert res['program'][0]['programId'] == programId
    print(res)

def test_getTwilightProgram_invaliduser(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getTwilightProgramList(setup.Userinfo_valid, setup.nonboxId)
        programId = res['program'][0]['programId']
        res = client.service.getTwilightProgram(setup.invalidusrname, programId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getTwilightProgram_invalidpassword(test_setup):
    Invalid_usercredentials = "Error: 2, Description: Invalid User Credentials"
    try:
        res = client.service.getTwilightProgramList(setup.Userinfo_valid, setup.nonboxId)
        programId = res['program'][0]['programId']
        res = client.service.getTwilightProgram(setup.invalidpasswd, programId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_usercredentials in excp['message']
        assert res

def test_getTwilightProgram_invalidpgmId(test_setup):
    Invalid_pgmid = "Error: 308, Description: Invalid Program Id"
    try:
        res = client.service.getTwilightProgramList(setup.Userinfo_valid, setup.nonboxId)
        programId = 100
        res = client.service.getTwilightProgram(setup.Userinfo_valid, programId)
    except Exception as exception:
        excp = exception.__dict__
        res = Invalid_pgmid in excp['message']
        assert res

def test_getTwilightProgram_nouserinfo(test_setup):
    Nouser_info = "Error: 1, Description: UserInfo Not Provided-Userid and Password mandatory"
    try:
        res = client.service.getTwilightProgramList(setup.Userinfo_valid, setup.nonboxId)
        programId = res['program'][0]['programId']
        res = client.service.getTwilightProgram(setup.nousername, programId)
    except Exception as exception:
        excp = exception.__dict__
        res = Nouser_info in excp['message']
        assert res
