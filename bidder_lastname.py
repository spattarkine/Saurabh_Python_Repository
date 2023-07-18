class Bidder:
    """
    Object of this class represents bidder in the auction
    """

    def __init__(self, num_users, num_rounds):
        """ Initializer for a bidder
        """

        self.num_users = num_users
        self.num_rounds = num_rounds
        self.bidding_round = 0

        # clearing prices for each user
        self.user_clearing_prices = {i: [] for i in range(num_users)}
        # dictionary mapping users to number of bids won for a user
        self.user_wins = {i: 0 for i in range(num_users)}
        # dictionary mapping the number of clicks for a user
        self.user_clicks = {i: 0 for i in range(num_users)}
        # the ratio of clicks to winning bids
        self.user_click_ratio = {i: 0. for i in range(num_users)}
        # current round number
        self.current_round_user_id = -1

        # percentage of users to explore before starting exploitation
        self.exploration_users = .25
        # if there are a small number of users relative to the number
        # of rounds, explore all users
        if self.num_users / self.num_rounds <= .2:
            self.exploration_users = 1
        # bid price during exploration
        self.exploration_bid_price = 1.
        self.default_bid_price = 0.5

        # next bid for a specific user
        # self.next_bid = {user_id : self.unseen_user_bid_price for user_id in range(num_users)}
        self.next_bid = {i: self.default_bid_price for i in range(num_users)}

        # set max bid amounts for high/med/low confidence bids
        self.high_bid_max = 0.99
        self.med_bid_max = 0.65
        self.low_bid_max = 0.1

        # adders applied to bids based on the last clearing price
        self.large_adder = 0.01
        self.small_adder = 0.005

        # phase of algorithm - explore or exploit
        self.phase = 'explore'

    def bid(self, user_id):
        """ Place a bid for the right to show an ad to a specific user
        Args:
            user_id (int): The user id that is being bid on
        Returns:
            float: the value of the bid > 0
        """

        self.bidding_round += 1
        self.current_round_user_id = user_id
        bid_price = self.default_bid_price


        # exploit if in exploitation phase, or the user has been seen before
        if self.user_wins[self.current_round_user_id] > 0 or self.phase == 'exploit':
            bid_price = self.next_bid[self.current_round_user_id]
        else:
            # if in exploration phase, try to win the round
            bid_price = self.exploration_bid_price
        return bid_price

    def notify(self, auction_winner, price, clicked):
        """ Notify the bidder of auction results
        """

        # update the list of clearing prices for this user
        self.user_clearing_prices[self.current_round_user_id].append(price)
        print(f"Winning bid price  was {price}")

        if auction_winner:
            # update the list of total winning bids for this user
            self.user_wins[self.current_round_user_id] += 1

            if clicked:
                # update the number of clicks for this user
                self.user_clicks[self.current_round_user_id] += 1
            # calculate the click ratio for the user
            if self.user_wins[self.current_round_user_id] > 0:
                self.user_click_ratio[self.current_round_user_id] = self.user_clicks[self.current_round_user_id] / self.user_wins[self.current_round_user_id]
            else:
                self.user_click_ratio[self.current_round_user_id] = 0
        # determine the phase based on the number of users who've been explored
        if len(self.user_wins.keys()) / self.num_users >= self.exploration_users or len(self.user_wins.keys()) == self.num_users:
            self.phase = 'exploit'
