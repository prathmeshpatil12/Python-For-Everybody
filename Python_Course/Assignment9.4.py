name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
word_dict = dict()
lst = list()
for line in handle:
    line.rstrip()
    if(line.startswith("From ")):
        #print(line)
        words = line.split()
        lst.append(words[1])
        #print(lst)
for word in lst:
    word_dict[word] = word_dict.get(word, 0) + 1

max_count=0
for word in word_dict:
    if(word_dict[word]>max_count):
        max_count=word_dict[word]
        max_word=word

print(max_word,max_count)