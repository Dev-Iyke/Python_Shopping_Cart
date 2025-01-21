# Initialized the cart as an empty list
cart = []

def add_to_cart(item_name, price, *args, **kwargs) -> dict:
  """
  This is a function that takes the details of an item and add it to the cart
  parameters
  item_name: str, the name of the item
  price: float, the price of the item
  *args: tuple, additional arguments for the item (discount)
  **kwargs: dict, keyword arguments for the item (size, color)

  returns:
  List[dict], the updated cart with the new item added
  """

  item_to_add = {
    'name': item_name,
    'price': float(price),
    'discount': float(args[0]),
    'size': kwargs['size'],
    'color': kwargs['color'],
    'final_price': price - (price * (args[0]/100))
  }

  # Check if the item already exists in the cart, if so, print a message and return the cart without adding the new item
  for item in cart:
    if (item['name'] == item_to_add['name']):  
      print(f'{item_name} already exists in the cart')
      return
  cart.append(item_to_add)
  print(f'Added {item_name} to the cart')
  return cart

#  Allows the user to add multiple items to the cart. 
while True:
  item_name = input('Enter item name or done to finish: ')
  if item_name == 'done':
    break
  else:
    try:
      item_price = int(input('Enter item price: '))
      item_discount = int(input('Enter item discount: '))
      item_size = input('Enter item size: ')
      item_color = input('Enter item color: ')
    finally:
      add_to_cart(item_name, item_price, item_discount, size=item_size, color=item_color)


def get_summary() -> float:
  """
  This function calculates and prints the total cost of all items in the cart
  
  returns:
  float, the total cost of all items in the cart
  """
  total = 0
  for item in cart:
    print(f"{item['name']} - ${item['final_price']} (color = {item['color']}, size = {item['size']})")
    total += item['final_price']

  print(f'Cost: {total}')
  return total

# Check if the cart is empty before printing the summary
if cart:
  get_summary()

print('The end')
