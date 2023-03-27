
"Write a function that enables you to determine which day is the day after 123456 days from today."



def day_determiner(today, count): # "today" can take an integer  value from 0 to 6 (monday=0,tuesday=1,...sunday=6)

    list_of_days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

    new_list = dict(enumerate(list_of_days))

    remainder = count%7

    result = (today + remainder)%7

    return new_list[result]


test = day_determiner(6, 123456)
print(test)
#output : thursday



