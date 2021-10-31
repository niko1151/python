#!/usr/bin/env python3

def reverse_dictionary(d):
    inverse = dict() 
    for key in d: 
        for item in d[key]:
            if item not in inverse: 
                inverse[item] = [key] 
            else: 
                inverse[item].append(key) 
    return inverse

def main():
        d={"move":["liikuttaa"], "hide":["piilottaa", "salata"], "six":["kuusi"], "fir":["kuusi"]}
        print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
