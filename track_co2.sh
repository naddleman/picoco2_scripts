#!/bin/bash

if [ -z "$1" ]
    then
        echo "Usage: ./track_co2.sh outfile"
	exit 1
fi

if [ ! -f "$1" ]; then
    echo "Creating log file $1"
    echo Time,CO2 PPM,Temperature,Relative humidity > $1
fi

timeout 1m usbtenkiget -i a -L $1 -I 10000
