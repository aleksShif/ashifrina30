import random as rand
#import csv

occupations_file = open('occupations.csv', 'r')
occupations = occupations_file.readlines()
occupations = occupations[1:len(occupations)-1]

occup = {}
for i in range(len(occupations)):
    temp = occupations[i].replace("\n", "") #removes any instances of \n from element of occupations
    temp = temp.replace(", ", "|") #replaces any instance of a comma followed by a whitespace(, ) with a bar - this is in order to prevent errors with splitting by commas later
    pair = temp.split(",") #splits temp into a list containing occupation and percentage as separate elements(using comma)
    pair[0] = pair[0].replace("|", ", ") #undoes line 12 to convert occupation back into regular form
    pair[0] = pair[0].replace('"', '') #removes any instances of double quotation marks around occupation
    pair[1] = float(pair[1]) #stores percentages as floats

def not_so_rando_occup(o):
    
    
    