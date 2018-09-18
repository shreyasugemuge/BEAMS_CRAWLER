import ssl
from urllib.request import urlopen

from conf import Config as const


def get_fund_url(ddo):
    return const.FUND_REPORT_BASE_URL + '&ddo=' + ddo

def get_raw_html(url):
    context = ssl._create_unverified_context()
    html = urlopen(url, context=context).read().decode('utf-8')
    return html

