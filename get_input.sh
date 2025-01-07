#!/bin/sh

YR=2016
DAY=$1

if [ -z "$DAY" ]; then
    DAY=$(date +%e | tr -d " ")
fi

if [ -n "$AOC_SESSION" ] && [ -z "$AOC_DEBUG"]; then
    echo "session is present"
elif [ -r .aocsession ]; then
    echo "getting value from .aocsession file"
    AOC_SESSION=$(cat .aocsession)
fi

if [ -z "$AOC_SESSION" ]; then
    echo "no session found"
    exit 0
fi

D2=$(printf "%02d" $DAY)

echo "getting puzzle input for year $YR day $D2"

(
UA="https://github.com/eduellery/aoc-2016"
curl -s https://adventofcode.com/$YR/day/$DAY/input --cookie "session=$AOC_SESSION" -H "User-Agent: $UA"
) | awk 'NR>1{print PREV} {PREV=$0} END{printf("%s",$0)}' > test/res/day$D2.in
