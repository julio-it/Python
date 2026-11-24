valid_coins = [5, 10, 25]
cost = 50

print('Amount Due: 50')

while True:
    inserted_coin = int(input('Insert Coin: '))

    if inserted_coin in valid_coins:
        cost -= inserted_coin

        if cost < 0:
            print(f'Change Owed: {cost * -1}')
            break

        elif cost == 0:
            print(f'Change Owed: 0')
            break
        
        else:
            print(f'Amount Due: {cost}')
    else:
        print('Amount Due: 50')
