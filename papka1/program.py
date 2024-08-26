a = int(input('1 '))
b = int(input('2 '))
c = int(input('3 '))

def summ_calculate(first, second):
    result = first + second
    return result

ab = summ_calculate(a, b)
ac = summ_calculate(a, c)
bc = summ_calculate(c, b)

print(ab, ac, bc)


if ab > c and ac > b and bc > a:
    print('Всё ок!!!')
        
else:
    print('Треугольник хреновый!')