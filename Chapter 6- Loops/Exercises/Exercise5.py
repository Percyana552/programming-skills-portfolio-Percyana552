#
"""Using the list sandwich_orders from Exercise 7-8,
make sure the sandwich 'pastrami' appears in the list at least three times.Add code
near the beginning of your program to print a message saying the deli has run out of pastrami,
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
Make sure no pastrami sandwiches end up in finished_sandwiches."""

sandwich_orders=['pastrami','Turkey','pastrami', 'Cheese', 'Chicken','pastrami']
finished_sandwiches=[]
print("the deli ran out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders != []:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich")
for sandwich in finished_sandwiches:
    print(f"The sandwich that was made is {sandwich}")
    