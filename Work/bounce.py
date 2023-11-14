# bounce.py
#
# Exercise 1.5

height = 100 # meters
next_bounce_ratio = 3 / 5
bounces = 10

for i in range(bounces):
    height *= next_bounce_ratio
    print(i + 1, round(height, 4))
