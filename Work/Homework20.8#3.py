#---------------------------------------------
# Name: Chapter 20 Homework
# Purpose: Homework
#
# Author: TaylorJB
#
# Created: 3/1/2025
#---------------------------------------------
#3
def process_text():
    the_text=open("alice.txt", "r")
    text=the_text.read()
    the_text.close()

    text=text.lower()
    words=text.split() #Splitting words and making them lowercase

    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789“”‘’" 
    def cleaning_words(s): #Function to get rid of all punctuation
        s_sans_punct = ""
        for letter in s:
            if letter not in punctuation:
                s_sans_punct += letter
        return s_sans_punct

    word_counts = {}
    for word in words:
        clean_words=cleaning_words(word)
        if clean_words != "":
            word_counts[clean_words] = word_counts.get(clean_words, 0) + 1
        

    count_items=list(word_counts.items())
    count_items.sort()
                          
    with open("alice_words.txt","w") as f:
        f.write("{}           {}\n".format("Word","Count"))
        f.write("====================\n")
        for (word, count) in count_items:
            f.write(f"{word:<15} {count}\n")

process_text()