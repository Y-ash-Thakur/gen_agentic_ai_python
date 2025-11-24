seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury": 
        print("luxury - Premium experience, high cost")
    case _:
        print("Invalid seat type")