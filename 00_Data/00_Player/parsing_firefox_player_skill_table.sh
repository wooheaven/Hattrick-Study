#!/bin/bash

head -n -1 $1/firefox_player_skill_table.txt > $1/tmpFile.txt
tail -n +2 $1/tmpFile.txt > $1/firefox_player_skill_table.txt

sed -i 's/\[td\]//g' $1/firefox_player_skill_table.txt
sed -i 's/\[th\]//g' $1/firefox_player_skill_table.txt

sed -i 's/\[\/td\]/,/g' $1/firefox_player_skill_table.txt
sed -i 's/\[\/th\]/,/g' $1/firefox_player_skill_table.txt

sed -i 's/\[tr\]//g' $1/firefox_player_skill_table.txt
sed -i 's/\[\/tr\]//g' $1/firefox_player_skill_table.txt

sed -i 's/#/Number/' $1/firefox_player_skill_table.txt

awk 'BEGIN{FS=OFS=","} {if ( NF == 5 ) printf "%s", $0; else if ( NF == 35 ) print substr($0,38); else print $0}' $1/firefox_player_skill_table.txt > $1/tmpFile.txt
mv $1/tmpFile.txt $1/firefox_player_skill_table.txt

awk 'BEGIN{FS=OFS=","} {print $2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19,$20,$21,$22,$23,$24,$25,$26,$27,$28,$29,$300,$30,$31,$32,$33,$34,$35,$36,$37,$38,$39}' $1/firefox_player_skill_table.txt > $1/tmpFile.txt
mv $1/tmpFile.txt $1/firefox_player_skill_table.txt

#awk 'BEGIN{FS=OFS=","} {if ( length($14) > 1 && $14 != "MB" ) $14="True"; print }' $1/firefox_player_skill_table.txt > $1/tmpFile.txt
#mv $1/tmpFile.txt $1/firefox_player_skill_table.txt
