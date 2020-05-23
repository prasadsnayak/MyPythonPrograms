#!/usr/bin/python
import os
import time
import logging
#import HtmlTestRunner

now = time.strftime('%Y%m%d') + '_' + time.strftime('%H%M%S')
logfile = '..\..\PyTest\Reports' + '\\'+  'BaseLogic_Test_Report' + '_' + now +'.html'
	
#cmd = "pytest -v --capture=sys | tee " + logfile
cmd_logfile = "pytest -v | tee " + logfile
cmd_html = "pytest --html=" + logfile + " --self-contained-html"
## run it ##
os.system(cmd_html)
#os.system(cmd_logfile)