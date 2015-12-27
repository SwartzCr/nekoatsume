import json
import time
import datetime


def store_data(data):
    with open("data.json", 'w') as f:
        json.dump(data, f)


def build_data():
    cur_time = time.time()
    data = {}
    data["items"] = {}
    data["cats"] = {}
    data["yard"] = []
    data["owned_food"] = []
    data["space"] = 6
    data["food_remaining"] = 0
    data["food"] = ""
    data["prefix"] = ""
    data["g_fish"] = 10
    data["s_fish"] = 300
    data["seen_cats"] = []
    data["start"] = cur_time
    data["pending_money"] = []
    build_items(data)
    build_cats(data)
    store_data(data)


def make_item(name, cost, cur, size, desc):
    return {"cost": cost,
            "currency": cur,
            "description": desc,
            "attributes": [],
            "occupant": [],
            "occupied": False,
            "in_yard": False,
            "size": size,
            "name": name}


# TODO: Keep data in JSON file to simplify this function
#       Consider something like Marshmallow for deserialization into app objs
#       https://marshmallow.readthedocs.org/en/latest/
def build_items(data):
    data["items"]["rubber ball"] = make_item("rubber ball", 5, "s", 1, "a small bright orange rubber ball, it's squishy and squeaky!")
    data["items"]["sparkle ball"] = make_item("sparkle ball", 5, "g", 1, "a small clear rubber ball filled with colorful sparkling glitter!")
    data["items"]["ball of yarn"] = make_item("ball of yarn", 10, "s", 1, "a ball of yarn, it's red!")
    data["items"]["fancy ball of yarn"] = make_item("fancy ball of yarn", 15, "g", 1, "a fancy ball of yarn, it's red, blue, and green with shimmering silver threads too!")
    data["items"]["tennis ball"] = make_item("tennis ball", 25, "s", 1, "a tennis ball, it's fuzzy and bright yellow!")
    data["items"]["paper bag"] = make_item("paper bag", 20, "s", 1, "A paper grocery bag, makes lots of crinkling noises!")
    data["items"]["scratching post"] = make_item("scratching post", 5, "g", 1, "A nice post for your cats to scratch!")
    data["items"]["fancy scratching post"] = make_item("fancy scratching post", 15, "g", 1, "A fancy deluxe hardwood and faux leather scratching post!")
    data["items"]["fishbowl"] = make_item("fishbowl", 10, "g", 1, "A small fishbowl with a cute goldfish swimming inside!")
    data["items"]["small condo"] = make_item("small condo", 75, "s", 1, "A small sized, partially carpeted kitty condo with room for up to 3 cats!")
    data["items"]["medium condo"] = make_item("medium condo", 150, "s", 2, "A medium sized kitty condo with full carpeting and room for up to 5 cats!")
    data["items"]["large condo"] = make_item("large condo", 50, "g", 2, "A large sized kitty condo with luxurious berber carpeting, hand stitching, and room for up to 7 cats!")
    data["items"]["bag of catnip"] = make_item("bag of catnip", 7, "g", 1, "A small bag of catnip, the smell drives cats wild!")
    data["items"]["plain pillow"] = make_item("plain pillow", 30, "s", 1, "A small plain pillow, it's soft and blue!")
    data["items"]["tie-dye pillow"] = make_item("tie-dye pillow", 15, "g", 1, "A thick fluffy pillow made from very soft tie-dyed fleece!")
    data["items"]["plastic bucket"] = make_item("plastic bucket", 20, "s", 1, "A small green plastic bucket with white handle, I has a bucket!")
    data["items"]["cereal box"] = make_item("cereal box", 15, "s", 1, "An empty box of Cinnamon Toasty Purrs cereal!")
    data["items"]["fruit box"] = make_item("fruit box", 75, "s", 1, "A small cardboard fruit box, if I fits I sits!")
    data["items"]["large box"] = make_item("large box", 30, "g", 2, "A large cardboard box that originally held an appliance but now has room to hold up to 4 cats!")
    data["items"]["butterfly toy"] = make_item("butterfly toy", 15, "g", 1, "A cute butterfly toy suspended from a string on a long stick, flying fun!")
    data["items"]["robotic laser pointer"] = make_item("robotic laser pointer", 125, "g", 1, "A little robotic arm with attached laser pointer, all time favorite!")
    data["items"]["rainbow umbrella"] = make_item("rainbow umbrella", 25, "g", 2, "A large rainbow patterned umbrella with room for up to 5 cats!")
    data["items"]["plain umbrella"] = make_item("plain umbrella", 250, "s", 2, "A large plain umbrella with room for up to 4 cats, it's bright yellow!")
    data["items"]["plush froggy"] = make_item("plush froggy", 75, "s", 1, "A cute green plush frog toy that squeaks when squeezed!")
    data["items"]["bowl of dry food"] = make_item("bowl of dry food", 10, "s", 300, "Basic dry cat food, it is very crunchy and plain.")
    data["items"]["can of wet food"] = make_item("can of wet food", 2, "g", 300, "Basic wet cat food, it has a pungent smell!")
    data["items"]["can of fancy food"] = make_item("can of fancy food", 5, "g", 300, "Artisanally hand-crafted fair trade organic cat food, mmmm!")


def make_cat(name, desc, treasure, mod):
    return {"name": name,
            "desc": desc,
            "time_in_yard": 0,
            "on_toy": {},
            "in_yard": False,
            "treasure": treasure,
            "given_treasure": False,
            "mod": mod}


# TODO: Keep data in JSON file to simplify this function
#       Consider something like Marshmallow for deserialization into app objs
#       https://marshmallow.readthedocs.org/en/latest/
#
# TODO: should this be named birth_cats? ;)
def build_cats(data):
    data["cats"]["Gordo"] = make_cat("Gordo", "The most fucking annoying cat, he's always eating your food", "It's a useless piece of wood because Gordo sucks", 0.1)
    data["cats"]["Pukka"] = make_cat("Pukka", "Pukka is a white shorthair with cream splotches and green eyes; she loves to chase lasers and surf", "It's a block of surf wax", 0.1)
    data["cats"]["Peebles"] = make_cat("Peebles", "Peebles is a black and white shorthair with blue eyes; he likes death metal music and piles of catnip", "It's a tortoise shell guitar pick", 0.1)
    data["cats"]["Tarawa"] = make_cat("Tarawa", "Tarawa is a gray longhair with white streaks and gray eyes; she likes relaxing and chasing birds", "It's a Blue Jay feather", 0.1)
    data["cats"]["Felix"] = make_cat("Felix", "Felix is an orange and white shorthair tabby with yellow eyes; he is very mellow and mostly meditates all day long", "It's a Buddha incense holder", 0.1)
