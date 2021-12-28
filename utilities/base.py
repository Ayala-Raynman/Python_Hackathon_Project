from page_objects.web.main_page import main_page

# Web globals
driver = None
user_Id = 10

# my data base globals
mydb = None
data_list = None
globals()['data_list'] = None
param_name = "user_name, password,amount"

# appium globals
reportDirectory = 'reports'
reportFormat = 'xml'
dc = {}
testName = 'Untitled'
# driver = None