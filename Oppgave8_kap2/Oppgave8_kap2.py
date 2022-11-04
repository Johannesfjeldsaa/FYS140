__author__ = 'Johannes Fjeldså'
__email__ = 'johannes.larsen.fjeldsa@nmbu.no'

import datetime

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib import patheffects
import pandas as pd

def read_and_preprocess(filepath):
    df = pd.read_csv(filepath, sep=';', decimal='.')
    df = df.rename(columns=lambda x: x.strip())
    df['Time'] = df['Year'].astype(str) + '.' + df['Month'].astype(str)
    df['Time'] = pd.to_datetime(df['Time'], format='%Y.%m')
    return df

def make_selection(df, from_time, to_time):
    return df.loc[(df['Time'] >= from_time) & (df['Time'] < to_time)]

def plot_selection(df):
    fig, ax = plt.subplots(3, sharex=True, sharey=True, figsize=(5, 8))

    ax[0].plot(df['Time'], df['Ten-year  Anomaly'],
               color='silver', ls='dashed')
    ax[0].plot(df['Time'], df['Twenty-year Anomaly'],
               color='silver', ls='dashed')
    ax[0].plot(df['Time'], df['Five-year Anomaly'],
               color='gold', label='Snitt av 5 år')

    ax[1].plot(df['Time'], df['Twenty-year Anomaly'],
               color='silver', ls='dashed')
    ax[1].plot(df['Time'], df['Five-year Anomaly'],
               color='silver', ls='dashed')
    ax[1].plot(df['Time'], df['Ten-year  Anomaly'],
               color='darkorange', label='Snitt av 10 år')

    ax[2].plot(df['Time'], df['Five-year Anomaly'],
               color='silver', ls='dashed')
    ax[2].plot(df['Time'], df['Ten-year  Anomaly'],
               color='silver', ls='dashed')
    ax[2].plot(df['Time'], df['Twenty-year Anomaly'],
               color='red', label=' Snitt av 20 år')


    for subplot in [0, 1, 2]:
        ax[subplot].legend(loc='upper left', facecolor='ivory')  # Lager legend
        ax[subplot].xaxis.set_major_formatter(DateFormatter('%Y'))  # Setter x-aksen som tid
        ax[subplot].yaxis.set_major_locator(plt.MaxNLocator(6))  # Setter maksantall av ticks på y-aksen

    # Felles Title etc
    fig.text(0.5, 0.04, 'Årstall', ha='center', fontsize=12)
    fig.text(0.02, 0.5, r'Tempraturavvik $[\degree C]$', va='center', rotation='vertical', fontsize=12)
    fig.suptitle(f'1970 - 2022', fontsize=16)

    plt.show()


if __name__ == '__main__':

    filepath1 = 'Data/Ice Temp Inf from air.csv'


    data1 = read_and_preprocess(filepath1)


    data1 = make_selection(data1, from_time='1970-01-01 00:00:01', to_time='2022-07-01 00:00:00')


    plot_selection(data1)

