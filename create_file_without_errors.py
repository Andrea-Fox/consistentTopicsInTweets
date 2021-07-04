import pandas as pd 


# https://stackoverflow.com/questions/21842885/python-find-a-substring-in-a-string-and-returning-the-index-of-the-substring
def find_str(s, char):      # funzione che dice in che punto inzia una sottostringa all'interno di una stringa
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

# prima di aprire il csv finale, dobbiamo fare in modo di eliminare le righe vuote. Per fare ciò eliminiamo tutti i comandi di cambiare riga che non sono preceduti da True o False
f = open("C:\Users\Andrea\Dropbox\universita\data_mining\data_mining\covid19_tweets.txt")
new_text_file = open("C:\Users\Andrea\Dropbox\universita\data_mining\data_miningcovid19_tweets_without_errors_1.txt", "wt") 
riga_corretta = ""
prima_riga = True

for line in f:
    if prima_riga:      # la prima riga va sempre riscritta sul nuovo file
        prima_riga = False
        print(line)
        new_text_file.write(line)
    else:
        #print(line)
        indice_nuova_riga = find_str(line, "\n")
        caratteri_precedenti = line[(indice_nuova_riga-5):indice_nuova_riga] # questi devono contenere True o False, altrimenti non è stato mandato a capo nel punto giusto
        if ("True" not in caratteri_precedenti) & ("False" not in caratteri_precedenti):    # c'è un errore, che va corretto
            #print("ERRORE")  
            line = line[:-1]                # we eliminate '\n' from the line 
            riga_corretta = riga_corretta + line + " "
            #print(line)  
        else:       # la riga studiata non ha errori: può essere concatenata con le righe precedenti (se esistono) e poi essere stampata sul nuovo file
            # concatenazione
            line = riga_corretta + line
            # stampa della nuova riga corretta sul nuovo file
            #print(line)
            new_text_file.write(line)
            # cancellazione delle precedenti righe sbagliate
            riga_corretta = ""

new_text_file.close()    