The code to execute in order to obtain the list of consistent itemsets for certain values of the parameters is compute_consistent_itemsets.py

In order to execute it, one has to open the terminal, get to the src folder and execute the following command:
python3 compute_consistent_itemsets.py

The 4 parameters (frequency_threshold, days_frequent_threshold, period_consistent_threshold and consider_hashtags) have to be specified in the first few lines of the code.

The output is a file which will contain the consistent itemsets: this file is going to be saved in the bin folder and the name is going to follow a certain pattern.
Given the values of the parameters (frequency_threshold, days_frequent_threshold, period_consistent_threshold) = (xxxx, yyyy, zzzz) ,  the name of the file is going to be xxxx_yyyy_zzzz.txt  In order to avoid problems, only the decimal part of frequency_threshold is going to be considered.
For example, if (frequency_threshold, days_frequent_threshold, period_consistent_threshold) = (0.005, 10, 5), the output file is going to be called '005_10_5.txt'.
The folder bin is then going to contain all the files for all possible triplets of parameters (except one file which has been obtained assuming consider_hasthags = True) obtained assuming consider_hasthtags = False.


The other files in the folder are:
- print_multiple_consisten_items.py, which prints all the output files (with the same pattern described above) for all possible couples (days_frequent_threshold, period_consistent_threshold), given the value of frequency_threshold. This last parameter has to be specified in the code. Moreover, this code also prints the number of consistent itemsets according to the baseline model

- dataset_preprocessing.py : this code takes as input the original dataset (covid19_tweets.txt), a list of stopwords (stop_words_english.txt) and computes the preprocessed dataset in the way explained in section 6 inside the report.

- baseline_method.py : method that computes the list of the frequent itemsets given by the baseline method described in the report. The only parameters are frequency_threshold, days_frequent_threshold and consider_hashtags, as there are no periods to consider. Its outputs are saved in the bin folder

