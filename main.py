# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename,"r") as file:
        words = file.read()
        return words
        print(read_file_content("story.txt"))

def count_words(str):
    # [assignment] Add your code here
    count = dict()
    txts = str.split()
    for txt in txts:
        if txt in count:
            count[txt] +=1
        else:
            count[txt] =1
    return count

#Output
text =read_file_content("story.txt")
lead="DICTIONARY TEXT SEEN BELOW :"
print(lead)
print(count_words(text)) 

#return {"as": 10, "would": 20}