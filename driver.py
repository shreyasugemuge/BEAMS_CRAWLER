from conf import Config as C
from data import parse as parser
from web import email as em, request as req
import datetime

def get_data(ddo):
    url = req.get_fund_url(ddo=ddo)
    html = req.get_raw_html(url)
    table = parser.get_raw_table_with_id(id='table2',html_str=html)
    raw_df = parser.to_dataframe(raw_table=str(table)).filter(['Scheme & Detail Head', 'Grant Received', 'Actual Exp'])
    df = parser.process_dataframe(raw_df)
    return df

def gen_section(thres,df):
    print(df.shape[0])
    if(df.shape[0] == 0):
        return ""
    final = C.SECTION_HEADER.format(color=C.COLOR[thres],thres=C.THRES[thres])
    count = 1
    for ind, data in df.iterrows():
        final += '<h4>' + str(count) + ". " + data['Scheme & Detail Head'] + ': ' + str(data['Spending']) + ' %' +'<h4>'
        count += 1
    return final

def split_df(df, thres):

    dfa = df[df['Spending'] < C.THRES[thres]]
    if (thres > 0):
        dfa = dfa[dfa['Spending'] > C.THRES[thres-1]]
    return dfa


def prettify(df):
    df.sort_values('Spending', inplace=True,ascending=True)
    df['Grant Received'] = 'Rs.' + round((df['Grant Received'] * 1000), 2).astype(str)
    df['Actual Exp'] = 'Rs.' + round((df['Actual Exp'] * 1000), 2).astype(str)
    df['Spending'] = df['Spending'].astype(str) + ' %'
    return df

def frame_data(df):
    df.sort_values('Spending', inplace=True, ascending=False)
    file = open('email_body.html','r')
    fr = file.read()
    data = fr.format(name="test", ddo="6201000362",crit="yo",
                              place="test, test", timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                              data_source="BEAMS", help_email="test@test.com", help_phone="+918805577007",
                     crit_1=gen_section(0, split_df(df, 0)),crit_2=gen_section(1, split_df(df, 1)),
                     crit_3=gen_section(2, split_df(df, 2)),crit_4=gen_section(3, split_df(df, 3)))
    file.close()
    return data

def main():
    ddo = 6201000362
    df = get_data(str(ddo))
    em.compose_and_send(fromaddr='feedback.strategy@gmail.com',frompass='26jan@2018',toaddr='ugemugeshreyas@gmail.com',name='Mr. Test Email',data=frame_data(df),ddo=ddo)

main()