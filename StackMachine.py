import operator
import functools

s = '13+62*7+*'

stack = []
stack2  = []
prev = str
c1 = []

for i in s:

 if i.isdigit():

  stack.append(i)

  ##print('1 ', stack)

  c1.append(i)
  ##print('c1 ', stack)


 elif not i.isdigit() and len(stack) >= 2:

  if (prev in ('+', '*')) and (i in ('+', '*')):

   del stack[len(stack) - 2]

   if i == '+':

    stack.append(int(stack[-2]) + int(stack[-1]))
    stack = list(filter(lambda x: x not in c1, stack))
    ##print('2 ', stack)


   elif i == '*' and len(stack) >= 2:

    stack.append(int(stack[-2]) * int(stack[-1]))
    stack = list(filter(lambda x: x not in c1, stack))
    ##print('3', stack)

  else:

        if i == '+':

           stack.append(int(stack[-2]) + int(stack[-1]))
           stack = list(filter(lambda x: x not in c1, stack))
           ##print('2 ', stack)


        elif i == '*' and len(stack) >= 2:

           stack.append( int(stack[-2]) * int(stack[-1]) )
           stack = list(filter(lambda x: x not in c1, stack))
           ##print('3', stack)

 else:

  print('-1')

  ## (if Function) break

 prev = i

## Will always hit because it's not in the function,
# otherwise the break would do
print (stack[ -1 ])
