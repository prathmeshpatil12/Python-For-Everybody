import re
fh = open('regex_sum_360068.txt')
sum=0
count=0
for line in fh:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    for i in x:
        i=int(i)
        count+=1
        sum = sum + i

print("There are",count,"values with sum=",sum)