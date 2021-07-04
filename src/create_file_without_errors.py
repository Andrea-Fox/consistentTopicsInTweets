import pandas as pd 


# https://stackoverflow.com/questions/21842885/python-find-a-substring-in-a-string-and-returning-the-index-of-the-substring
def find_str(s, char):      # this function tells us the starting index of the substring we're interested in
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1
# before opening the final csv file, we need to make sure that the empty lines are eliminated
f = open("covid19_tweets.txt")
new_text_file = open("covid19_tweets_without_errors.txt", "wt") 
correct_line = ""
first_line = True

for line in f:
    if first_line:      # the first line always has to be writtne on the new file as well
        first_line = False
        print(line)
        new_text_file.write(line)
    else:
        #print(line)
        index_new_line = find_str(line, "\n")

        # the following have to contain either True or False, otherwise the new line hasn't been started in the correct place
        caratteri_precedenti = line[(index_new_line-5):index_new_line] 
        if ("True" not in caratteri_precedenti) & ("False" not in caratteri_precedenti):    # an error has been found, hence has to be corrected
            #print("ERROR")  
            line = line[:-1]                # we eliminate '\n' from the line 
            correct_line = correct_line + line + " "
            #print(line)  
        else: 
            # the line considered has no errors: it can be concatenated with the prevois correct lines and then has to printed on the new file   
            
            # concatenation
            line = correct_line + line

            # print on the new file
            new_text_file.write(line)

            # deletion of previous incorrect lines 

new_text_file.close()    