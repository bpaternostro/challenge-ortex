import csv

from datetime import datetime
from collections import Counter

from . import transaction as transaction_o
from .constant import FILE_LOCATION 

class Dispacher():

    def __init__(self) -> None:
        self.transactions = []
        self.process_file()

    # creates a list with all the rows of the csv
    def process_file(self):
        try:
            with open(FILE_LOCATION, newline='', encoding='utf-8') as f:            
                reader = csv.reader(f)
                for row in reader:
                    t = transaction_o.Transaction(row)
                    self.transactions.append(t)
        except Exception as e:
            print("There were problems opening the csv file:"+str(e))
            return False
        else:        
            # removes headers
            del (self.transactions[0])
    
    # sort list
    def sort_list(self, transaction_list):
        return dict(sorted(transaction_list.items(), key=lambda item: item[1]))

    # creates a list with all the rows of the csv
    def get_exchanges(self):
        ex = []
        try:
            for row in self.transactions:
                ex.append(row.get_dict()["exchange"])
        except Exception as e:
            print("There were problems in method Dispacher.get_exchanges:"+str(e))
            return False

        return ex
    
    def get_top_exchange(self):
        ex_list = self.get_exchanges()
        if ex_list != False:
            unique = Counter(ex_list).keys() # equals to list(set(words))
            top = {}
            for ex in unique:
                transaction_per_exchange = ex_list.count(ex)
                top[ex] = transaction_per_exchange            
            # sort list
            top_exchanges = self.sort_list(top)   

        else:
            return False
        
        # after order the dictionary gets last exchange
        return list(top_exchanges.items())[-1]

    def get_highest_combined_value_eur(self):        
        aux = {}
        try:
            for d in self.transactions:
                t = d.get_dict()            
                # cheking date
                if datetime.strptime(t['tradedate'],"%Y%m%d").strftime("%m%Y") == "082017":
                    #value_converted = float(t["valueEUR"])                    
                    value_converted = int(t["valueEUR"].replace(".",""))
                    if t["companyName"] in aux:
                        aux[t["companyName"]] += value_converted
                    else:
                        aux[t["companyName"]] = value_converted
                
            highest_combined_value_eur = self.sort_list(aux)
                        
        except Exception as e:
            print("There were problems in method Dispacher.get_highest_combined_value_eur:"+str(e))
            return False

        return list(highest_combined_value_eur.items())[-1]

    def get_list_with_percentages(self, **filters):                
        try:
            # filter by tradeSignificance and year
            filter_trade_significance = [x for x in self.transactions if x.get_dict()['tradeSignificance'] == filters["trade_significance"] and str(datetime.strptime(x.get_dict()['tradedate'],"%Y%m%d").year) == filters["year"]]
            total_transactions = len(filter_trade_significance)
            totals={}
            for t in filter_trade_significance:
                month_name = datetime.strptime(t.get_dict()['tradedate'],"%Y%m%d").strftime("%b")            
                if month_name in totals:
                    totals[month_name] +=1
                else:
                    totals[month_name] =1
            final_result = {k: "{:.2%}".format(v / total_transactions) for k, v in totals.items()}
        except Exception as e:
            print("There were problems in method Dispacher.get_list_with_percentages:"+str(e))
            return False
        else:
            return final_result
    
    def generates_report(self,result):
        print("===============================================================================")
        print("Date"+"\t\t\t\t"+"Sales"+"\t\t\t"+"Month to Date")
        print("===============================================================================")

        for r in result:
            
            if r["Aditional-data"]:
                print(str(r["Date"])+"(leap year)\t\t"+str(r["Sales"])+"\t"+str(r["Month to date"])+"\n")    
            else:   
                print(str(r["Date"])+"\t\t"+str(r["Sales"])+"\t"+str(r["Month to date"])+"\n")    

            print("|Total sales for the month: "+str(r["Total"])+"|")
            print("-------------------------------------------------------------------------------")  