# PicoCO2 scripts

## track\_co2.sh
track\_co2.sh writes co2 (PPM), temperature (C), and relative humidity with
timestamps to a csv file, recording every 10 minutes for 24 hours. 

Usage:
```bash
./track_co2.sh outfile.csv
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
