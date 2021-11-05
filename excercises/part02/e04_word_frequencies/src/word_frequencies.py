#!/usr/bin/env python3
import re

def word_frequencies(filename):
    word_frequency = {}
    with open(filename,'r') as f:
        for line in f:
                word = re.findall(r'(\S*)', line)
                word = [line.strip("""!"#$%&'()*,-./:;?@[]_""") for line in word]
                for line in word:
                    if line in word_frequency:
                        word_frequency[line] += 1
                    else:
                        word_frequency[line] = 1

    return word_frequency

    

def main():
    print(word_frequencies('src/alice.txt'))

if __name__ == "__main__":
    main()
