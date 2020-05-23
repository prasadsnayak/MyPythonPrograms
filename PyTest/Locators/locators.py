class Locators():

    username = "salimsalam"
    password = "Qwerty@123456"
    invalidusrname = "standalone2_usr1"
    invalidpasswd = "Qwerty@12345611"
    nousername = ""
    nopsswd = ""

    rootnodeId = 20
    nodeId = 23
    nonboxId = 21
    NonodeId = None
    norecordnodeId = 26
    masterNode = 'Portal'
    rootnodeName = 'Salim Salam'

    commandId_Auto = 0
    commandId_On = 1
    commandId_Off = 2
    commandId_Scene1 = 5
    invalidcmdId = 20
    invalidnodeId = 0

    startdate = {'Day': '1', 'Month': '1', 'Year': '2020'}
    enddate = {'Day': '28', 'Month': '1', 'Year': '2020'}
    nodata_startdate = {'Day': '19', 'Month': '1', 'Year': '2008'}
    nodata_enddate = {'Day': '28', 'Month': '1', 'Year': '2008'}
    invalidenddate = {'Day': '31', 'Month': '12', 'Year': '2019'}

    alarmstate_Open = {'alarmStateList': 'OPEN'}
    alarmstate_Closed = {'alarmStateList': 'CLOSED'}
    alarmstate_invalid = {'alarmStateList': 'XXXX'}
    alarmseverity_ALL = {'severitycode': 'ALL'}
    alarmseverity_FIVE = {'severitycode': 'FIVE'}

    WSDL_URL = "https://192.168.10.19:8001/BaseLogicAPI/BaseLogicWebService?wsdl"
    # proxy = {
    #     "http":"http://prasad.nayak@signify.com:Udipu@2016@zscaler.proxy.intra.lighting.com:9480",
    #     "https":"https://prasad.nayak@signify.com:Udipu@2016@zscaler.proxy.intra.lighting.com:9480"
    # }
    proxy = {}
    ssl_cert = False