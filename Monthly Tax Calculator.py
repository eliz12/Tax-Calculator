

class monthly_tax_calculator(object):
    
    def __init__(self):
        
        self.tax_amount = None
    
    def monthly_tax(self, year, amount, credit):
        """
        This function returns the total monthly tax to pay
        """
        monthly_tax_amount = (self.monthly_tax_before_credit(year, amount) 
                              - self.credit(year, credit))
           
        self.tax_amount = monthly_tax_amount if monthly_tax_amount > 0 else 0
        
    
    
    def monthly_tax_before_credit(self, year, amount):
        """
        This function returns the monthly tax amount before 
        the credit
        """
        
        # tax_degrees are the relevant tax degrees by year
        tax_degrees = self.degrees_by_year(year)
        
        # case that the total amount is in the first degree
        if amount < tax_degrees[0][0]:
            return amount * tax_degrees[0][1]
        
        # all other cases    
        tax_before_credit = tax_degrees[0][0] * tax_degrees[0][1]
        for i in xrange(1, len(tax_degrees)):
            if amount > tax_degrees[i][0]:
                tax_before_credit += ((tax_degrees[i][0]
                                      -  tax_degrees[i - 1][0])
                                     * tax_degrees[i][1])
            else:
                tax_before_credit += ((amount 
                                      -  tax_degrees[i - 1][0])
                                     * tax_degrees[i][1])
                break
                
        return tax_before_credit
                
    def degrees_by_year(self, year):
        """
        This function returns the tax degrees values
        """
        if year == 2018:
            return ((6240, 0.10), (8950, 0.14), (14360, 0.20),
                    (19960, 0.31), (41530, 0.35), (53490, 0.47),
                    (999999999, 0.50))

        elif year == 2017:
            return ((6220, 0.10), (8920, 0.14), (14320, 0.20),
                    (19900, 0.31), (41410, 0.35), (53334, 0.47),
                    (999999999, 0.50))

        elif year == 2016:
            return ((5220, 0.10), (8920, 0.14), (13860, 0.21),
                    (19800, 0.31), (41410, 0.34), (66960, 0.48),
                    (999999999, 0.50))
       
        elif year == 2015:
            return ((5270, 0.10), (9000, 0.14), (13990, 0.21), 
                    (19980, 0.31), (41790, 0.34), (67560, 0.48), 
                    (999999999, 0.50))
        
        
    def credit(self, year, credit_points):
        """
        This function returns the amount of the credit
        It gets the point of the credit
        """
        if year == 2018:
            return credit_points * 216    
        elif year == 2017:
            return credit_points * 215
        elif year == 2016:
            return credit_points * 216 
        elif year == 2015:
            return credit_points * 218 
        elif year == 2014:
            return credit_points * 218 
        elif year == 2013:
            return credit_points * 218
        
            
            
            
            
def main():
    while True:
        my_tax = monthly_tax_calculator()
        print "Let's check the tax"
        print "Enter the revant year"
        year = input()
        if year not in [2015, 2016, 2017, 2018]:
            print "I can't check the tax for this year"
            continue
        print "Please enter your salary"
        salary = input()
        if type(salary) not in [int, float]:
            print "The salary should be a number"
            continue
        print "Please enter your credit points"
        credit = input()
        if type(credit) not in [int, float] :
            print "The credit should be a number"
            continue
        my_tax.monthly_tax(year, salary, credit)
        print "This is your tax: ",my_tax.tax_amount
        print "press 1 if you want to have a new calculate"
        check = input()
        if check !=1:
            break
        
main()
 

