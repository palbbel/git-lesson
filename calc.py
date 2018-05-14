from collections import deque, namedtuple
import operator
from io import StringIO
import tokenize

Operator = namedtuple('Operator', ('assoc', 'prior', 'func'))  # тип данных задаем

LEFT_ACCOS = -1  # левая ассоциативность
RIGHT_ACCOS = 1  # правая ассоциативность

OPER = {
    '+': Operator(LEFT_ACCOS, 10, operator.add),
    '-': Operator(LEFT_ACCOS, 10, operator.sub),
    '*': Operator(LEFT_ACCOS, 11, operator.mul),
    '/': Operator(LEFT_ACCOS, 11, operator.truediv),
    '%': Operator(LEFT_ACCOS, 11, operator.mod),
    '//': Operator(LEFT_ACCOS, 11, operator.floordiv),
    '^': Operator(RIGHT_ACCOS, 13, operator.pow)
    }


def convert(expr):
    rpn = deque()
    stack = deque()

    for token in tokenize.generate_tokens(StringIO(expr).readline):
        #print(token)
        token_type, value, *_ = token
        #print(token_type, value,)

        if token_type == tokenize.NUMBER:
            rpn.append(value)
        elif token_type == tokenize.OP:
            if value == '(':
                stack.append(value)
            elif value == ')':
                while stack:
                    top = stack.pop()

                    if top == '(':
                        break

                    rpn.append(top)

            else:
                oper_info = OPER.get(value)
                flag = True
                while stack and stack[-1] != '(' and flag:
                    top_oper = stack[-1]
                    top_oper_info = OPER.get(top_oper)
                    flag = (oper_info.assoc == RIGHT_ACCOS and oper_info.prior < top_oper_info.prior) \
                           or (oper_info.assoc == LEFT_ACCOS and oper_info.prior <= top_oper_info.prior)

                    if flag:
                        rpn.append(stack.pop())


                stack.append((value))

    while stack:
        rpn.append(stack.pop())

    return ' '.join(rpn)


def calc(expr):
    rpn = convert(expr)
    stack = deque

    for token in rpn.split(' '):
        if token in OPER:
            op2, op1 = stack.pop(), stack.pop()

            oper = OPER.get(token)
            stack.append(oper.func(op1, op2))
        else:
            stack.append(float(token))

    #print(stack.pop())
    return stack.pop()



#print(convert('(-10 + 21) // 100 - 38'))

if __name__ == '__main__':
    print(calc(input()))