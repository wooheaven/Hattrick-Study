#!/bin/bash

head -n -1 d.txt > tmpFile.txt
tail -n +2 tmpFile.txt > d.txt
rm -rf tmpFile.txt

awk 'BEGIN{FS=OFS="["} {if ( NF == 10 ) printf "%s", $0; else if ( NF == 73 ) print substr($0,38); else print $0}' d.txt > tmpFile.txt
mv tmpFile.txt d.txt

sed -i 's/\[td\]//g' d.txt
sed -i 's/\[th\]//g' d.txt

sed -i 's/\[\/td\]/,/g' d.txt
sed -i 's/\[\/th\]/,/g' d.txt

sed -i 's/\[tr\]//g' d.txt
sed -i 's/\[\/tr\]//g' d.txt

awk 'BEGIN{FS=OFS=","} {if ( length($14) > 1 && $14 != "MB" ) $14="True"; print }' d.txt > tmpFile.txt
mv tmpFile.txt d.txt

sed -i 's/#/Number/' d.txt
