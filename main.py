cart = []

def add_to_cart(item_name, price, *args, **kwargs):
  print(kwargs)
  item_to_add = {
    'name': item_name,
    'price': float(price),
    'discount': float(args[0]),
    'size': kwargs['size'],
    'color': kwargs['color'],
    'final_price': price - (price * (args[0]/100))
  }
  print(item_to_add)
  cart.append(item_to_add)
  print(f'Added {item_name} to the cart')
  print(cart)


while True:
  item_name = input('Enter item name or q to exit: ')
  if item_name == 'q':
    break
  else:
    try:
      item_price = int(input('Enter item price: '))
      item_discount = int(input('Enter item discount: '))
      item_size = input('Enter item size: ')
      item_color = input('Enter item color: ')
    finally:
      add_to_cart(item_name, item_price, item_discount, size=item_size, color=item_color)


print('The end')
