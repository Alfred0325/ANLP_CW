import re
import sys
from random import random
from math import log
from collections import defaultdict

tri_counts=defaultdict(int) #counts of all trigrams in input

#this function currently does nothing.
def preprocess_line(line):
    return line

if __name__ == "__main__":
    #here we make sure the user provides a training filename when
    #calling this program, otherwise exit with a usage error.
    if len(sys.argv) != 2:
        print("Usage: ", sys.argv[0], "<training_file>")
        sys.exit(1)

    infile = sys.argv[1] #get input argument: the training file

    with open(infile) as f:
        for line in f:
            line = preprocess_line(line) #doesn't do anything yet.
            for j in range(len(line)-(3)):
                trigram = line[j:j+3]
                tri_counts[trigram] += 1


                

    # print("Trigram counts in ", infile, ", sorted alphabetically:")
    # for trigram in sorted(tri_counts.keys()):
    #     print(trigram, ": ", tri_counts[trigram])

    # print("Trigram counts in ", infile, ", sorted numerically:")
    # for tri_count in sorted(tri_counts.items(), key=lambda x:x[1], reverse = True):
    #     print(tri_count[0], ": ", str(tri_count[1]))