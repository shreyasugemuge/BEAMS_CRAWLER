from util import bargraph as bar
from util import parse as parser
from util import request as req
from util import email as em

def get_data(ddo):
    url = req.get_fund_url(ddo=ddo)
    html = req.get_raw_html(url)
    table = parser.get_raw_table_with_id(id='table2',html_str=html)
    raw_df = parser.to_dataframe(raw_table=str(table)).filter(['Scheme & Detail Head', 'Grant Received', 'Actual Exp'])
    df = parser.process_dataframe(raw_df)
    return df


ddo = 6201000362
df = get_data(str(ddo))
plot = bar.gen_graph(df, ddo)


def frame_data(df):
    df.sort_values('Spending', inplace=True,ascending=False)
    df['Grant Received'] = 'Rs.' + round((df['Grant Received'] * 1000), 2).astype(str)
    df['Actual Exp'] = 'Rs.' + round((df['Actual Exp'] * 1000), 2).astype(str)
    df['Spending'] = df['Spending'].astype(str) + ' %'

    data = "Dear {name}," \
           "<BR><BR>This email is to notify you about budget spending and the lack thereof." \
           " There are certain schemes pertaining with your DDO: " \
           "{ddo} that appear to have very low spending as of 14 September 2018. " \
           "You are requested to look into the following schemes personally. " \
           "A summary of the same has been given below.<BR><HR><BR><BR>" \
           "<CENTER>" + df.to_html(index=False, justify='center')\
           + "</CENTER>" \
           "<BR><BR><BR><HR>"
    return data

em.compose_and_send(fromaddr='feedback.strategy@gmail.com',frompass='26jan@2018',toaddr='dvishwas79@gmail.com',name='Mr. Test Email',data=frame_data(df),ddo=ddo)


