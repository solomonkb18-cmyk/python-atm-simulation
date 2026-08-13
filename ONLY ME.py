ATTEMPTS=3
NAME='MA AWINGAIH'
for i in range(3):
    WHO=(input('WHO ARE YOU...'))
    if WHO == NAME:
        print('I LOVE YOU SO MUCH. I MISS YOU BBY. WILL YOU MARRY ME? ')
        break
    else:
        ATTEMPTS-=1
        if ATTEMPTS>0:
            print(f'{ATTEMPTS} TIMES LEFT.')
        else:
            print('MANY INCORRECT ATTEMPTS...(TRY AGAIN)!')