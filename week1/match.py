name = input('WHat is your name?')

match name:
    case "ajay":
        print("Hello ajay")
    case "manu":
        print("Hello manu")
    case _:
        print("Hello unknown")