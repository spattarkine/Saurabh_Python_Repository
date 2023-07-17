from numpy import random

class User:
"""
Represents a user that will click an ad based on a secret probability
...
Attributes
----------
__probability : float
private attribute representing the probability that the user will click an ad
Methods
-------
show_ad():
A method to simulate showing an ad to a user. A boolean is return
based on the user's secret probability of clicking an ad
"""

    def _init_(self):
    """ Initializer for a user
    """
        self.__probability = random.uniform(0, 1)

    def get_probability(self):
    """ Returns the secret probability.
    Args:
    Returns:
    float: User's probability of clicking an ad
    """
    return self.__probability

    def show_ad(self):
    """ Displays an ad to a user. The user clicks the ad based on their secret probability.
    Args:
    Returns:
    bool: Indicator if the user clicked the ad or not
    """

        # draw a random number to simulate whether the user clicked
        click_threshold = random.uniform(0, 1)

        # compare the random draw to the secret probability to represent if the user clicked
        if click_threshold <= self.__probability:
            return True

        return False


class Auction:
"""
Represents an auction containing 1 or more rounds.
...
Attributes
----------
users : list[User]
list of users who are participants in the auction
bidders : list[Bidder]
list of bidders who bid on the right to display an ad to a user
balances : dict[Bidder->float]
list of account balances for all bidders. initialized to a list 0s of size len(bidders)
Methods
-------
execute_round():
A method to simulate a single round of an auction in which bidders
bid on the right to show an ad to a user and are rewarded when
the user clicks the ad
"""

    def _init_(self, users, bidders):
    """ Initializer for an Auction
    Args:
    num_users (list[User]): The list of Users participating in the auction

    num_round (list[Bidder]): The list of Bidders participating in the auction
    Returns:
    """

        self.users = users
        self.bidders = bidders
        
        # initialize all balances to 0
        self.balances = {bidder: 0 for bidder in bidders}

    def execute_round(self):
    """ A method to simulate a single round of an auction in which
    bidders bid on the right to show an ad to a user and are rewarded
    when the user clicks the ad. Notifies bidders of round results via notify()
    Args:
    Returns:
    """

        # select a random user for the round
        random_user = randint(0, len(self.users))

        bids = {}
        for bidder in self.bidders:
           # call each bidder's bid method to place the bid
            bids[bidder] = bidder.bid(random_user)

        # select the winning bidder and winning price (second highest bid)
        highest_bid = 0
        winning_price = 0
        
        for bidder, bid_value in bids.items():
        # evaluate the bid to determine if it is the highest
        # the highest bidder wins the round
            if bid_value > highest_bid:
            # set the winning bid price to the previous high bid
                winning_price = highest_bid
                highest_bid = bid_value
            # this case is for when the bid price < highest bid but > the current winning price
            elif bid_value > winning_price:
                winning_price = bid_value

        # tie-breaking logic
        winning_bidders = []
        # create a list of all bidders who bid the highest price
        for bidder in self.bidders:
            if bids[bidder] == highest_bid:
                winning_bidders.append(bidder)
                # randomly select the winning bidder from this list
                winning_bidder_index = (0 if len(winning_bidders) == 1 else randint(0, len(winning_bidders)))
                winning_bidder = winning_bidders[winning_bidder_index]

        # show the ad to the user
        ad_result = self.users[random_user].show_ad()

        for bidder in self.bidders:
            if bidder == winning_bidder:
            # send notification to the winning bidder and update the balance
                bidder.notify(True, winning_price, ad_result)
                self.balances[bidder] -= winning_price
        if ad_result:
            self.balances[bidder] += 1
        else:
            # send notification to the losing bidders
            bidder.notify(False, winning_price, None)        
            