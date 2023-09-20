response = input('Input max number for FIZZBUZZ\n')

if not response.isnumeric():
    print('Please enter a valid number.')
else:
    y = int(response)
    y +=1 
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