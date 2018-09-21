# DATA FETCH CONFIG
FUND_REPORT_BASE_URL = 'https://beams.mahakosh.gov.in/Beams5/BudgetMVC/MISRPT/DDO_FundReport.jsp?year=2018-2019&dist=0&type=All'
SCHEME_HEADER = '20550168'

# set thresholds here. 4 criteria for minimium spending %
THRES = [10, 20, 40, 60]
COLOR = ['#bd1a2b', '#bd431a', '#bd6614', '#cbc02']

# TEST
DDO_TEST = 6201000362
NAME_TEST = 'Mr. Vishwas Deshpande'

# EMAIL CONTENT CONFIG
EMAIL_SUBJECT = "DDO Expense reminder: {DDO}"
DATA_SOURCE = "BEAMS (https://beams.mahakosh.gov.in/)"
HELP_EMAIL = "feedback.strategy@gmail.com"
HELP_PHONE = "+918805577007"
LOGO_FILENAME = 'Logo.jpeg'
PLACE_TEST='Akola'

# EMAIL CONFIG
TO_ADDR = 'ugemugeshreyas@gmail.com'
FROM_PASS = '26jan@2018'
FROM_ADDR = 'feedback.strategy@gmail.com'

# EMAIL FORMAT CONFIG
SECTION_HEADER = '<HR color={color}><h3>Spending below {thres} %</h3>'
STRF_FORMAT = "%Y-%m-%d %H:%M"
SCHEME_DICT_QUERY = "SELECT * FROM SCHEME_HEAD"
SQLITE_DB_ENDPOINT = 'data.db'

# LOGGER
DEBUG_PORT = 8881
INFO_PORT = 8882
ERROR_PORT = 8883