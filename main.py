def add_to_cart(item_name, price, *args):
  # print(kwargs)
  item_to_add = {
    'name': item_name,
    'price': float(price),
    'discount': args[0],
    # 'properties': {
    #   'color': kwargs[color],
    #   'size': kwargs[size],
    # }
  }
  print(item_to_add)

cart = {}
while True:
  item_name = input('Enter item name or q to exit')
  if item_name == 'q':
    break
  item_price = input('Enter item price or q to exit')
  if item_price == 'q':
    break
  item_discount = input('Enter item discount or q to exit')
  if item_discount == 'q':
    break
  item_to_add = {
    'name': item_name,
    'price': float(item_price),
    'discount': float(item_discount),
  }
  cart[item_name] = item_to_add
  print(f'Added {item_name} to the cart')

print('The end')
print(cart)
# add_to_cart(name, price, discount)


# print(item_to_add)