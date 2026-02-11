def express_as_percentage(figure, digits = 2):
    return str(round(figure, digits)) + '%'

def express_as_dollars(figure):
    formatted_string = f"{figure:,.2f}"
    return '$'+formatted_string

def get_months():
    month_array = [
        { 'mo_name': 'January', 'mo_num': 0 },
        { 'mo_name': 'February', 'mo_num': 1 },
        { 'mo_name': 'March', 'mo_num': 2 },
        { 'mo_name': 'April', 'mo_num': 3 },
        { 'mo_name': 'May', 'mo_num': 4 },
        { 'mo_name': 'June', 'mo_num': 5 },
        { 'mo_name': 'July', 'mo_num': 6 },
        { 'mo_name': 'August', 'mo_num': 7 },
        { 'mo_name': 'September', 'mo_num': 8 },
        { 'mo_name': 'October', 'mo_num': 9 },
        { 'mo_name': 'November', 'mo_num': 10 },
        { 'mo_name': 'December', 'mo_num': 11 },
    ]
    return month_array

def get_name_of_month(monthNum):
    match monthNum:
        case 0:
            return 'January'
        case '0':
            return 'January'
        case 1:
            return 'February'
        case 2:
            return 'March'
        case 3:
            return 'April'
        case 4:
            return 'May'
        case 5:
            return 'June'
        case 6:
            return 'July'
        case 7:
            return 'August'
        case 8:
            return 'September'
        case 9:
            return 'October'
        case 10:
            return 'November'
        case 11:
            return 'December'
        case _:
            return 'Not a Month'
    