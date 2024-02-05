#!/bin/sh

YR=2016
DAY=$1

if [ -z "$DAY" ]; then
    DAY=$(date +%e | tr -d " ")
fi

if [ -r .aocsession ]; then
    AOC_SESSION=$(cat .aocsession)
fi

if [ -z "$AOC_SESSION" ]; then
    echo "no session found"
    exit 1
fi

D2=$(printf "%02d" $DAY)

echo "getting puzzle input for day $D2 for year $YR"

(
UA="https://github.com/eduellery/aoc-2016"
curl -s https://adventofcode.com/$YR/day/$DAY/input --cookie "session=$AOC_SESSION" -H "User-Agent: $UA"
) | awk 'NR>1{print PREV} {PREV=$0} END{printf("%s",$0)}' > test/day$D2.in
