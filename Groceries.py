shopping_list = ['milk','pasta','bread','rice','cake','eggs']
another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

print('^'*30)

shopping_list+= ['cookies']
print(shopping_list)
print(id(shopping_list))
print(id(another_list))
print()
print(another_list)

a=b=c=d=e=f= another_list
print()
print('a',a)
print('         Adding cream')
b.append('cream')
print('b',b)
print('c',c)
print('d',d)
print('a',a)