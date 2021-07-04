# apriamo il dataset
import pandas as pd 

full_data = pd.read_csv('C:/Users/Andrea/Dropbox/universita/data_mining/data_mining/covid19_tweets_without_errors.txt', sep=",")
# print(full_data.shape)
# print(full_data.head)


# scegliamo solo le colonne relative alla data, il suo testo e gli hashtag contenuti, che sono le uniche cose che andremo a considerare d'ora in poi
interesting_index = [8, 9, 10]
data = full_data.iloc[:, interesting_index]
data = data.iloc[1:100, ]
print(data.head)

# notiamo come abbiamo già il set degli hashtag per ciascun tweet
print(data['text'])


# il nostro obiettivo deve essere estrarre, per ogni tweet, la data e le parole
# in particolare, ogni tweet sarà caratterizzato da tre oggetti: data, set delle parole (compresi gli hashtag), set degli hashtag

print(data['text'])
print(data.shape)
# cerchiamo ora di andare a creare per ogni tweet un set contenente le parole di quel tweet

# ha senso tenere solo quelle uniche? in quel caso ->  list(set(stringa.split(' ')))

parole = data['text']
print(data.shape[0])
i=0
for stringa in data['text']:
    #print("------------------------------------------------------------------------------------------------")
    # print(i)
    #print("data =", data.iloc[i, 0], "\t testo = ", data.iloc[i, 1], "\t hashtags = ", data.iloc[i, 2])
    # print("stringa =",  stringa)
    set_of_words = list(stringa.split(' '))
    # print(set_of_words)
    # print(len(set_of_words))
    length_list = len(set_of_words) 
    # togliamo i tag (ha senso farlo), i link e le parole che vengono troncate alla fine
    for word in set_of_words:
        # print(i, " ", word)
        if "@" in word:
            # print("parola eliminata (contiene @)")
            set_of_words.remove(word)
        elif "https:" in word:
            # print("parola eliminata (contiene link)")
            set_of_words.remove(word)
        elif "…" in word:
            # print("parola eliminata (contiene ...)")
            set_of_words.remove(word)
    #print(set_of_words)
    data.iloc[i, 1] = set_of_words
    i+=1
    # print(set_of_words)

print(data['text'])

print(data.head)

# stampa del dataset finale in un nuovo file
# final_dataset = open("/home/andrea/Desktop/data_mining/final_dataset_covid19_tweets.csv", "wt") 
# data.to_csv(final_dataset, index = False, header = True)

