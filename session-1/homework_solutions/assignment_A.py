first = 'Hello'
print(first)
second = ','
print(second)
third = 'you can'
print(third)
fourth = 'code!'
print(fourth)
last = 5
print(last)

print(type('Hello world'))

print(first)
print(second)
print(third)
print(fourth)
print(last)

# \n means new line

print(first, end='?')
print(second, end='?')
print(third, end='?')
print(fourth, end='?')
print(last, end='?')

print()
print(first, second, third, fourth)
print(first, second, third, fourth, sep=',')

print()
print(third.title()[0:3], 'r ', 'favourit number is ', second*last, fourth[-1], sep='')
print(third.title()[0:3], 'r ', 'favourit number is ', '+'.join(['1']*last), fourth[-1], sep='')
