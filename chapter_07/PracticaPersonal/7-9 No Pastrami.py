#Using the list sandwich_orders from Exercise 7-8,
# make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['pastrami','pollo','carne','pastrami','palta','pastrami','pastrami']
print(sandwich_orders)
print('se nos acabó el pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)