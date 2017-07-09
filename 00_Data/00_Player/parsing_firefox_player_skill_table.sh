#!/bin/bash

unset targetFile
unset tmpFile
unset isReady

if [[ -e $1 ]]; 
then 
echo "Ready to parsing firefox_player_skill_table.txt";

targetFile="$1/firefox_player_skill_table.txt"
tmpFile="$1/tmpFile.txt"
isReady="true"

else 
echo "Not ready to parsing firefox_player_skill_table.txt";
fi

if [[ $isReady -eq "true" ]];
then
head -n -1 $targetFile > $tmpFile
tail -n +2 $tmpFile > $targetFile
    
sed -i 's/\[td\]//g' $targetFile
sed -i 's/\[th\]//g' $targetFile

sed -i 's/\[\/td\]/,/g' $targetFile
sed -i 's/\[\/th\]/,/g' $targetFile
    
sed -i 's/\[tr\]//g' $targetFile
sed -i 's/\[\/tr\]//g' $targetFile
    
sed -i 's/#/Number/' $targetFile
    
awk 'BEGIN{FS=OFS=","} {if ( NF == 5 ) printf "%s", $0; else if ( NF == 35 ) print substr($0,38); else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
    
awk 'BEGIN{FS=OFS=","} {print $2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19,$20,$21,$22,$23,$24,$25,$26,$27,$28,$29,$300,$30,$31,$32,$33,$34,$35,$36,$37,$38,$39}' $targetFile > $tmpFile
mv $tmpFile $targetFile
    
awk 'BEGIN{FS=OFS=","} {if ( length($14) > 1 && $14 != "MB" ) $14="True"; print }' $targetFile > $tmpFile
mv $tmpFile $targetFile
fi

cat $targetFile

unset targetFile
unset tmpFile
unset isReady
