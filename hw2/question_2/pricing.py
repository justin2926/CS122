apply_tax = lambda price: price*1.08 

def apply_discount(func):
    def wrapper(price):
        if price > 100.0:
            price *= 0.9
            return func(price)
        else:
            return apply_tax(price)
    return wrapper

def price_generator(prices, processing_function):
    for price in prices:
        yield processing_function(price)
