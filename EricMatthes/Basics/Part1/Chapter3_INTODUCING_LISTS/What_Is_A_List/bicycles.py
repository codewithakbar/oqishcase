bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

"""Accessing Elements in a List"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

"""Index Positions Start at 0, Not 1"""

print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

"""Using individual Values from a List"""

message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)


