from decimal import Decimal

class IncomeIsNotNumberError(ValueError)
    pass
    

TAX_RATE = {0 : Decimal('0.1') , 10000 : Decimal('0.2') , 50000 : Decimal('0.3') , 100000 : Decimal('0.4') , 500000 : Decimal('0.5')}

def find_tax_rage(annual_income):
    result = Decimal('0.0')
    for income , rate in TAX_RATE.items():
        if annual_income > income :
            result = rate
        else:
            result = result 
    
    return result
    
    
def calculate_tax(annual_income):
    if not (isinstance(annual_income,int)) or isinstance(annual_income,float): #isinstance(object,classinfo) 判斷一個對象是否為已知的類型
        raise ValueError('Parameter "amount" has to be a number')  #關鍵字 raise 用來發起例外(exception) 
    return float(Decimal(str(annual_income)) * find_tax_rage(annual_income))
    
                                       
    