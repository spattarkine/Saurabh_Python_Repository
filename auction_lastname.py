from numpy import random
from numpy.random import randint

class User:
    """
    Represents a user that will click an ad based on a secret probability. 
    """

    def __init__(self):
        """ Initialize user attributes in this constructor
        """

        self.__probability = random.uniform(0, 1)

    def get_probability(self):
        """ Returns the secret probability.
        """
        return self.__probability

    def show_ad(self):
        """ Displays an ad to a user. Clicks are made based on secret probability.
        """

        # draw a random number to evaluate user clicks.
        clk_threshold = random.uniform(0, 1)

        # compare the random draw to the secret probability
        if clk_threshold <= self.__probability:
            return True

        return False
class Auction:
    """
    Represents an auction containing 1 or more rounds and consequences of user clicks on the ad
    """

    def __init__(self, users, bidders):
        """ Initializer for an Auction - Constructor
        
        """

        self.users = users
        self.bidders = bidders
        # initialize all balances to 0 this will help reset values in multiple rounds / games.
        self.balances = {bidder: 0 for bidder in bidders}

    def execute_round(self):
        """
        This method ensures one round is conducted and returns notification.
        """

        # Random user for the round
        random_user = randint(0, len(self.users))

        bids = {}
        for bidder in self.bidders:
            # call each bidder's bid method to apply the bid
            bids[bidder] = bidder.bid(random_user)

        # select highest and second highest bidder
        highest_bid = 0
        winning_price = 0
        for bidder, bid_value in bids.items():
            # evaluate the bid to determine if it is the highest
            # the highest bidder wins the round
            if bid_value > highest_bid:
                # set the winning bid price to the previous high bid
                winning_price = highest_bid
                highest_bid = bid_value
            # this case is for when the bid price is one less than highest the current winning price
            elif bid_value > winning_price:
                winning_price = bid_value

        # Handle edge case in case there is a tie between bidders.
        winning_bidders = []
        # Add bidders who bid the highest price to the list.
        for bidder in self.bidders:
            if bids[bidder] == highest_bid:
                winning_bidders.append(bidder)
        # randomly select the highest bidder from this list
        winning_bidder_index = (0 if len(winning_bidders) == 1 else randint(0, len(winning_bidders))
        )
        winning_bidder = winning_bidders[winning_bidder_index]

        # Display the ad to the current user
        ad_result = self.users[random_user].show_ad()

        for bidder in self.bidders:
            if bidder == winning_bidder:
                # send message to the winning bidder + update the balance
                bidder.notify(True, winning_price, ad_result)
                self.balances[bidder] -= winning_price
                if ad_result:
                    self.balances[bidder] += 1
            else:
                # send message to the losing bidders
                bidder.notify(False, winning_price, None)
