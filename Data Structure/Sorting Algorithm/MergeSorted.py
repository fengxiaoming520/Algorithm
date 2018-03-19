def MergeSorted(L):
    if len(L) <= 1:
        return L
    num = int(len(L) / 2)
    left = MergeSorted(L[: num])
    right = MergeSorted(L[num : ])
    return Merge(left, right)

def Merge(left, right):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    s = input('Please enter a sort number (separated by space):')
    slist = s.split(" ") #Python split () slice the specified string by the specified delimiter
    slist = [int(slist[i]) for i in range(len(slist))]
    print(MergeSorted(slist))
