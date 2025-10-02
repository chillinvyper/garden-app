def season_check(season):
    '''Checks input and adjusts advice based on input or displays error'''
    while True:
        if season.lower() == "summer":
            season = "Water your plants regularly and provide some shade.\n"
            return season

        if season.lower() == "winter":
            season = "Protect your plants from frost with covers.\n"
            return season

        if season.lower() == 'autumn' or season.lower() == 'spring':
            season = "No advice for this season.\n"
            return season

        else:
            print("sorry that is not a valid input, please try again")
            season = input("what season do you need advice for? ")


def plant_type_check(plant_type):
    '''checks the user input for plant type then adds it to the
    advice variable '''
    if plant_type.lower() == "flower":
        plant_advice = "Use fertiliser to encourage blooms."

    elif plant_type.lower() == "vegetable":
        plant_advice = "Keep an eye out for pests!"

    else:
        plant_advice = "No advice for this type of plant."

    return plant_advice


# Collects and prints all the results after the input checks
season_advice = input("what season do you need advice for? ")
ADVICE = season_check(season_advice)

plant_type = input("What type of plant are you are you growing? flower or vegetable ")
ADVICE += plant_type_check(plant_type)
print(ADVICE)

# Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
