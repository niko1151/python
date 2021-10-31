#!/usr/bin/env python3

def merge(L1, L2):
    list = []
    i, x = 0, 0
  
    while i < len(L1) and x < len(L2):
        if L1[i] < L2[x]:
            list.append(L1[i])
            i += 1
        else:
            list.append(L2[x])
            x += 1

    if i < len(L1):
        list = list + L1[i:]
    elif x < len(L2):
        list = list + L2[x:]
    
    return list

def main():
    L1 = sorted([1, 5, 8, 10, 50])
    L2 = sorted([3, 4, 29, 41, 45, 49])

    print(merge(L1,L2))

if __name__ == "__main__":
    main()
