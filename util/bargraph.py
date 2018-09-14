
import math

from bokeh.io import export_png
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

def gen_graph(df,ddo):
    xs = df['Scheme & Detail Head'].tolist()
    ys = ['Grant Received', 'Actual Exp']

    data = {'xs': xs,
            'Grant Received': df['Grant Received'].tolist(),
            'Actual Exp': df['Actual Exp'].tolist()}

    palette = ["#c9d9d3", "#718dbf"]


    x = [(fr, yr) for fr in xs for yr in ys]
    counts = sum(zip(data['Grant Received'], data['Actual Exp']), ())  # like an hstack

    source = ColumnDataSource(data=dict(x=x, counts=counts))

    p = figure(x_range=FactorRange(*x), plot_height=350, title="ddo: " + str(ddo),
               toolbar_location=None, tools="")

    p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
           fill_color=factor_cmap('x', palette=palette, factors=ys, start=1, end=2))

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = "vertical"
    p.xaxis.group_text_font_size = '5pt'
    p.xaxis.group_text_align = 'right'
    p.xgrid.grid_line_color = None
    export_png(p, 'plot.png')
    return p