import random

'''
Charles's Angels::Aleksandra Shifrina, Nakib Abedin, Ameer Alnasser
<Frist> <Lsat>
SoftDev
K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
<yyyy>-<mm>-<dd>
time spent: <elapsed time in hours, rounded to nearest tenth>
'''

krewes = {1:['A', 'B', 'C'], 2:['D', 'E', 'F']}
def find_devo(krewes):
    rando_key = random.randint(1, len(krewes))
    rando_value = random.randint(0, len(krewes[rando_key]))
    return krewes[rando_key][rando_value]

print(find_devo(krewes))
    
    
