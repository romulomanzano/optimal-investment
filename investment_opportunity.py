import random
import datetime
import constants
from collections import namedtuple

class InvestmentOpportunity(namedtuple('Investment', 'capital_investment profit')):
    
    @staticmethod
    def generate_random_opportunity():
        random.seed(datetime.datetime.now().timestamp())
        cap_investment = random.randint(0,constants.MAX_CAPITAL_INVESTMENT) +1
        profit = random.randint(0,constants.MAX_PROFIT + 1)
        investment = InvestmentOpportunity(capital_investment=cap_investment, profit=profit)
        return investment
    