def bubble(list):
    for i in range(len(list)-1):
        for j in range(len(list) - 1 - i):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)

if __name__ == '__main__':
    s = input('Please enter a sort number (separated by space):')
    slist = s.split(" ") #Python split () slice the specified string by the specified delimiter
    slist = [int(slist[i]) for i in range(len(slist))]
    bubble(slist)

