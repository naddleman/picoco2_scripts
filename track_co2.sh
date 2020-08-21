#!/bin/bash

if [ -z "$1" ]
    then
        echo "Usage: ./append_co2_data.sh outfile"
	exit 1
fi

echo time, CO2 PPM, temperature, relative humidity > $1

runtime="1 day"
endtime=$(date -d "$runtime" +%s)

while [[ $(date -u +%s) -le $endtime ]]
do
    echo `date -I'seconds'`, `usbtenkiget -i a` >> $1
    sleep 600
done
