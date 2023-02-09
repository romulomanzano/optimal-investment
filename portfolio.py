from investment_opportunity import InvestmentOpportunity
import constants

class Portfolio:
    investment_opportunities : list
    unallocated_opportunities : list
    allocated_opportunities : list
    seed_capital: int
    final_capital: int

    def __init__(self,  market_size=constants.MAX_INVESTMENT_OPPORTUNITY_SIZE):
        #generate a list of X investment opportunities
        opportunities = [InvestmentOpportunity.generate_random_opportunity() for _ in range(market_size) ]
        #only need to sort once, later on can simply filter
        self.investment_opportunities = sorted(opportunities, key=lambda x: x.profit, reverse=True)
        self.unallocated_opportunities = list(self.investment_opportunities)
        self.allocated_opportunities = []
        
    
    def most_profitable_opportunity_given_capital(self, available_capital):
        #get index and value
        for idx, x in enumerate(self.unallocated_opportunities):
            if x.capital_investment <= available_capital:
                return idx, x
        return None


    def _reset_allocation(self):
        self.unallocated_opportunities = list(self.investment_opportunities)
        self.allocated_opportunities = []
        self.seed_capital = None
        

    def get_optimal_investment_sequence(self, size, seed_capital):
        """
        return optimal investment sequence given started capital and desired sice
        """
        self._reset_allocation()
        size = min([size,len(self.investment_opportunities)])
        self.seed_capital = seed_capital
        capital = seed_capital
        for n in range(1,size,1):
            #small optimization if remaining capital is sufficient for all remaining opportunity, select top N
            if self.unallocated_opportunities[size-n].capital_investment <= capital:
                self.allocated_opportunities = self.allocated_opportunities + list(self.unallocated_opportunities[:size-n+1])
                #add all the profit
                capital += sum([x.profit for x in self.unallocated_opportunities[:size-n+1]])
                del self.unallocated_opportunities[:size-n]
                break
            unallocated_index, top_opportunity = self.most_profitable_opportunity_given_capital(capital)
            del self.unallocated_opportunities[unallocated_index]
            self.allocated_opportunities.append(top_opportunity)
            capital += top_opportunity.profit
        self.final_capital = capital

    def validate_constraints(self):
        """
        Normally would put something like this in a test case and check using pytest
        only run if needed
        """
        failed = False
        capital = self.seed_capital
        for al in self.allocated_opportunities:
            failed = al.capital_investment > capital
            if failed:
                pass
            capital += al.profit
        return not failed
