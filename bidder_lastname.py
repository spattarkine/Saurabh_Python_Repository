class Bidder:
    """
    Object of this class represents bidder in the auction. 
    """

    def __init__(self, num_users, num_rounds):
        """ Initialize bidder
        """

        self.num_users = num_users
        self.num_rounds = num_rounds
        self.bidding_round = 0

        # clearing prices
        self.user_clearing_prices = {i: [] for i in range(num_users)}
        # dictionary mapping users to number of bids won by each user
        self.user_wins = {i: 0 for i in range(num_users)}
        # dictionary mapping the number of clicks for a user
        self.user_clicks = {i: 0 for i in range(num_users)}
        # Ratio of clicks to winning bids
        self.user_clk_ratio = {i: 0. for i in range(num_users)}
        # current round
        self.crnt_round_user_id = -1

        # percentage of users to explore before starting exploitation
        self.exploration_users = .25
        # if there are a small number of users compared to the number of rounds we can explore all users
        if self.num_users / self.num_rounds <= .2:
            self.exploration_users = 1
        # bid price
        self.exploration_bid_price = 1.
        self.default_bid_price = 0.5

        # next bid for a specific user
        self.next_bid = {i: self.default_bid_price for i in range(num_users)}

        # Maximum bidding amount for high/med/low confidence bids
        self.high_bid_max = 0.99
        self.med_bid_max = 0.65
        self.low_bid_max = 0.1

        # adder value added to bids based on the last price
        self.large_adder = 0.01
        self.small_adder = 0.005

        # algorithm phase as per requirement
        self.phase = 'explore'

    def bid(self, user_id):
        """ Place a bid for a specific user
        """

        self.bidding_round += 1
        self.crnt_round_user_id = user_id
        bid_price = self.default_bid_price


        # exploit if in exploitation phase or if the user has been seen before
        if self.user_wins[self.crnt_round_user_id] > 0 or self.phase == 'exploit':
            bid_price = self.next_bid[self.crnt_round_user_id]
        else:
            # if in exploration phase then user can try to win the round
            bid_price = self.exploration_bid_price
        return bid_price

    def notify(self, auction_winner, price, clicked):
        """ Notify the bidder of auction results
        """

        # Update the list of clearing prices for current user
        self.user_clearing_prices[self.crnt_round_user_id].append(price)
        # print(f"Winning bid price  was {price}") - commented after troubleshooting

        if auction_winner:
            # update the list of total winning bids for current user
            self.user_wins[self.crnt_round_user_id] += 1

            if clicked:
                # update the number of clicks made by current user
                self.user_clicks[self.crnt_round_user_id] += 1
            # calculate the click ratio for the user by dividing user clicks with user wins.
            if self.user_wins[self.crnt_round_user_id] > 0:
                self.user_clk_ratio[self.crnt_round_user_id] = self.user_clicks[self.crnt_round_user_id] / self.user_wins[self.crnt_round_user_id]
            else:
                self.user_clk_ratio[self.crnt_round_user_id] = 0
        # Evaluate the phase based on the number of users who've been explored till this point.
        if len(self.user_wins.keys()) / self.num_users >= self.exploration_users or len(self.user_wins.keys()) == self.num_users:
            # Algorithm phase as per requirement
            self.phase = 'exploit'
