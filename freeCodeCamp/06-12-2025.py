def format_date(date_string):
    date = date_string.split(" ")

    #Month : 
    m = ['January',"February","March","April","May","June","July","August","September","October","November","December"]

    month = str(m.index(date[0])+1)
    if len(month) != 2:
        month = "0" + month

    #Day :
    day = date[1][:-1]
    if len(day) != 2:
        day = "0" + day
    
    new_date = date[2] +"-"+month+"-"+day

    return new_date

print(format_date("January 1, 2000"))
print(format_date("December 6, 2025"))
print(format_date("November 11, 1111"))
print(format_date("September 7, 512"))
print(format_date("May 4, 1950"))
print(format_date("February 29, 1992"))