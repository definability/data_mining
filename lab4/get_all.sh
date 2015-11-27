echo "Getting words for $1"
sh get_valuable_words.sh ../lab3/output/out1_03.csv $1 > words.py
echo "Getting bigrams for $1"
sh get_valuable_words.sh ../lab3/output/out2_03.csv $1 > bigrams.py
echo "Getting trigrams for $1"
sh get_valuable_words.sh ../lab3/output/out3_03.csv $1 > trigrams.py

