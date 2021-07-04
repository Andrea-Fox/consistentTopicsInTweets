import pandas as pd 
from pathlib import Path

from datetime import datetime
from efficient_apriori import apriori

# parameters to define
frequency_threshold = 0.005
days_frequent_threshold = 10
period_consistent_threshold = 5
consider_hashtags = False



# upload the preprocessed data
path = Path('compute_consistent_itemsets.py').parent
full_data_path = (path / "../data/preprocessed_dataset.csv").resolve()
full_data = pd.read_csv(full_data_path)

number_of_tweets = full_data.shape[0]
for i in range(full_data.shape[0]):
    try:
        full_data.iloc[i, 1] = full_data.iloc[i, 1].split(" ")
    except:
        full_data.iloc[i, 1] = [""]
    # we add, if necessary, also the hashtags to the sets of words to study
    if (consider_hashtags):
        try:
            full_data.iloc[i, 1] = full_data.iloc[i, 1] + full_data.iloc[i, 2].split(" ")
        except:
            continue

# we eliminate the second columns, as the hashtags, if needed, have been added to the first columns
interesting_data = full_data.iloc[:, :2]

first_day = interesting_data.iloc[0, 0]
last_day = interesting_data.iloc[-1, 0]
days_to_consider = 26

# creation of 26 different baskets, one for each day
i = 0
iFinale = 0
list_of_basket = []
for days in range(days_to_consider):
    
    daily_basket = []
    i = iFinale
    considered_day = interesting_data.iloc[iFinale, 0][:10]
    while((i+1 < number_of_tweets) and (considered_day) == (interesting_data.iloc[i+1, 0][:10])):
        i += 1
        daily_basket.append(interesting_data.iloc[i, 1])
    iFinale = i+1
    list_of_basket.append([tuple(row) for row in daily_basket])

# initalization of the sets which will contain the sets of frequent itemsets of each period
frequent_itemsets_period_1 = set()
frequent_itemsets_period_2 = set()
frequent_itemsets_period_3 = set()
frequent_itemsets_period_4 = set()
frequent_itemsets_period_5 = set()
frequent_itemsets_period_6 = set()
frequent_itemsets_period_7 = set()
days_in_period_1 = range(0, 4)
days_in_period_2 = range(4, 8)
days_in_period_3 = range(8, 12)
days_in_period_4 = range(12, 16)
days_in_period_5 = range(16, 20)
days_in_period_6 = range(20, 24)
days_in_period_7 = range(24, 26)

# at this point we have, for each day, the list of tuples of terms which appear in the tweets. Now we can apply the function apriori to obtain the frequent itemsets
list_of_frequent_itemsets = []
for i in range(days_to_consider):
    output_frequent_itemsets, rules = apriori(list_of_basket[i], min_support=frequency_threshold)
    frequent_itemsets_current_day = set()

    # we can try to eliminate all those useless data, such as the frequent itemsets of size 1 and the occurrences of each set
    for key in output_frequent_itemsets.keys():
            if (key > 1):       # we are not interested in frequent words: we only care about frequent itemsets
                frequent_itemsets_current_day = frequent_itemsets_current_day.union(set(output_frequent_itemsets.get(key).keys()))
    list_of_frequent_itemsets.append(frequent_itemsets_current_day)
    if i in days_in_period_1:
        frequent_itemsets_period_1 = frequent_itemsets_period_1.union(frequent_itemsets_current_day)
    elif i in days_in_period_2:
        frequent_itemsets_period_2 = frequent_itemsets_period_2.union(frequent_itemsets_current_day)
    elif i in days_in_period_3:
        frequent_itemsets_period_3 = frequent_itemsets_period_3.union(frequent_itemsets_current_day)
    elif i in days_in_period_4:
        frequent_itemsets_period_4 = frequent_itemsets_period_4.union(frequent_itemsets_current_day)
    elif i in days_in_period_5:
        frequent_itemsets_period_5 = frequent_itemsets_period_5.union(frequent_itemsets_current_day)
    elif i in days_in_period_6:
        frequent_itemsets_period_6 = frequent_itemsets_period_6.union(frequent_itemsets_current_day)
    elif i in days_in_period_7:
        frequent_itemsets_period_7 = frequent_itemsets_period_7.union(frequent_itemsets_current_day)

# we now create a dictionary which has, as key, a frequent itemset and as value the number of occurrences
frequent_itemsets_dict = {}
for i in range(days_to_consider):
    for frequent_itemset in list_of_frequent_itemsets[i]:
        if frequent_itemset not in frequent_itemsets_dict.keys():
            # we have to create a new element that appears (for now) only once
            frequent_itemsets_dict.update({frequent_itemset: 1}) 
        else:
            # we have to increase the count of the corresponding value
            frequent_itemsets_dict[frequent_itemset] = frequent_itemsets_dict[frequent_itemset] + 1

# we keep only those itemsets which appear at least days_frequent_threshold times
candidate_consistent_itemsets = [item for item in frequent_itemsets_dict if frequent_itemsets_dict[item] >= days_frequent_threshold]

# now we need to find all those elements contained in candidate_consistent_itemsets which appear in at least period_consistent_threshold periods
consistent_itemsets = []


for element in candidate_consistent_itemsets:
    counter = 0
    if element in frequent_itemsets_period_1:
        counter += 1
    if element in frequent_itemsets_period_2:
        counter += 1
    if element in frequent_itemsets_period_3:
        counter += 1
    if element in frequent_itemsets_period_4:
        counter += 1
    if element in frequent_itemsets_period_5:
        counter += 1
    if element in frequent_itemsets_period_6:
        counter += 1
    if element in frequent_itemsets_period_7:
        counter += 1
    if (counter >= period_consistent_threshold): 
        consistent_itemsets.append(element)

# we print on a file the frequent itemsets
path_string = '../bin/' + str(frequency_threshold)[2:] + '_' + str(days_frequent_threshold) + '_' + str(period_consistent_threshold) + '.txt'
output_file_path = (path / path_string).resolve()
with open(output_file_path, 'w') as f:
    for item in consistent_itemsets:
        f.write("%s \n" %str(item))
