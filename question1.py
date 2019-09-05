# Write a function called count_words that receives a file name as parameter and performs the following actions
# (1) the function parses the file content and removes remove all commas and full stops 
# (2) the function removes the following words: "and", "the", "a", "an", "is", "are", "of"
# (3) after that, the function counts the number of times each word appeared in the file and returns a dictionary with words and counts i.e., key is the word and value is the count
# the returned dictionary should be sorted by key.
# hint: pay attention to empty lines while parsing

def count_words(filename):
    infile = open(filename, "r")
    dic = {}
    for line in infile.readlines():
        line = line.lower()
        line = line.replace(',', '')
        line = line.replace('.', '')
        line = line.replace(' and ', ' ')
        line = line.replace(' the ', ' ')
        line = line.replace(' a ', ' ')
        line = line.replace(' an ', ' ')
        line = line.replace(' is ', ' ')
        line = line.replace(' are ', ' ')
        line = line.replace(' of ', ' ')

        for word in line.split():
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    s = {}
    for k in sorted(dic.keys()):
        s[k] = dic[k]
    return s
        

print(count_words("data1.txt"))