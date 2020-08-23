#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from pytz import timezone
import sys

TIMEZONE = 'US/Pacific'
TITLE = 'Air quality: Temperature (C), Relative Humidity, CO2 (PPM)'

def parseargs(args):
    if len(args) != 3:
        sys.exit('Usage: python graph.py infile.csv outfile.png')
    infile, outfile = args[1:]
    return infile, outfile

def parse_csv(csv):
    df = pd.read_csv(csv, header=0)
    df['dtnum'] = mdates.date2num(df['Time'])
    return df

def produce_plots(df, title):
    fig, axs = plt.subplots(3, 1, sharex=True)
    for i, col in enumerate(df.columns[1:4], -1):
        axs[i].plot_date(df['dtnum'], df[col], xdate=True, tz=TIMEZONE, fmt='-')
        axs[i].set_ylabel(col)
    fig.suptitle(title)
    fig.autofmt_xdate()
    fig.set_size_inches(10, 8)
    myFmt = mdates.DateFormatter('%H:%M')
    myFmt.set_tzinfo(timezone(TIMEZONE))
    axs[2].xaxis.set_major_formatter(myFmt)
    return fig, axs

def main(argv):
    infile, outfile = parseargs(argv)
    df = parse_csv(infile)
    fig, axs = produce_plots(df, TITLE)
    plt.savefig(outfile, format='png')

if __name__ == '__main__':
    main(sys.argv)
