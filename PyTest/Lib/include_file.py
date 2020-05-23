from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep import Client
from zeep.transports import Transport

import sys
sys.path.append('../')
from Locators.locators import Locators

#Asia shadow server
class include_class():
    def __init__(self):
        self.Userinfo_valid = {'userId': Locators.username, 'password': Locators.password}
        self.invalidusrname = {'userid': Locators.invalidusrname, 'password': Locators.password}
        self.invalidpasswd = {'userid': Locators.username, 'password': Locators.invalidpasswd}
        self.nousername = {'userid': Locators.nousername, 'password': Locators.password}
        self.nopsswd = {'userid': Locators.username, 'password': Locators.nopsswd}
        self.rootnodeId = Locators.rootnodeId
        self.nodeId = Locators.nodeId
        self.nonboxId = Locators.nonboxId
        self.norecordnodeId = Locators.norecordnodeId
        self.rootnodeName = Locators.rootnodeName
        self.masterNode = Locators.masterNode
        self.commandId_Auto = Locators.commandId_Auto
        self.commandId_On = Locators.commandId_On
        self.commandId_Off = Locators.commandId_Off
        self.commandId_Scene1 = Locators.commandId_Scene1
        self.invalidcmdId = Locators.invalidcmdId
        self.invalidnodeId = Locators.invalidnodeId
        self.startdate = Locators.startdate
        self.enddate = Locators.enddate
        self.nodata_startdate = Locators.nodata_startdate
        self.nodata_enddate = Locators.nodata_enddate
        self.invalidenddate = Locators.invalidenddate
        self.alarmstate_Open = Locators.alarmstate_Open
        self.alarmstate_Closed = Locators.alarmstate_Closed
        self.alarmstate_invalid = Locators.alarmstate_invalid
        self.alarmseverity_ALL = Locators.alarmseverity_ALL
        self.alarmseverity_FIVE = Locators.alarmseverity_FIVE

class setup_class():
    def __init__(self):
        self.WSDL_URL = Locators.WSDL_URL
        self.WSDL_USERNAME = Locators.username
        self.WSDL_PASSWORD = Locators.password
        # self.proxy = {
        #     "http":"http://prasad.nayak@signify.com:Udipu@2016@zscaler.proxy.intra.lighting.com:9480",
        #     "https":"https://prasad.nayak@signify.com:Udipu@2016@zscaler.proxy.intra.lighting.com:9480"
        # }
        self.proxy = Locators.proxy
        self.ssl_cert = Locators.ssl_cert
        self.session = Session()

    def Session(self,session, WSDL_URL, proxy, ssl_cert, WSDL_USERNAME, WSDL_PASSWORD):
        self.session.auth = HTTPBasicAuth(WSDL_USERNAME, WSDL_PASSWORD)
        self.session.proxies = proxy
        self.session.verify = ssl_cert
        self.client = Client(WSDL_URL, transport=Transport(session=session))
        return self.client