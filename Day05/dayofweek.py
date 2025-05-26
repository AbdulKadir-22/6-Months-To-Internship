
def dayOfTheWeek(day):
    match day:
        case "1":
            return "Today is Sunday"
        case "2":
            return "Today is Monday"
        case "3":
            return "Today is Tuesday"
        case "4":
            return "Today is Wednesday"
        case "5":
            return "Today is Thursday"
        case "6":
            return "Today is Friday"
        case "7":
            return "Today is Saturday"
        
day = input("Enter a number between 1-7: ")
print (dayOfTheWeek(day))