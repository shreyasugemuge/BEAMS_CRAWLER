import datetime

from config import DATA_SOURCE, HELP_EMAIL, HELP_PHONE, STRF_FORMAT, NAME_TEST, TO_ADDR, FROM_PASS, FROM_ADDR, \
    DDO_TEST, PLACE_TEST
from data import parse as parser
from data.parse import split_df
from web import email as em, request as req
from web.email import gen_section


def get_data(ddo):
    print("fetching data")
    url = req.get_fund_url(ddo=ddo)
    html = req.get_raw_html(url)
    print("fetched raw HTML")
    table = parser.get_raw_table_with_id(id='table2', html_str=html)
    raw_df = parser.to_dataframe(raw_table=str(table)).filter(['Scheme & Detail Head', 'Grant Received', 'Actual Exp'])
    df = parser.process_dataframe(raw_df)
    print("processed data")
    return df

def get_place(ddo):
    pass

def frame_data(df, ddo):
    df.sort_values('Spending', inplace=True, ascending=False)
    file = open('email_body.html', 'r')
    fr = file.read()
    print("Formatting Email")
    data = fr.format(name=NAME_TEST, ddo=str(ddo),
                     place=PLACE_TEST, timestamp=datetime.datetime.now().strftime(STRF_FORMAT),
                     data_source=DATA_SOURCE, help_email=HELP_EMAIL, help_phone=HELP_PHONE,
                     crit_1=gen_section(0, split_df(df, 0)), crit_2=gen_section(1, split_df(df, 1)),
                     crit_3=gen_section(2, split_df(df, 2)), crit_4=gen_section(3, split_df(df, 3)))
    file.close()
    return data

def main():
    ddo = DDO_TEST
    print("Initializing..")
    df = get_data(str(ddo))

    em.compose_and_send(fromaddr=FROM_ADDR, frompass=FROM_PASS,
                        toaddr=TO_ADDR, data=frame_data(df, ddo), ddo=ddo)


main()