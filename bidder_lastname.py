import random
class Bidder:
    def __init__(self):
        self.__balance = 0
    
    def bid(self, user_id):
        return random.uniform(0, self.__balance + 1)
    
    def notify(self, auction_winner, price, clicked):
        if auction_winner:
            self.__balance -= price
            if clicked:
                self.__balance += 1