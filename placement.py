import printer

try:
    input = raw_input
except NameError:
    pass


def menu(data):
    data["prefix"] = "[The Yard]"
    # printer.ok(data["prefix"], "You have {0} spaces open in your yard".format(compute_space(data)))
    list_yard_items(data)
    data["placing"] = True
    actions = {"list owned items": list_owned_items,
               "examine yard": list_yard_items,
               "cats": cats,
               "place toy": place,
               "place food": food,
               "leave yard": exit}
    while data["placing"]:
        printer.prompt(data["prefix"], actions.keys())
        inp = input("{.STATUS}{} What do you want to do? {.ENDC}".format(
            printer.PColors, data["prefix"], printer.PColors))
        if inp in actions:
            actions[inp](data)
            continue
        else:
            printer.invalid(data["prefix"], actions.keys())


def compute_space(data):
    return data["space"] - sum([item["size"] for item in data["yard"]])


def exit(data):
    data["placing"] = False


def list_owned_items(data):
    printer.info(data["prefix"], "You currently own a {0}".format(", and a ".join([item["name"] for item in data["items"].values() if "owned" in item["attributes"]])))


def list_yard_items(data):
    if len(data["yard"]) > 0:
        things = [(item["name"], item["occupant"]) for item in data["yard"]]
        for thing in things:
            cat = "no one"
            if thing[1]:
                try:
                    cat = thing[1][0]["name"]
                except:
                    pass
            printer.info(data["prefix"], "Your yard currently has a {0} in it, occupied by {1}".format(thing[0], cat))
    # TODO: add cat descriptions
    else:
        printer.warn(data["prefix"], "You currently have nothing in your yard, how sad")
    check_food(data)


def cats(data):
    # cats = [(obj, obj["occupant"]) for obj in data["yard"] if obj["occupied"]]
    # for cats:
    #     printer.info(data["prefix"], "{0} is playing with a {1}")
    return


def place(data):
    items_list = [item for item in data["items"].values() if "owned" in item["attributes"] and not item["in_yard"]]
    # TODO: this is ultra gross
    placable_items = {}
    for item in items_list:
        if item["size"] < 6:
            placable_items[item["name"]] = item
    printer.info(data["prefix"], "Here are the items that you can put in your yard: {0}".format(", ".join(placable_items.keys())))
    inp = input("{.STATUS}{} Which item would you like to place? {.ENDC}".format(
        printer.PColors, data["prefix"], printer.PColors))
    if inp in placable_items.keys():
        try_to_place(data, placable_items[inp])
    else:
        printer.warn(data["prefix"], "I'm sorry I didn't recognize that item")


def try_to_place(data, item):
    if sum([toy["size"] for toy in data["yard"]]) + item["size"] < data["space"]:
        data["yard"].append(item)
        item["in_yard"] = True
        printer.ok(data["prefix"], "Nice! Your yard now consists of a {0}".format(", and a ".join([toy["name"] for toy in data["yard"]])))
    else:
        printer.warn(data["prefix"], "Oops that won't fit in your yard! Would you like to remove an item?")
        offer_replace(data, item)


def offer_replace(data, item):
    yard_items = [toy["name"] for toy in data["yard"]]
    printer.info(data["prefix"], "Currently in your yard you have: a {0}".format(", and a".join(yard_items)))
    inp = input("{.STATUS}{} Would you like to replace any of the items in your yard? Which one? {.ENDC}".format(printer.PCOLORS, data["prefix"], printer.PColors))
    if inp in yard_items:
        remove_from_yard(data, inp)
        try_to_place(data, item)
    else:
        printer.warn(data["prefix"], "Sorry I don't see that item in your yard")


def remove_from_yard(data, item_name):
    # TODO: god help me
    to_remove = [item for item in data["yard"] if item["name"] == item_name]
    for item in to_remove:
        # TODO: clear cats from this
        data["yard"].remove(item)
        item["in_yard"] = False


def check_food(data):
    if data["food_remaining"] == 0:
        printer.warn(data["prefix"], "Your yard currently doesn't have any food in it! No cats will come if there's no food!")
    else:
        printer.info(data["prefix"], "Your yard currently has a {0} in it with {1} time remaining".format(data["food"], data["food_remaining"]))


def food(data):
    check_food(data)
    placable_items = {}
    for idx, item in enumerate(data["owned_food"]):
        if item["name"] not in placable_items.keys():
            placable_items[item["name"]] = [1, idx]
        else:
            placable_items[item["name"]][0] += 1
    printer.info(data["prefix"], "Here's what you can place:")
    for key in placable_items.keys():
        printer.info(data["prefix"], "A {0} ({1})".format(key, placable_items[key][0]))
    to_place = input("{.STATUS}{} Which would you like to place? (hit ENTER if none) {.ENDC}".format(printer.PColors, data["prefix"], printer.PColors))
    if to_place in placable_items.keys():
        put_food_in_yard(data, placable_items[to_place][1])


def put_food_in_yard(data, arr_idx):
    food = data["owned_food"].pop(arr_idx)
    data["food"] = food["name"]
    data["food_remaining"] = food["size"]
    printer.ok(data["prefix"], "Sweet! Your yard now has a {0} set out, and {1} of food remaining".format(data["food"], data["food_remaining"]))
