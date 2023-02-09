import pytest
import random
import datetime
import portfolio
import constants

def test_10_portfolios():
    random.seed(datetime.datetime.now().timestamp())
    for n in range(10):
        size = random.randint(0, constants.MAX_ALLOCATIONS//2)
        pt = portfolio.Portfolio(constants.MAX_INVESTMENT_OPPORTUNITY_SIZE//2)
        capital = min([x.capital_investment for x in pt.investment_opportunities])
        pt.get_optimal_investment_sequence(size, capital)
        assert pt.validate_constraints()
