# Week 2 - Create a Dynamic Shopping Cart Program
## Task Number: 1
Deadline: 2025-01-20 00:00:00
### Description (Part 1)
Write a Python program that simulates a shopping cart. The program should:

- Use a function called add_to_cart that accepts the following arguments:
- item_name (required): The name of the item to add.
- price (required): The price of the item.
- *args: Optional discounts (e.g., percentage discounts like 10% 20%, etc.).
- **kwargs: Optional item details (e.g., color="red", size="large", etc.).

Calculate the final price of the item after applying all discounts (if any).

Use a loop to allow the user to add multiple items to the cart.

Use if conditions to:
- Check if the item already exists in the cart (avoid duplicates).
- Apply discounts only if they are provided.

Display the cart summary at the end, including:
- All items added.
- Their final prices.
- The total cost of all items in the cart.


## Example Output:

Enter item name (or 'done' to finish): Laptop
Enter item price: 1000
Enter discounts (if any, separated by space
### Description (Part 2)
s): 10 5
Enter item details (e.g., color=red size=large): color=black weight=2kg
Item added: Laptop - Final Price: $855.0

Enter item name (or 'done' to finish): Mouse
Enter item price: 50
Enter discounts (if any, separated by spaces):
Enter item details (e.g., color=red size=large): color=white
Item added: Mouse - Final Price: $50.0

Enter item name (or 'done' to finish): done

## --- Cart Summary ---
Laptop - $855.0 (color=black, weight=2kg)
Mouse - $50.0 (color=white)
Total Cost: $905.0