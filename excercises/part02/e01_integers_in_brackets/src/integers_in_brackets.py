#!/usr/bin/env python3

import re

def integers_in_brackets(s):
    r= []
    patt = re.compile(r'\[\s*([+-]?\d+)\s*\]')
    for i in patt.findall(s):
        r.append(int(i))
    return r

def main():
    integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx")

if __name__ == "__main__":
    main()
