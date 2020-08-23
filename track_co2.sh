#!/bin/bash

usage () { echo 'Usage: ./track_co2.sh -L <logfile> -I <interval (s)> -d <duration>' 1>&2; exit 1; }
while getopts "L:I:d:" opt; do
    case $opt in
        d)
          duration=$OPTARG
          ;;
        I)
          interval=$OPTARG
          ;;
        L)
          logfile=$OPTARG
	  ;;
        \?)
          echo "Invalid option: -$opt" >&2
          usage
          ;;
        :)
          usage
          ;;
    esac
done

if [ -z "$1" ] || [ -z "${logfile}" ] || [ -z "${duration}" ] || [ -z "${interval}" ]
    then
        usage
fi

echo "duration = $duration"
echo "interval = $interval"s
echo "logfile = $logfile"
ms=$((1000 * $interval))


if [ ! -f "$logfile" ]; then
    echo "Creating log file $logfile"
    echo Time,CO2 PPM,Temperature,Relative humidity > $logfile
fi

timeout $duration usbtenkiget -i a -L $logfile -I $ms
exit 0
