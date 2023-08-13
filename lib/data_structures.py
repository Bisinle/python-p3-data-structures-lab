spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    food_names = [food["name"] for food in spicy_foods]
    return food_names


def get_spiciest_foods(spicy_foods):
    spicy_foods_dict_list = [
        spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5
    ]
    return spicy_foods_dict_list


def print_spicy_foods(spicy_foods):
    spicy_food_list = list()
    for spicy_food in spicy_foods:
        spicy_food_list.append(
            f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {spicy_food['heat_level'] *'🌶'}"
        )
    for spicy_food in spicy_food_list:
        print(spicy_food)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food


def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            print(
                f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {spicy_food['heat_level'] *'🌶'}"
            )


def get_average_heat_level(spicy_foods):
    heat_level_list = [spicy_food["heat_level"] for spicy_food in spicy_foods]
    heat_level_ave = sum(heat_level_list) / len(heat_level_list)
    return int(heat_level_ave)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
