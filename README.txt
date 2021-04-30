This is the repo that hosts out team's work. These are the main files that
record our work.
1. get_tweet.py : use the Twitter API credentials to pull tweets, pull tweets
   according to hashtags and word seawrch. limit to 1500 tweets per hashtag and
wordsearch. outpu are .csv files named accordingly. This we look up the method
online, substituting the words and hastags we want and credentials.

2. merge.py: merge the .csv of the same subject(ex:climate, election, stimulus
   check) into 3 big .csv files. This we look up how to online.

3. Stimulus-Analysis.ipynb and Stimulus-Analysis-2.ipynb: 
  -read from the stimulus_raw.csv file
  - preprocess data (drop unused columns, drop
duplicates, remove punctuation, hastag, mention, tokenize data) and save that
into a column called Processed
  -explore the data : length of tweets, number of words in a tweet,location the
tweets were posted from (country or usa states).
  -Vectorize data: use Tf-idf. Choose between 100 and 130 word to create a list
of most popularly repeated to create stop words. Then fit and tranformed the
Processed data.
  - Out of Curiosity, we explore the locations and volumns of tweets by the
    hour from the collected data. outputs are demonstated by graphs. We can see
the most polular tweets (according to retweets and favorite). we can see the
most popular words as well.
  - Sentiment Analysis : calculate polarity and subjectivity with textBlob.
    Polarity is between -1 and 1. Subjectivity is between 0 and 1. 
  -Build a machine learning model: use BAyes Classifier. we used tf-idf vectors
created above as feature and labels as target. We evaluate the model's accuracy
with classification report.
4 Climate-Analysis.ipynb and Climate-Analysis-2.ipynb
5.Election-Analysis.ipynb and Election-Analysis-2.ipynb
(Both follow the abpve structure, we'll save the detail analysis for the paper)

For the Analysis, the majority of codes are here and there. We know what we
want to do and look up online, like exploring data, cleaning data, and so on.
Zijun did most of the data preprocessing, Linh did Vectorization build machine
leanring model, Likhitha did data exploratory and visualization.
