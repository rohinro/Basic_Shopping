available = ['T-shirt', 'Wrangler Jeans', 'Leather Jacket', 'NIKE AIR MAX ', 'Wrist Watches', 'Cologne']
current_status = ' '
updated_cart = [ ]

valid_choices = [str(i) for i in range(1,len(available)+1)]  #list comprehension
print(valid_choices)
while current_status != '0':
    if current_status in valid_choices:
        print('Adding {}: '.format(current_status))
        if current_status == '1':
            updated_cart.append('T-shirt')
        elif current_status == '2':
            updated_cart.append('Wrangler Jeans')
        elif current_status == '3':
            updated_cart.append('Leather Jacket')
        elif current_status == '4':
                updated_cart.append('NIKE AIR MAX ')
        elif current_status == '5':
                updated_cart.append('Wrist Watches')
        elif current_status == '6':
                updated_cart.append('Cologne')
        print('{}'.format(updated_cart))
    else:
        print('Please add options from list below')
        for number, part in enumerate(available, 1):
            print("{0}: {1}".format(number, part))

    current_status = input()
print('Cart details : ', updated_cart)