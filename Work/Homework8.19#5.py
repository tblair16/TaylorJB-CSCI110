#---------------------------------------------
# Name: Chapter 8 Homework
# Purpose: Homework
#
# Author: TaylorJB
#
# Created: 2/12/2025
#---------------------------------------------
#Number 5
fav_song = """No words appear before me in the aftermath
Salt streams out my eyes and into my ears
Every single thing I touch becomes sick with sadness
'Cause it's all over now, all out to sea
Goodbye, goodbye, goodbye
You were bigger than the whole sky
You were more than just a short time
And I've got a lot to pine about
I've got a lot to live without
I'm never gonna meet
What could've been, would've been
What should've been you
What could've been, would've been you
Did some bird flap its wings over in Asia?
Did some force take you because I didn't pray?
Every single thing to come has turned into ashes
'Cause it's all over, it's not meant to be
So I'll say words I don't believe
Goodbye, goodbye, goodbye
You were bigger than the whole sky
You were more than just a short time
And I've got a lot to pine about
I've got a lot to live without
I'm never gonna meet
What could've been, would've been
What should've been you
What could've been, would've been
What should've been you
(What could've been, would've been)
What could've been, would've been you
(Could've been, would've been)
(Could've been, would've been)
Goodbye, goodbye, goodbye
You were bigger than the whole sky
You were more than just a short time
And I've got a lot to pine about
I've got a lot to live without
I'm never gonna meet
What could've been, would've been
What should've been you"""

wds = fav_song.split() #Splitting string into words 

def count_e(fav_song): #Function for counting all the e's
    count=0
    for c in wds:
        if "e" in c:
            count+=1
    return(count)

wordcount=len(wds)
ecount=count_e(fav_song)
percent= (ecount/wordcount)*100

print("Your text contains {} words of which {} ({}%) contain the letter 'e'" .format(wordcount, ecount, percent))