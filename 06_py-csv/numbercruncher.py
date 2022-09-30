import random as rand
#import csv

occupations_file = open('occupations.csv', 'r')
occupations = occupations_file.readlines()
occupations = occupations[1:len(occupations)-1]

occup = {}
for i in range(len(occupations)):
    temp = occupations[i].replace("\n", "")
    print(temp)
    temp.replace(", ", "|")
    pair = temp.split(",")
    print(pair)
    #pair = temp.split(",")
    #pair[0] = pair[0].replace('"', '')
    #print(pair)
    
    