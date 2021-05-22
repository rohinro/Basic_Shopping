available = ["Levi's T-shirt",'Wrangler Jeans','Zara Jacket','NIKE AIR MAX 90','Daniel Wellington Watches','Lacoste Perfume']
current_status = ' '
updated_cart = [ ]  #intially empty

valid_choices = [str(i) for i in range(1,len(available)+1)]  #list comprehension
print(valid_choices)

while current_status != '0':
    if current_status in valid_choices:
        index = int(current_status)
        selected = available[index]

        if selected in updated_cart:                       #removal of items
            print('Removing {}: '.format(current_status))  # prints index
            updated_cart.remove(selected)
            print("{}".format(updated_cart))
        else:
            print('Adding {}: '.format(current_status))  # prints index
            updated_cart.append(selected)

        print("{}".format(updated_cart))                #prints items

    else:
        print('Please add options from list below')
        for number, part in enumerate(available, 1):
            print("{0}: {1}".format(number, part))

    current_status = input()
print('Cart details : ', updated_cart)