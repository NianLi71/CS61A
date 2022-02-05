# run:
# python ChurchNumerals.py

from hw02 import *

four = successor(three)

print(f'add(three, one) = {church_to_int(add_church(three,one))}')
print(f'mul(three, four) = {church_to_int(mul_church(three,four))}')
print(f'two**three, pow(two, three) = {church_to_int(pow_church(two,three))}')
