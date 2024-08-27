def inc(sal):
    sal = sal + sal * 20 / 100
    return sal

sal = inc(1000)
print('Incremented Salary: %.2f' %sal)