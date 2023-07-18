from random import randint
from numpy import random
 
class User:
    def __init__(self):
        self.__click_prob = random.uniform(0, 1)
    
    def show_ad(self):
        return random.random() <= self.__click_prob

class Auction:
    def __init__(self, users, bidders):
        self.users = users
        self.bidders = bidders

    def execute_round(self):
        user = random.choice(self.users)
        bids = [bidder.bid(user_id=user_id) for user_id, bidder in enumerate(self.bidders)]
        winner_idx = max(range(len(self.bidders)), key=lambda i: bids[i])
        winners = [i for i in range(len(self.bidders)) if bids[i] == bids[winner_idx]]
        winning_price = max(bids)
        if len(winners) > 1:
            winning_price = bids[winner_idx]
        clicked = user.show_ad()
        for i, bidder in enumerate(self.bidders):
            bidder.notify