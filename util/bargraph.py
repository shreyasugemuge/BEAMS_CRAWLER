
import math

from bokeh.io import export_png
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file


def gen_graph(df):
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
                  x_minor_ticks=2,
                  x_range=x)

    plot.vbar_stack(['Grant Received', 'Actual Exp'], source=data, x='SDH', width=0.3, color=["#c9d9d3", "#85bb65"])

    plot.xaxis.major_label_orientation = math.pi / 4
    export_png(plot, 'plot.png')
    return plot