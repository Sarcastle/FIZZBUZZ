y = int(input('Input max number for FIZZBUZZ\n'))

for x in range(1,y):
    isfizz = x % 3 == 0
    isbuzz = x % 5 == 0
    isfizzbuzz = isfizz and isbuzz

    if isfizzbuzz:
        print('fizzbuzz')
    elif isbuzz: 
        print('buzz')
    elif isfizz:
        print('fizz')
    else: 
        print(f'{x}')