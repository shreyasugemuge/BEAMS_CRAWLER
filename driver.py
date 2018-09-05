from util import parse as parser
from util import request as req


def get_data(ddo):
    url = req.get_fund_url(ddo=ddo)
    html = req.get_raw_html(url)
    table = parser.get_raw_table_with_id(id='table2',html_str=html)
    raw_df = parser.to_dataframe(raw_table=str(table)).filter(['Scheme & Detail Head', 'Grant Received', 'Actual Exp'])
    df = parser.process_dataframe(raw_df)
    return df

