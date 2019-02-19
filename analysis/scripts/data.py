import pandas as pd

htsensor_columns = ['timestamp', 'Start Symbol', 'Zustand', 'Zeitstempel', 'Temp1', 'Temp2', 'Temp3', 'Temp4', 'Temp5',
                    'Temp6', 'Temp7', 'Temp8', 'Humi1', 'Humi2', 'Humi3', 'Humi4', 'Humi5', 'Humi6', 'Humi7', 'Humi8',
                    'Temperatur Kombisensor', 'Humid Kombisensor', 'Windgeschwindigkeit', 'Niederschlag', 'Rain',
                    'Stop Symbol'
                    ]


def braunschweig(url):

    # read data from file: parse the date after reading, just as a sanity check
    df = pd.read_csv(url, sep=';', decimal=',', names=htsensor_columns)

    # select relevant columns
    df = df[['timestamp', 'Temp1', 'Temp2', 'Temp3', 'Temp4', 'Temp8', 'Humi1', 'Humi2', 'Humi3', 'Humi4']]

    # create time series by parsing timestamp, and insert it as new column
    df.insert(1, 'datetime',
                pd.to_datetime(df.timestamp, errors='coerce'))  # If ‘coerce’, then invalid parsing will be set as NaT

    # set the date as the index
    df.set_index('datetime', inplace=True)

    # remove the orginal time
    df.drop(columns='timestamp', inplace=True)

    return df


def deutsches_wetterdienst(url, start=2014, end=2017):

    df = pd.read_csv(url, sep=';')

    # parse date
    df.insert(2, 'datetime', pd.to_datetime(df['MESS_DATUM'], errors='coerce', format='%Y%m%d%H'))

    # create index
    df.set_index('datetime', inplace=True)

    # rename columns
    df.rename(columns={'TT_TU': 'Temp', 'RF_TU': 'Humi'}, inplace=True)

    # filter years
    span = (df.index.year >= start) & (df.index.year <= end)
    df = df.loc[span, ['Temp', 'Humi']]

    # drop erroneous data points
    dropidx = df[df.Humi < 0].index
    df.drop(dropidx, inplace=True)
    
    return df