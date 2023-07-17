from random import randint
from numpy import random
 
class User:
    def __init__(self):
        self.__click_prob = random.uniform(0, 1)
    
    def show_ad(self):
        return random.random() <= self.__click_prob

class Auction:
    def __init__(self, num_users, num_rounds):
        self.users = [User() for _ in range(num_users)]
        self.bidders = [Bidder() for _ in range(num_bidders)]
        self.num_rounds = num_rounds

    def run(self):
        for round in range(self.num_rounds):
            user = random.choice(self.users)
            bids = [(bidder, bidder.bid(user.id)) for bidder in self.bidders]
            winner, winning_bid = max(bids, key=lambda x: x[1])
            second_highest_bid = max(bid for _, bid in bids if bid < winning_bid)
            winning_price = second_highest_bid if second_highest_bid else 0
            clicked = user.show_ad()
            for bidder, bid in bids:
                bidder.notify(bidder == winner, winning_price, clicked)