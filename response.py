from random import choice
from locations import locations # Import dictionary from locations.py

# Pre-generated message list
Reply_List = [
    "{} seems like a great option for today!",
    "How about checking out {}? It's a great place to chill!",
    "{} could be fun spot to rest and relax!",
    "I heard {} is a great place to go!",
    "Maybe try {}? It's a popular choice for some people!",
    "If you're looking for something to just lepak, {} is one of the recommended picks!",
    "{} sounds like a cozy place to just chill!",
    "I would suggest going to {}!",
    "{} is a good spot!",
    "{} is a great place to relax!"
]


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return 'Well, you\'re awfully quiet....'
    elif lowered == 'lepaksg':
        return 'Hi there! Which town are you planning to lepak at?'



    # Check if user input contains any known towns
    for town, categories in locations.items():
        if town in lowered:
            category = choice(list(categories.keys())) # A spot is chosen at random depending on the selected town
            place = choice(categories[category])
            message = choice(Reply_List).format(place) # Format with a pre-written reply
            return message
    
    return choice(["Im not sure where that is, my developer half fuck my code so my process is a bit limited.",
                   "Hmm, I don't have info on that, but let me know if I should add it!"])