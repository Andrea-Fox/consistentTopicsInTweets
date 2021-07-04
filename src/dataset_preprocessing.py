
import pandas as pd 

# we open the corrected dataset
full_data = pd.read_csv('covid19_tweets_without_errors.txt', sep=",")

# we only choose those columns which contain the tweet's date, its text and the hashtags 
interesting_index = [8, 9, 10]
data = full_data.iloc[:, interesting_index]
data = data.iloc[1:100, ]
print(data.head)

print(data['text'])

# our goal is to extract, for each tweet, the date and its words
# in particular, each tweet will be characterized by three elements: date, set of words (hashtag included), set of hashtags

print(data['text'])
print(data.shape)

# we now create, for each tweet, the set of the words contained in it

words = data['text']
print(data.shape[0])
i=0
for new_string in data['text']:
    set_of_words = list(new_string.split(' '))
    length_list = len(set_of_words) 
    # we eliminate tags, links to external websotes e and those words which are truncated at the end
    for word in set_of_words:
        # print(i, " ", word)
        if "@" in word:
            # print("eliminated word which contains  @")
            set_of_words.remove(word)
        elif "https:" in word:
            # print("external link eliminated")
            set_of_words.remove(word)
        elif "…" in word:
            # print("truncated word eliminated")
            set_of_words.remove(word)
    #print(set_of_words)
    data.iloc[i, 1] = set_of_words
    i+=1
    # print(set_of_words)

print(data['text'])

print(data.head)

# stampa del dataset finale in un nuovo file
final_dataset = open("final_dataset_covid19_tweets.csv", "wt") 
data.to_csv(final_dataset, index = False, header = True)

