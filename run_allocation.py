import argparse
import portfolio
import constants
from utils import get_generic_logger
import pprint

logger = get_generic_logger(__name__)


def run_random_portfolio(investment_opportunities, portfolio_size, validate=False):
    size = portfolio_size
    pt = portfolio.Portfolio(investment_opportunities)
    capital = min([x.capital_investment for x in pt.investment_opportunities])
    pt.get_optimal_investment_sequence(size, capital)
    if validate:
        assert pt.validate_constraints()
    logger.info("Allocation result")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(pt.allocated_opportunities)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--action",
        help="Define what you want to do.",
        choices=["simulate"],
        required=True,
    )

    parser.add_argument(
        "--investment-opportunities",
        help="Provide the number of investment opportunities to choose from.",
        dest="investment_opportunities",
        type=int, choices=range(1, constants.MAX_INVESTMENT_OPPORTUNITY_SIZE)
    )

    parser.add_argument(
        "--portfolio-size",
        help="Provide the desired portfolio size.",
        dest="portfolio_size",
        type=int, choices=range(1, constants.MAX_ALLOCATIONS)
    )

    parser.add_argument(
        "--validate",
        help="Set flag if want to run validation",
        action="store_true",
    )

    args = parser.parse_args()
    if args.action == "simulate":
        data = run_random_portfolio(args.investment_opportunities, args.portfolio_size, args.validate)