#!/usr/bin/env python3

def detect_ranges(l):
    res = []
    L = sorted(l)   
    i = 0
    
    while i < len(L):                           # gentag lige så mange gange som der er tal i listen L
        if i+1 < len(L) and L[i]+1 == L[i+1]:   # hvis der stadig er flere i L (jeg piller ved i, længere nede)
                                                # ... og den værdi i peger på, plus en (+1), er lig med den næste værdi i listen
                                                # altså: vi er i starten af et interval 
           
            seqStart = L[i]                     # intervallets startværdi
            seqEnd = L[i+1]                     # intervallets slutværdi

            j = i+1
            while j+1 < len(L) and L[j]+1 == L[j+1]: # check at j stadig er indenfor listen
                                                     # ... og at vi stadig er i et interval

                seqEnd = L[j+1]                      # opdater slutværdien
                j += 1                               # index til næste

                                                # når det indre while loop slutter, 
                                                # er der ikke flere i intervallet
            res.append( (seqStart, seqEnd+1) )  # så, vi tilføjer start og slut    
            i = j                               # set i til j, så vi kan begynde forfra, med derfra vi nåede til

        else:
            res.append(L[i])                    # single

        i += 1                                  # næste
        
    return res    

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
