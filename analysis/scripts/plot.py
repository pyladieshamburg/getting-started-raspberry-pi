import plotly.graph_objs as go
from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool
from bokeh.plotting import figure


def bohek_slider(df, col, title=None):

    titledwd = 'Official Outdoor Observations Braunschweig (City Center) Germany'

    dates = df.index.values
    source = ColumnDataSource(data=dict(date=dates, close=df[col]))

    p = figure(title=col + ":" + title,
               plot_height=300, plot_width=800, tools="", toolbar_location=None,
               x_axis_type="datetime", x_axis_location="above",
               background_fill_color="#efefef", x_range=(dates[0], dates[df[col].shape[0] - 1]))

    p.line('date', 'close', source=source)
    p.yaxis.axis_label = 'Celcius'

    select = figure(title="Drag the middle and edges of the selection box to change the range above",
                    plot_height=130, plot_width=800, y_range=p.y_range,
                    x_axis_type="datetime", y_axis_type=None,
                    tools="", toolbar_location=None, background_fill_color="#efefef")

    range_tool = RangeTool(x_range=p.x_range)
    range_tool.overlay.fill_color = "navy"
    range_tool.overlay.fill_alpha = 0.2

    select.line('date', 'close', source=source)
    select.ygrid.grid_line_color = None
    select.add_tools(range_tool)
    select.toolbar.active_multi = range_tool

    return column(p, select)


def plotly_dwd(df):

    title = 'Official Outdoor Observations Braunschweig (City Center) Germany'
    trace_temp = go.Scatter(x=list(df.index),
                            y=list(df.Temp),
                            name='Temperature',
                            line=dict(color='#3FA65F'))

    # set the initial graph
    data = [trace_temp]

    # when drop down changes:  get new values for y then update the graph
    updatemenus = list([
        dict(
            buttons=list([
                dict(label='Temperature',
                     method='update',
                     args=[{'y': [df.Temp]},
                           {'title': 'Temperature ' + title}]),

                dict(label='Humidity',
                     method='update',
                     args=[{'y': [df.Humi]},
                           {'title': 'Humidity ' + title}])
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0.3,
            xanchor='left',
            y=1.2,
            yanchor='top'
        )
    ])

    # Place widgets on screen
    layout = dict(updatemenus=updatemenus,
                  title=title,
                  xaxis=dict(
                      rangeselector=dict(
                          buttons=list([
                              dict(count=1,
                                   label='1m',
                                   step='month',
                                   stepmode='backward'),
                              dict(count=6,
                                   label='6m',
                                   step='month',
                                   stepmode='backward'),
                              dict(count=1,
                                   label='YTD',
                                   step='year',
                                   stepmode='todate'),
                              dict(count=1,
                                   label='1y',
                                   step='year',
                                   stepmode='backward'),
                              dict(step='all')
                          ])
                      ),
                      rangeslider=dict(
                          visible=True
                      ),
                      type='date'
                  )
                  )

    fig = dict(data=data, layout=layout)
    return fig


def plotly_home(df):

    title = 'Residencial Observations in Braunschweig, Germany'
    trace_temp = go.Scatter(x=list(df.index),
                            y=list(df.Temp1),
                            name='Temperature1',
                            line=dict(color='#3FA65F'))

    # set the initial graph
    data = [trace_temp]

    # when drop down changes:  get new values for y then update the graph
    updatemenus = list([
        dict(
            buttons=list([
                dict(label='Temperature 1',
                     method='update',
                     args=[{'y': [df.Temp1]},
                           {'title': 'Temperature 1 ' + title}]),

                dict(label='Humidity 1',
                     method='update',
                     args=[{'y': [df.Humi1]},
                           {'title': 'Humidity 1 ' + title}]),

                dict(label='Temperature 2',
                     method='update',
                     args=[{'y': [df.Temp2]},
                           {'title': 'Temperature 2 ' + title}]),

                dict(label='Humidity 2',
                     method='update',
                     args=[{'y': [df.Humi2]},
                           {'title': 'Humidity 2 ' + title}]),

                dict(label='Temperature 3',
                     method='update',
                     args=[{'y': [df.Temp3]},
                           {'title': 'Temperature 3 ' + title}]),

                dict(label='Humidity 3',
                     method='update',
                     args=[{'y': [df.Humi3]},
                           {'title': 'Humidity 3 ' + title}]),

                dict(label='Temperature 4',
                     method='update',
                     args=[{'y': [df.Temp4]},
                           {'title': 'Temperature 4 ' + title}]),

                dict(label='Humidity 4',
                     method='update',
                     args=[{'y': [df.Humi4]},
                           {'title': 'Humidity 4 ' + title}])
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0.3,
            xanchor='left',
            y=1.2,
            yanchor='top'
        )
    ])

    # Place widgets on screen
    layout = dict(updatemenus=updatemenus,
                  title=title,
                  xaxis=dict(
                      rangeselector=dict(
                          buttons=list([
                              dict(count=1,
                                   label='1m',
                                   step='month',
                                   stepmode='backward'),
                              dict(count=6,
                                   label='6m',
                                   step='month',
                                   stepmode='backward'),
                              dict(count=1,
                                   label='YTD',
                                   step='year',
                                   stepmode='todate'),
                              dict(count=1,
                                   label='1y',
                                   step='year',
                                   stepmode='backward'),
                              dict(step='all')
                          ])
                      ),
                      rangeslider=dict(
                          visible=True
                      ),
                      type='date'
                  )
                  )

    fig = dict(data=data, layout=layout)
    return fig