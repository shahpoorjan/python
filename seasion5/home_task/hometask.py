product_data = {
    "store": "TechNova",
    "location": {
        "city": "San Francisco",
        "country": "USA"
    },
    "products": [
        {
            "id": "P1001",
            "name": "Wireless Mouse",
            "brand": "LogiTech",
            "price": 29.99,
            "currency": "USD",
            "stock": 0,
            "specs": {
                "color": "Black",
                "connectivity": "Bluetooth",
                "battery_life": "12 months"
            },
            "ratings": {
                "average": 4.5,
                "count": 240
            }
        },
        {
            "id": "P1002",
            "name": "Mechanical Keyboard",
            "brand": "KeyChron",
            "price": 79.99,
            "currency": "USD",
            "stock": 0,
            "specs": {
                "color": "White",
                "switch_type": "Gateron Brown",
                "backlight": "RGB"
            },
            "ratings": {
                "average": 4.7,
                "count": 145
            }
        },
        {
            "id": "P1003",
            "name": "Sony Wireless Noise-Canceling Headphones",
            "brand": "Sony",
            "price": 199.99,
            "currency": "USD",
            "stock": 23,
            "specs": {
                "color": "Black",
                "connectivity": "Bluetooth",
                "noise_cancellation": "Active",
                "battery_life": "30 hours"
            },
            "ratings": {
                "average": 4.8,
                "count": 529
            }
        }
    ]
}
unique_products= set()
# TASK 1
for product in product_data['products']:
    if product['stock'] == 0:
        print('OUT OF STOCK PRODUCTS' , product['name'])
print('**********************************************************')
# TASK2
for product in product_data['products']:
    if product['price'] > 50.0 and product['ratings']['average'] > 4.5 :
        print('PRODUCTS OVER 50$ AND HIGHT RATING' , product['name'])
print('**********************************************************')
# TASK3:
for product in product_data['products']:
    unique_products.add(product['name'])
    print('UNIQUE PRODUCTS:' ,list(unique_products))
print('**********************************************************')
# TASK4:
for product in product_data['products']:
    discount=product['price'] * 0.10
    print(product['name'],'PRICE WAS:', product['price'] , '10 % discount applied new price =', round(discount ,2))


