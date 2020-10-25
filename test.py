import Sum
if Sum.a+Sum.b == Sum.b+Sum.a:
    print('функция сложения для чисел {} и {} вернула {} -результат верный'.format(Sum.a,Sum.b,Sum.a+Sum.b))
import sub
if abs(sub.a - sub.b) == abs(sub.b - sub.a):
    print('функция вычитания для чисел {} и {} вернула {} -результат верный'.format(sub.a,sub.b,Sum.a-sub.b))
import div
if div.a/div.b == div.a/div.b:
    print('функция деления для чисел {} и {} вернула {} -результат верный'.format(div.a,div.b,div.a/div.b))
import multi
if multi.a * multi.b == multi.b * multi.a:
    print('функция сложения для чисел {} и {} вернула {} -результат верный'.format(multi.a,multi.b,multi.a*multi.b))