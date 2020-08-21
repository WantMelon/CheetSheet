#strings
print('This is a string!')
print('''This is second string
in the program''')
print(f'This is {3}-rd string\nBut it f-string')

print('-' * 20)

#math
print('Math time: ')
print(50 + 50) #100
print(50 - 20) #30
print(2 * 10) #20
print(10 / 2) #5
print(12 ** 2) #144
print(17 // 7) #2
print(12 % 5) #2

print('-' * 20)

#variables & methods
print('Fun with variables and methods: ')
str = 'It is a simple string'
print(len(str)) #length
print(str.upper()) #uppercase
print(str.lower()) #lowercase
print(str.title()) #titlecase
print(str.replace('simple', 'not simple'))

n = str.find('string')
print(str[n:]) #string

n = str.count(' ') + 1
print(f'In the string {n} words')

arr = str.split(' ') #list
dic = {} #dictionary
for x in arr:
    dic[x] = len(x)
print(dic) #the number of letters in each word

n = 2.67
print(type(n))
print(int(n))
print(round(n))
print(max(n, 3))
del n
n = int(input("Enter a number: "))
print(f'Your number is {n}')

print('-' * 20)

#functions
print('Now some functions: ')
def who_am_i():
    name = 'Artem'
    age = 19
    print(f'Your name is {name}, you {age} years old!')
who_am_i()

def mul(a, b):
    return a * b
n = mul(12, 6)
print(f'12 * 6 = {n}')

def square_root(n):
    return n ** .5
print(square_root(121))

print('-' * 20)

#boolean expressions
print('Boolean expressions: ')
bool1 = True
bool2 = 3*3 == 9
bool3 = not(2+2 == 4)
bool4 = 3+3 == 6 and 2+2 == 10
bool5 = 3+3 == 6 or 2+2 == 10
bool6 = 7 > 8
bool7 = 10 <= 10

print(bool1, bool2, bool3, bool4, bool5, bool6, end = ' ')
print(bool7)

print('-' * 20)

#conditional statements
print('Conditional statements: ')
def soda(money):
    if money >= 2:
        return "You've buy a soda"
    else:
        return 'You don\'t have enoght money'
print(soda(8))

def alcohol(age, money):
    if (age >= 18) and (money >= 5):
        return 'It\'s OK'
    elif (age >= 18):
        return 'Where are your money?'
    elif (age < 18) and (money >= 5):
        return 'You\'re too small'
    else:
        return 'GET OUT!'
print(alcohol(19, 3))

print('-' * 20)

#lists
print('This is about lists: ')
numbers = [34, 72, 91, 20, 77, 56, 12]

print(numbers)
print(numbers[0])
print(numbers[0:3])
print(numbers[4:])
print(numbers[-2:])
print(len(numbers))
print(min(numbers))

numbers.append(33)
numbers.remove(72)
numbers.insert(2, 56)
numbers.sort()
numbers.reverse()
print(numbers)

print(numbers.index(91))
print(numbers.count(56))
print(numbers.pop())

account = list(range(len(numbers)))
print(account)

combined = zip(account, numbers)
print(list(combined)) #list/dict

numbers.clear()
account.clear()
