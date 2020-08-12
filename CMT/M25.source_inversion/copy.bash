#!/bin/bash


readarray -t events < eventlist.500.M26_add.2

echo "events: ${#events[@]}"

srcdir="/mnt/sdd1/Research/source_inversion_II/source_inversion_stage2/earthquakes/global_cmt.1976-2017/merged#dur-16_mag5.5-7.2"
dstdir="quakeml.500.M26_add.2"

i=0
for event in ${events[@]}
do
  src="$srcdir/$event.xml"
  if [ ! -f $src ]; then
    echo "Missing: $src"
    exit
  fi

  i=$(( $i + 1 ))
  echo "[$i] event: $event | cp $src --> $dstdir"
  cp $src $dstdir
done
