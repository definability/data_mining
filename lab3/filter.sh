>"$2"
for txt in "$1"/*
do
    echo -n $(basename ${txt%_www*}) >> $2
    cat $txt | ./filter.pl >> $2 
    echo "" >> $2
done

