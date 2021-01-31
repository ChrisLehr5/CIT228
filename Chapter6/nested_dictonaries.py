print("------------------Chapter 6, Hands On #3 Nested Dictonary---------------------------")
yarns = {
'AM': {
    'brand': 'AMANO',
    'price': 7.49,
    'length': 109,
    'weight': 'worsted',
    },
'CB': {
    'brand': 'Cloudborn',
    'price': 3.99,
    'length': 192,
    'weight': 'sport',
    },
'OP': {
    'brand': 'Oink Pigments',
    'price': 27.00,
    'length': 205,
    'weight': 'fingering',
    },
}

for yarn, info in yarns.items():
    print(f"\nYarn: {info['brand']}")
    price = info['price']
    length = info['length']
    weight = info['weight']

    print(f"\tPrice: {price}")
    print(f"\tLength(yrds): {length}")
    print(f"\tWeight: {weight}")
