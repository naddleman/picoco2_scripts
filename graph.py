import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from pytz import timezone
import sys

if len(sys.argv) != 3: 
    print('Usage: python graph.py infile.csv outfile.png')
    sys.exit(1)

infile, outfile = sys.argv[1:]

df = pd.read_csv(infile, header=0)
df['dt'] = mdates.date2num(df['time'])
fig, axs = plt.subplots(3, 1, sharex=True)
for i, col in enumerate(df.columns[1:4]):
    axs[i-1].plot_date(df['dt'], df[col], xdate=True, tz='US/Pacific', fmt='-')
    axs[i-1].set_ylabel(col)

fig.suptitle("Office atmosphere")
plt.gcf().autofmt_xdate()
plt.gcf().set_size_inches(10, 8)
myFmt = mdates.DateFormatter('%H:%M')
myFmt.set_tzinfo(timezone('US/Pacific'))
axs[2].xaxis.set_major_formatter(myFmt)
plt.savefig(outfile, format='png') 
