try:
    start = int(input('start->'))
    end = int(input('end->'))
    sum = float(0)
    counter = 0
    for i in range(start, end+1):
        print(f'{sum} + {i} = {sum + i}\t counter = ', end="")
        sum += i
        counter += 1
        print(counter)
    print(f'sum = {sum}, Avg = {sum} / {counter} = {sum/counter}')
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')

