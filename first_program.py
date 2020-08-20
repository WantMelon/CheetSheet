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


