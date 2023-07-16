def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f"{i+1}. {dwarves[i]}")

def summon_captain_planet(planeteer_calls):
    capitalized_calls = [call.capitalize() + '!' for call in planeteer_calls]
    return capitalized_calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheese_types = ["cheddar", "gouda", "camembert"]
    
    for snack in snacks:
        if snack in cheese_types:
            return snack
    
    return None

