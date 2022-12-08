try:
    lenght = int(input('lenght->'))
    sign = input('sign->') 
    for i in range(0, lenght): 
        print(sign, end='') 
except Exception as ex: 
    print (f'Error: {ex}') 
    print (f'Name: {ex.__class___.____name__}')
