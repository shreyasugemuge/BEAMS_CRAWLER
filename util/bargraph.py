
import math

from bokeh.io import export_png
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file
from bokeh.core.properties import value
from bokeh.models import LabelSet

def gen_graph(df,ddo):
    df.sort_values('Grant Received', inplace=True)
    x = df['Scheme & Detail Head']
    y1 = df['Grant Received']
    y2 = df['Actual Exp']

    source = ColumnDataSource(dict(x=x, y=y1))
    data = {
        'SDH': x,
        'Grant Received': y1,
        'Actual Exp': y2
    }

    output_file("lines.html", title="line plot example")

    plot = figure(plot_width=1200, plot_height=600,
                  x_minor_ticks=2, tools="",
                  x_range=x, title='Scheme Wise Expenditure for ddo: {0}'.format(ddo))

    plot.vbar_stack(['Grant Received', 'Actual Exp'],legend=[value(x) for x in ['Actual Expense', 'Grant Received']], source=data, x='SDH', width=0.3, color=["#c9d9d3", "#85bb65"])


    plot.xaxis.major_label_orientation = math.pi / 4
    export_png(plot, 'plot.png')


    return plot