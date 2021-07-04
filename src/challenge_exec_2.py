from datetime import datetime

from core import dispacher as dispa_o

'''
This task is to fix this code to write out a simple monthly report. The report should look professional.
The aim of the exercise is to:
- Ensure that the code works as specified including date formats
- Make sure the code will work correctly for any month
- Make sure the code is efficient
- Ensure adherence to PEP-8 and good coding standards for readability
- No need to add comments unless you wish to
- No need to add features to improve the output, but it should be sensible given the constraints of the exercise.
Code should display a dummy sales report
'''
### Do not change anything in the section below, it is just setting up some sample data
# test_data is a dictionary keyed on day number containing the date and sales figures for that day
month = "02"
test_data = {f"{x}": {"date": datetime.strptime(f"2021{month}{x:02d}", "%Y%m%d"),
                      'sales': float(x ** 2 / 7)} for x in range(1, 29)}

### Do not change anything in the section above, it is just setting up some sample data'''

# - BP - Fixing the index to something more dinamic
# start=test_data[0]
# end=test_data[27]
start = test_data[list(test_data)[0]]
end = test_data[list(test_data)[-1]]

def DateToDisplayDate(date):
    # E.g. Monday 8th February, 2021
    return (f"""{date.strftime("%a")} {date.strftime("%d")}th {date.strftime("%B")}, {date.strftime("%Y")}""")    

#start["date"] = DateToDisplayDate(start["date"])
#end["date"] = DateToDisplayDate(end["date"])
# I created 2 variables to avoid changing the dict
aux_start = DateToDisplayDate(start["date"])
aux_end = DateToDisplayDate(end["date"])

# - BP - I did some changes in order to make more readable this lines
# print("Sales Report\nReport start date: " + start["date"] + "| Starting value: " + str(start["sales"]) + "\nReport end date: " + end["date"] + "\nTotal sales: " + str(end["sales"]) + "\n")
print("Sales Report\nReport start date: " + str(aux_start) + "| Starting value: " + str(aux_start) + "\nReport end date: " + str(aux_end) + ", total sales: " + str(aux_end) + "\n")

# - BP - changing to 0
#total=None
total=0

# - BP - fix adding method .items()
result=[]
for k, v in test_data.items():        
    leap_year=False    
    # - BP - fix - adding a value to the variable month    
    month=v["date"].strftime("%m")

    # - BP - I've changed the operator
    #if  month is "2" and k is "29":
    if  month == "2" and k == "29":
        leap_year=True # Must be displayed if data is for a leap year

    aux={
        "Date":DateToDisplayDate(v['date']),
        "Sales":v['sales'],
        "Month to date":"${t}".format(t=total),
        "Total":v['sales']+total,
        "Aditional-data":leap_year
    }
    
    total=v['sales']+total

    result.append(aux)

dispa=dispa_o.Dispacher()
dispa.generates_report(result)
  