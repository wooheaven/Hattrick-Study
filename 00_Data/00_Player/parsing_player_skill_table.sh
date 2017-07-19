#!/bin/bash

unset targetFile
unset tmpFile
unset isReady

if [[ -e $1 ]]; 
then 
echo "Ready to parsing player_skill_table.txt";

targetFile="$1/player_skill_table.txt"
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
    
awk 'BEGIN{FS=OFS=","} {if ( NF == 5 ) printf "%s", $0; else if ( NF == 33 ) print ","$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19,$20,$21,$22,$23,$24,$25,$26,$27,$28,$29,$30,$31,$32,$33 ; else print $0 }' $targetFile > $tmpFile
mv -f $tmpFile $targetFile
   
awk 'BEGIN{FS=OFS=","} {if ( NF > 35 ) print $2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19,$20,$21,$22,$23,$24,$25,$26,$27,$28,$29,$30,$31,$32,$33,$34,$35,$36 ; else }' $targetFile > $tmpFile
mv -f $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( length($14) == 3 ) $14="TRUE"; print }' $targetFile > $tmpFile
mv -f $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( length($14) == 0 ) $14="FALSE"; print }' $targetFile > $tmpFile
mv -f $tmpFile $targetFile

sed -i '1s/Player/Player,PlayerID/' $targetFile
awk 'BEGIN{FS=OFS=","} {if ( length($3) > 7 && $3 != "Player" ) $3=substr($3,1,index($3," [")-1)","substr($29,11,9); print }' $targetFile > $tmpFile
mv -f $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( $8 != "Since") sub(" 주  ", "주", $8) ; print }' $targetFile > $tmpFile
mv -f $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if ( $8 != "Since") sub(" 일", "일", $8) ; print }' $targetFile > $tmpFile
mv -f $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( $24 != "Last" && length($24) > 10 ) $24=substr($24, 1, 10) ; print}' $targetFile > $tmpFile
mv -f $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( $29 != "TC") $29="" ; print }' $targetFile > $tmpFile
mv -f $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( $30 != "PH") $30="" ; print }' $targetFile > $tmpFile
mv -f $tmpFile $targetFile

#sed -i 's/,/\t/g' $targetFile

fi

cat $targetFile

unset targetFile
unset tmpFile
unset isReady
