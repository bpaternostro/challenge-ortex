from core import dispacher as dispa_o

t = dispa_o.Dispacher()

# What Exchange has had the most transactions in the file? 
result_1 = t.get_top_exchange()
if result_1 != False:
    point_1="Top exchange is '{ex}' with {x} transactions".format(ex = result_1[0], x = result_1[1])
    print(point_1)

# In August 2017, which companyName had the highest combined valueEUR?
result_2 = t.get_highest_combined_value_eur()
if result_2 != False:
    point_2="Highest combined valueEUR is '{}' with EUR {:0,.2f}".format(result_2[0],result_2[1])
    print(point_2)

# For 2017, only considering transactions with tradeSignificance 3, what is the percentage of transactions per month?
result_3 = t.get_list_with_percentages(year="2017", trade_significance="3")
if result_3 != False:    
    print(result_3)


        


