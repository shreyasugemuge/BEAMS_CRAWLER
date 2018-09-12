from util import bargraph as bar
from util import parse as parser
from bokeh.plotting import show
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
    df.sort_values('Grant Received', inplace=True)
    data = "Dear {name},<BR>Below is the DDO Scheme Wise Expenditure Summary<BR><CENTER>" + df.to_html(index=False, justify='center') + "<CENTER><BR>"
    return data

em.compose_and_send(fromaddr='feedback.strategy@gmail.com',frompass='26jan@2018',toaddr='ugemugeshreyas@gmail.com',name='Mr. Test Email',data=frame_data(df))


