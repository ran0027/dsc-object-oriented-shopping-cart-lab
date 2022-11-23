import numpy as np

class ShoppingCart:
    # write your code here
    def __init__(self, total=0, emp_discount=None, items=[]):
      self.total = total
      self.emp_discount = emp_discount
      self.items = items
    
    def add_item(self, name, price, quantity=1):
        self.items.append({ name : [price, quantity] })
        self.total += (price*quantity)
        return self.total

    def mean_item_price(self):
        num_items = 0
        for item in self.items:
            for k, v in item.items():
                num_items+=v[1]
        return round(self.total / num_items,2)

    def median_item_price(self):
        # order items by price, taking into account the number of items of that type!
        # create empty list for prices
        list_of_prices = []
        
        # iterate through item dictionaries in self.items
        for item in self.items:
            # get the key, value pairs for each item in dictionary (there will only be one, so this loop runs once)
            for k, v in item.items():
                # for i in the range of quantity - runs once if quantity = 1, twice if quantity = 2, etc.
                for i in range(v[1]):
                    # append the price of the item to list of prices
                    list_of_prices.append(v[0])
        
        # put items in order
        list_of_prices.sort()
        
        # how many items total?
        n = len(list_of_prices)
        
        # if # of items is even, average middle two
        if n%2 == 0:
            median = (list_of_prices[n/2 - 1] + list_of_prices[n/2])/2
        # otherwise, median is number of numbers / 2, rounded down, plus 1
        else:
            median_loc = int(np.floor(n/2) + 1)
            median = list_of_prices[median_loc]
        
        # return median
        return median

    def apply_discount(self):
       if self.emp_discount:
            return self.total*(1 - self.emp_discount/100)
       else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
       if self.items:
           # remove last item from shopping cart
           to_remove = list(self.items.pop(-1).values())[0]
           # update total
           self.total -= to_remove[0]
           return self.total
       else:
           return "There are no items in your cart!"