s=input('Please enter a sort number (separated by space):')
slist=s.split(" ")  #Python split () slice the specified string by the specified delimiter
slist=[int(slist[i]) for i in range(len(slist))]

for i in range(0, len(slist)-1):
    index = i
    for j in range(i+1, len(slist)):
        if slist[index] >slist[j]:
            index = j
    slist[i], slist[index] = slist[index], slist[i]


for m in range(0,len(slist)):
    print(slist[m])
