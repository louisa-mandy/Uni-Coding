#create a program where it can count the amounth of letters
# of every sentences / words there is ( including spaces )

# how many sentences per 100 words = deviding words by 100 
# deviding sentences by words times 100 

# the longer the sentences are, the greater the grade will be 

def letter_counter (text) :
    return sum(1 for char in text if char.isalpha())

def count_words(text) : 
    words = text.split()
    return len(words)

def sentence_counter(text)  : 
    sentence_delimiters = [ '.', '?', '!']
    sentence_count = 0 
    for char in text:
        if char in sentence_delimiters:
            sentence_count += 1 
    return sentence_count


def coleman_liau_index(letters, words, sentences) : 
    L = (letters / words ) * 100 
    S = (sentences / words) * 100 
    index = 0.0588 * L - 0.296 * S - 15.8 
    return round (index)

def main():
    text = input("input a text here: ... ")
    letters = letter_counter(text)
    words = count_words(text)
    sentences = sentence_counter(text)
    index = coleman_liau_index(letters, words, sentences)

    if index < 1: 
        print ("before grade 1")
    elif index >= 16: 
        print("grade 16+")
    else:
        print(f" grade {index}")

if __name__ == "__main__": # to call the main function 
    main()


