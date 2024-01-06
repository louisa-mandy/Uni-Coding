
def countWordOcurence(sentence):
    counts = {} # works the same as dict()
    words = sentence.split() # to split sentence in to words 

    for word in words:
        if word in counts:
            counts[word] += 1 # multiple same words + 1 
        else:
            counts[word] = 1 # only one word, then only 1 
    return counts

def countCharOccurence(sentence):
    counts = {} # for adding dictionary 

    for char in sentence:
            if char in counts:
                counts[char] += 1 # if a certain character has more than 1, then it will have an addition +1
            else:
                counts[char] = 1 # when a character has no repetition, only 1 time muncul
    return counts
 
myInput = input("enter a sentence")

# try to add .lower ??????

wordCount = countWordOcurence(myInput)
charCount = countCharOccurence(myInput)

print(wordCount)
print(charCount)
