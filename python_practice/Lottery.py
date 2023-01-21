import random
from random import choice

lottery_list = ['a', 'c', 'f', 'g', 'j', 'k', 'm', 'z', '1', '4', '6', '9', '0']
length = len(lottery_list)
print(length)
lottery_value = []

for i in range(1,5):
    lottery_value.append(choice(lottery_list))
winning_choice = ''.join(lottery_value)
print(f"The winning number is: {winning_choice}\n\n")

my_ticket = []
loop_count = 0
while my_ticket != winning_choice:
    my_ticket.append(choice(lottery_list))
    my_choice = ''.join(my_ticket)
    loop_count = loop_count + 1
    if my_choice.__eq__(winning_choice): 
        print(f"It took {loop_count} loops to get to the winning ticket\n\n")

# print(f"It took {loop_count} loops to get to the winning ticket\n\n")

