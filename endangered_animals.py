def endangered_animals(animal_dict):
    result = ""
    for animal, population in animal_dict.items():
        result += "{}".format(animal) + "\n"
    return result

print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))
# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger
