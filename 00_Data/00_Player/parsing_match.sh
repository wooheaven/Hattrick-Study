#!/bin/bash

unset targetFile
unset tmpFile
unset isReady

if [[ -e $1 ]];
then 
echo "Ready to parsing match.txt";

targetFile="$1/match.txt"
tmpFile="$1/tmpFile.txt"
isReady="true"

else 
echo "Not ready to parsing match.txt";
fi

if [[ $isReady -eq "true" ]];
then

sed -i 's/,{/\n{/g' $targetFile
awk 'BEGIN{FS=OFS=","} {print $2,$1,$4,$10,$11}' $targetFile > $tmpFile
mv $tmpFile $targetFile

# Change PlayerID to Number
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619233" ) print "{"$1,"1",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "428709461" ) print "{"$1,"2",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619235" ) print "{"$1,"3",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619236" ) print "{"$1,"4",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619237" ) print "{"$1,"5",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619238" ) print "{"$1,"6",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619239" ) print "{"$1,"7",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619240" ) print "{"$1,"8",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619241" ) print "{"$1,"9",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619242" ) print "{"$1,"10",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619243" ) print "{"$1,"11",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619244" ) print "{"$1,"12",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619245" ) print "{"$1,"13",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619246" ) print "{"$1,"14",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619247" ) print "{"$1,"15",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619248" ) print "{"$1,"16",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619249" ) print "{"$1,"17",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619250" ) print "{"$1,"18",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "428801949" ) print "{"$1,"19",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427827635" ) print "{"$1,"20",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "428112207" ) print "{"$1,"21",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "428060480" ) print "{"$1,"22",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "428125893" ) print "{"$1,"23",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "425173438" ) print "{"$1,"24",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "406205227" ) print "{"$1,"25",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "425734621" ) print "{"$1,"26",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "428157949" ) print "{"$1,"27",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile
awk 'BEGIN{FS=OFS=","} {if( substr($2,13) == "427619232" ) print "{"$1,"99",$3,$4,$5; else print $0}' $targetFile > $tmpFile
mv $tmpFile $targetFile

# PositionID to Pos
sed -i 's/}//' $targetFile

awk -v oldPos="0" -v oldFromMin="-1" 'BEGIN{FS=OFS=","} {if( substr($1,15) == "-1" && substr($5,9) == oldFromMin ) print oldPos,$2,$3,$4,$5; else print substr($1,15),$2,$3,$4,$5; oldPos=substr($1,15); oldFromMin=substr($4,11)}' $targetFile >> $tmpFile
mv $tmpFile $targetFile

awk -v oldPos="0" -v oldToMin="-1" 'BEGIN{FS=OFS=","} {if( $1 == "-1" && substr($4,11) == oldToMin ) print oldPos,$2,$3,$4,$5; else print $1,$2,$3,$4,$5; oldPos=$1; oldToMin=substr($5,9)}' $targetFile >> $tmpFile
mv $tmpFile $targetFile

tac $targetFile > $tmpFile
mv $tmpFile $targetFile

awk -v oldPos="0" -v oldToMin="-1" 'BEGIN{FS=OFS=","} {if( $1 == "-1" && substr($4,11) == oldToMin ) print oldPos,$2,$3,$4,$5; else print $1,$2,$3,$4,$5; oldPos=$1; oldToMin=substr($5,9)}' $targetFile >> $tmpFile
mv $tmpFile $targetFile

tac $targetFile > $tmpFile
mv $tmpFile $targetFile

sort -t, -k1n,1 -k4,4 $targetFile > $tmpFile
mv $tmpFile $targetFile

echo "PO,Number,Star,FromMin,ToMin" >> $tmpFile
echo "" >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "0" ) print "CO",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
echo "" >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "100" ) print "KP",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
echo "" >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "101" ) print "WB",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "105" ) print "WB",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
echo "" >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "102" ) print "CD",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "104" ) print "CD",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
echo "" >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "106" ) print "W",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "110" ) print "W",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
echo "" >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "107" ) print "IM",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "109" ) print "IM",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
echo "" >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "111" ) print "FW",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
awk 'BEGIN{FS=OFS=","} {if( $1 == "113" ) print "FW",$2,$3,$4,$5; else}' $targetFile >> $tmpFile
mv $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( length($3) >= 9 ) $3=substr($3,9); print}' $targetFile > $tmpFile
mv $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( length($4) >= 11 ) $4=substr($4,11); print}' $targetFile > $tmpFile
mv $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( length($5) >= 9 ) $5=substr($5,9); print}' $targetFile > $tmpFile
mv $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( $4 == "-1" ) $4="0"; print}' $targetFile > $tmpFile
mv $tmpFile $targetFile

awk 'BEGIN{FS=OFS=","} {if ( $5 == "-1" ) $5="0"; print}' $targetFile > $tmpFile
mv $tmpFile $targetFile

echo ""
cat $targetFile

fi

unset targetFile
unset tmpFile
unset isReady