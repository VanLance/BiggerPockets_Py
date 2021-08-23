class bigPockets:

    def __init__(self, cost, units, loan15or30):
        self.cost = cost
        self.units = units
         
        self.loan= loan15or30
        

    def totalIncome(self):
        self.income = 0
        rent = int(input(f'How much will you charge per unit?: ').lstrip("$"))* self.units
        storeIncome = int(input(f'How much will you make from storage income?: ').strip("$"))
        laundryIncome = int(input(f'How much will you make from laundry service?: ').lstrip("$"))
        miscIncome = int(input(f'How much will you make from misc income?: ').lstrip("$"))
        
        self.income += laundryIncome
        self.income +=rent
        self.income+= miscIncome
        self.income+= storeIncome

        print(f'\nThe income from this property will be : {self.income}')

    def expenses(self):
        self.spend = 0
        vacancy = self.income * .05
        print(f'\nWe recommend to save ${vacancy} for future vacancies. This is added to expenses.')
        repairs = 100 * self.units
        print(f'\nWe advise you save ${repairs} for repairs. This covers {self.units} units/units')
        answerRepair = input("If you have to save you can save half of that. Which will you choose? full/half: ")
        if answerRepair.lower == "half":
            repairs / 2
        bigRepair = 100 #Already added to spend
        bigRepairAnswer = input("\nWe strongly recommend putting away $100 for big repairs. Will you elect to do this? yes/no: ")
        if bigRepairAnswer.lower() == "yes":
            self.spend += bigRepair
        propManager = 200 #Already added to spend
        propManagerAnswer = input(f"\nWill you hire a property manager for ${propManager}? yes/no: ")
        if propManagerAnswer.lower() == "yes":
            self.spend += propManager
        tax = 150
        adjustTax = input("\nDo you live in a high/average/low cost of living area?: ")
        if adjustTax.lower() == "high":
            tax += 50
        elif adjustTax.lower() == "low":
            tax -= 50
        insurance = 100
        adjustins = input("\nWhat kind of insurance will you be using? basic/upgraded/minimum: ")
        if adjustins.lower() == "upgraded":
            insurance += 50
        elif adjustins.lower() == "minimum":
            insurance -= 30
        #Utility pay already added to spend
        utilityPay = 350
        whoUtility = input("\nWho will cover the utilities? owner/renter: ")
        if adjustTax.lower == "high":
            utilityPay += 100
        elif adjustTax.lower == "low":
            utilityPay -= 75
         #Utility pay already added to spend
        if whoUtility.lower() == "owner":
            self.spend += utilityPay
        elif whoUtility.lower() == "renter":
            self.spend += utilityPay 
        mortgage = 0
        if self.loan == 15 and self.cost < 100000: 
            mortgage += 400
        elif self.loan == 15 and (self.cost > 100000 and self.cost <= 200000):
            mortgage += 800
        elif self.loan == 15 and self.cost > 200000:
            mortgage += 2000   
        elif self.loan == 30 and self.cost < 100000:
            mortgage += 250
        elif self.loan == 30 and (self.cost > 100000 and self.cost <= 200000):
            mortgage += 520
        elif self.loan == 30 and self.cost > 200000:
            mortgage += 1300

        self.spend += vacancy
        self.spend += repairs
        self.spend += tax
        self.spend += insurance
        self.spend += mortgage

        print(f"\nRecap: You will pay ${self.spend} total. From: ${vacancy} for vacancy, ${repairs} for repairs, ${tax} for taxes, ${insurance} for insurance, and ${mortgage} for the mortgage.")
        if whoUtility.lower() == "owner":
            print(f"you are also paying ${utilityPay} for utilites.")
        print("The remaining balance is coming from big repairs and property manger fees.")
    def cashFlow(self):
        self.cashflow = self.income - self.spend
        print(f"\nIt appears your total monthly cashflow will be: ${self.cashflow}")

    def cashOnCashRe(self):
        self.totalIvestment = 0
        downPayment= int(input(f"\nHow much was your downpayment? (Typical for your cost: ${self.cost * .05}): ").lstrip("$"))
        closingCost = int(input(f"\nHow much was your closing cost? (Typical 3000): ").lstrip("$"))
        rehabBudget = 5000
        print(f"\nWe forcast you will spend 5000 on house rehabilitation.")

        self.totalIvestment += downPayment
        self.totalIvestment += closingCost
        self.totalIvestment += rehabBudget

        print(f"\nYour total investment is ${self.totalIvestment}. From ${downPayment} for downpayment, ${closingCost} for closing cost, and {rehabBudget} for the house rehab.")
        
        annualCashFlow = self.cashflow * 12
        cashOnCash = annualCashFlow / self.totalIvestment

        goals = int(input(f"\nWhat are your goals for cash return? (2-20%?): ").strip("%"))
        
        if goals <= (cashOnCash * 10):
            print(f"\nYour goals are %{goals} and your cash on cash revenue is %{cashOnCash *10}, this seems like a good investment")
        else:
            print(f"\nYour goals are %{goals} and your cash on cash revenue is %{cashOnCash * 10}, this seems like a bad investment.")



newHouse = bigPockets(1000000, 4, 30)

def run(house):
    house.totalIncome()
    house.expenses()
    house.cashFlow()
    house.cashOnCashRe()
    

run(newHouse)
            

            

   


