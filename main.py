from identifier import defineLexemsFromFile

print('Enter number of test file:\n',
      '\texample.c - 0\n',
      '\tdigits.c - 1')
n = int(input('n: '))
if n == 0:
    defineLexemsFromFile('example.c')
elif n == 1:
    defineLexemsFromFile('digits.c')