def kasir():
    print('='*40)
    print('      Chasier Program With Python')
    print('='*40)
    print()
    print('Choose a Menu: ')
    print('1. Clothes')
    print('2. Food')
    print('3. Item')
    menu = str(input('What do you select? : '))
    if menu == '1':
        print('You have selected (1)')
        print('='*20)
        print()
        print('Choose a Model:')
        print('1. Drees ($100)')
        print('2. Shirt ($20)')
        print('3. T-Shirt ($10)')
        print('4. Pants ($20)')
        choose = str(input('What do you select? : '))
        if choose == '1':
            a = int(input('How many? : '))
            jumlah = a * 100
            print('Total of All is : $', jumlah)
            print()
            pay = int(input('How many your pay? : $'))
            total = pay - jumlah
            print('charge is : ', total)
            print('='*20)
            select = str(input('Try again? (y/n) : '))
            print('='*20)
            if select == 'y':
                kasir()
            elif select == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        elif choose == '2':
            a = int(input('How many? : '))
            jumlah = a * 20
            print('Total of All is : $', jumlah)
            print()
            pay = int(input('How many your pay? : $'))
            total = pay - jumlah
            print('charge is : ', total)
            print('='*20)
            select = str(input('Try again? (y/n) : '))
            print('='*20)
            if select == 'y':
                kasir()
            elif select == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        elif choose == '3':
            a = int(input('How many? : '))
            jumlah = a * 10
            print('Total of All is : $', jumlah)
            print()
            pay = int(input('How many your pay? : $'))
            total = pay - jumlah
            print('charge is : ', total)
            print('='*20)
            select = str(input('Try again? (y/n) : '))
            print('='*20)
            if select == 'y':
                kasir()
            elif select == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        elif choose == '4':
            a = int(input('How many? : '))
            jumlah = a * 20
            print('Total of All is : $', jumlah)
            print()
            pay = int(input('How many your pay? : $'))
            total = pay - jumlah
            print('charge is : ', total)
            print('='*20)
            select = str(input('Try again? (y/n) : '))
            print('='*20)
            if select == 'y':
                kasir()
            elif select == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        else:
            print('INVALID RANGE!')
            kasir()          
    elif menu == '2':
        print('You have selected (2)')
        print('='*20)
        print()
        print('Choose a Model:')
        print('1. Burger ($1)')
        print('2. Pizza ($20)')
        print('3. Krabby Patty ($5)')
        print('4. Punk Shit me i am ($5)')
        choose1 = str(input('What do you select? : '))
        if choose1 == '1':
            a1 = int(input('How many? : '))
            jumlah1 = a1 * 1
            print('Total of All is : $', jumlah1)
            print()
            pay1 = int(input('How many your pay? : $'))
            total1 = pay1 - jumlah1
            print('charge is : ', total1)
            print('='*20)
            select1 = str(input('Try again? (y/n) : '))
            print('='*20)
            if select1 == 'y':
                kasir()
            elif select1 == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        elif choose1 == '2':
            a2 = int(input('How many? : '))
            jumlah2 = a2 * 20
            print('Total of All is : $', jumlah2)
            print()
            pay2 = int(input('How many your pay? : $'))
            total2 = pay2 - jumlah2
            print('charge is : ', total2)
            print('='*20)
            select2 = str(input('Try again? (y/n) : '))
            print('='*20)
            if select2 == 'y':
                kasir()
            elif select2 == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        elif choose1 == '3':
            a3 = int(input('How many? : '))
            jumlah3 = a3 * 5
            print('Total of All is : $', jumlah3)
            print()
            pay3 = int(input('How many your pay? : $'))
            total3 = pay3 - jumlah3
            print('charge is : ',total3)
            print('='*20)
            select3 = str(input('Try again? (y/n) : '))
            print('='*20)
            if select3 == 'y':
                kasir()
            elif select3 == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        elif choose1 == '4':
            a4 = int(input('How many? : '))
            jumlah4 = a4 * 5
            print('Total of All is : $', jumlah4)
            print()
            pay4 = int(input('How many your pay? : $'))
            total4 = pay4 - jumlah4
            print('charge is : ', total4)
            print('='*20)
            select4 = str(input('Try again? (y/n) : '))
            print('='*20)
            if select4 == 'y':
                kasir()
            elif select4 == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        else:
            print('INVALID RANGE!')
    elif menu == '3':
        print('You have selected (3)')
        print('='*20)
        print()
        print('Choose a Model:')
        print('1. Pen ($1)')
        print('2. Book ($2)')
        print('3. Coloring Pen ($5)')
        print('4. Pencil ($1)')
        choose2 = str(input('What do you select? : '))
        if choose2 == '1':
            a5 = int(input('How many? : '))
            jumlah5 = a5 * 1
            print('Total of All is : $', jumlah5)
            print()
            pay5 = int(input('How many your pay? : $'))
            total5 = pay5 - jumlah5
            print('charge is : ', total5)
            print('='*20)
            select5 = str(input('Try again? (y/n) : '))
            print('='*20)
            if select5 == 'y':
                kasir()
            elif select5 == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        elif choose2 == '2':
            a6 = int(input('How many? : '))
            jumlah6 = a6 * 2
            print('Total of All is : $', jumlah6)
            print()
            pay6 = int(input('How many your pay? : $'))
            total6 = pay6 - jumlah6
            print('charge is : ', total6)
            print('='*20)
            select6 = str(input('Try again? (y/n) : '))
            print('='*20)
            if select6 == 'y':
                kasir()
            elif select6 == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        elif choose2 == '3':
            a7 = int(input('How many? : '))
            jumlah7 = a7 * 5
            print('Total of All is : $', jumlah7)
            print()
            pay7 = int(input('How many your pay? : $'))
            total7 = pay7 - jumlah7
            print('charge is : ', total7)
            print('='*20)
            select7 = str(input('Try again? (y/n) : '))
            print('='*20)
            if select7 == 'y':
                kasir()
            elif select7 == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        elif choose2 == '4':
            a8 = int(input('How many? : '))
            jumlah8 = a8 * 5
            print('Total of All is : $', jumlah8)
            print()
            pay8 = int(input('How many your pay? : $'))
            total8 = pay8 - jumlah8
            print('charge is : ', total8)
            print('='*20)
            select8 = str(input('Try again? (y/n) : '))
            print('='*20)
            if select8 == 'y':
                kasir()
            elif select8 == 'n':
                print('Thank you for using my program:)')
            else:
                print('INVALID SELECT!')
        else:
            print('INVALID RANGE!')
        
            
kasir()