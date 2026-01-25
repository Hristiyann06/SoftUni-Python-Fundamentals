n = int(input())
text = ''
unbalanced = False

for i in range(1, n + 1):
    symbol = input()
    if symbol != '(' and symbol != ')':
        continue
    elif symbol == '(' and text == '':
        text += symbol
    elif symbol == ')' and text == '(':
        text = ''
    else:
        unbalanced = True

if unbalanced:
    print('UNBALANCED')
else:
    print('BALANCED')

