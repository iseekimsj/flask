from calculator.controller import CalculatorController

if __name__ == '__main__':
    num1 = int(input('첫번째 수 \n'))
    num2 = int(input('두번째 수 \n'))

    op = input('연산자는? \n')

    calc = CalculatorController(num1, num2)
    result = calc.exec(op)

    print('계산결과: %d' % result)



