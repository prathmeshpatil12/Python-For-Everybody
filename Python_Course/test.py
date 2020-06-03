def isPresent(ls,new_w):
    for word in ls:
        if word is new_w:
            return True
        return False

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
temp_lst = []
for line in fh:
    line = line.rstrip()
    temp_lst=line.split()
    for word in temp_lst:
        if ls


