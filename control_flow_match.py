while True:
    day = input('write down your day'.lower())
    match day :
        case "mon": print(day,' is not included!')
        case "tue": print(day,' is not included!')
        case "wed": print(day,' is not included!')
        case "thu": print(day,' is not included!')
        case "fri": print(day,' is not included!')
        case "sat": print(day,' weekend, weekend not included!')
        case "sun": print(day,' weekend, weekend not included!')
        case _: print(day, ' is invalid input')

