# PicoCO2 scripts

## track\_co2.sh
track\_co2.sh writes co2 (PPM), temperature (C), and relative humidity with
timestamps to a csv file, recording every 10 minutes for 24 hours. 

Usage:
```bash
./track_co2.sh -L <outfile.csv> -I <interval (seconds)> -d <duration>

## Example, record every 10 seconds for 1 hour:

./track_co2.sh -L out.csv -I 10 -d 1h

## duration is a floating point number with suffix 's' 'm' 'h' or 'd' for 
## seconds, minutes, hours, and days, respectively. Defaults to 's'.
## Passing '0' enables indefinite logging.
```

Requires usbtenkiget software from the
[Dracal website](https://www.dracal.com/store/support/downloads/index.php)

## graph.py
graph.py graphs the data recorded with track\_co2.sh.

Usage:
```bash
python graph.py infile.csv outfile.png
```

Requires: Python >= 3.8, matplotlib, pandas >= 1.1.0, pytz.
