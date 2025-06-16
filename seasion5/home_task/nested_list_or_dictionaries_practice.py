products = [
    {
        "name": "USB-C Charger",
        "brand": "Anker",
        "price": 25.99,
        "stock": 10,
        "rating": 4.6
    },
    {
        "name": "Laptop Stand",
        "brand": "Rain Design",
        "price": 49.99,
        "stock": 0,
        "rating": 4.4
    },
    {
        "name": "Noise Cancelling Earbuds",
        "brand": "Sony",
        "price": 89.99,
        "stock": 5,
        "rating": 4.8
    }
]
# TASKS: 
# Write Python code to:
# 	1.	Print names of products that are out of stock
# (Hint: stock is 0)
# 	2.	Print products with price over $30 and rating over 4.5
# (Print name, price, rating)
# 	3.	Print original and 15% discounted price for each product

# task1
out_of_stock=[]
for key in products:
    if (key['stock']) == 0:
        out_of_stock.append(key['name'])
        print('out of stock product', key['name'] ,out_of_stock)
print('------------------------------------')

# task2
for key in products:
    if key['price'] > 30.0 and key['rating'] > 4.5:
        discount= key['price'] * 0.15
        new_price= key['price'] - discount
        print(key['name'] , key['price'] , 'dicsounted price' , round(new_price ,2))
print('------------------------------------')
# task3:
for key in products:
    discount= key['price'] * 0.15
    print('products with 15% discount' , key ['name'], round(discount,2) )
print('------------------------------------')