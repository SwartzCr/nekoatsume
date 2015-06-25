import printer

def menu(data):
    data["prefix"] = "[Placement]"
    printer.p(data["prefix"], "You have {0} spaces open in your yard".format(compute_space(data)))
    data["placing"] = True
    actions = {"list owned items": list_owned_items,
               "list yard items": list_yard_items,
               "place item": place,
               "leave yard": exit}
    while data["placing"]:
        printer.prompt(data["prefix"], actions.keys())
        inp = raw_input("{0} What do you want to do? ".format(data["prefix"]))
        if inp in actions:
            actions[inp](data)
            continue
        else:
            printer.invalid(data["prefix"], actions.keys())


def compute_space(data):
    return  data["space"] - sum([item["size"] for item in data["yard"]])

def exit(data):
    data["placing"] = False

def list_owned_items(data):
    printer.p(data["prefix"], "You currently own a {0}".format(", and a ".join([item["name"] for item in data["items"].values() if "owned" in item["attributes"]])))

def list_yard_items(data):
    if len(data["yard"]) > 0:
        printer.p(data["prefix"], "Your yard currently has a {0} in it".format(", and a ".join([item["name"] for item in data["yard"]])))
    else:
        printer.p(data["prefix"], "You currently have nothing in your yard, how sad")

def place(data):
    items_list = [item for item in data["items"].values() if "owned" in item["attributes"] and not item["in_yard"]]
    #TODO this is ultra gross
    placable_items = {}
    for item in items_list:
        placable_items[item["name"]] = item
    printer.p(data["prefix"], "Here are the items that you can put in your yard: {0}".format(", ".join(placable_items.keys())))
    inp = raw_input("{0} Which item would you like to place? ".format(data["prefix"]))
    if inp in placable_items.keys():
        try_to_place(data, placable_items[inp])
    else:
        printer.p(data["prefix"], "I'm sorry I didn't recognize that item")

def try_to_place(data, item):
    if sum([toy["size"] for toy in data["yard"]]) + item["size"] < data["space"]:
        data["yard"].append(item)
        item["in_yard"] = True
        printer.p(data["prefix"], "Nice! Your yard now consists of a {0}".format(", and a ".join([toy["name"] for toy in data["yard"]])))
    else:
        printer.p(data["prefix"], "Oops that won't fit in your yard! Would you like to remove an item?")
        offer_replace(data, item)

def offer_replace(data, item):
    yard_items = [toy["name"] for toy in data["yard"]]
    printer.p(data["prefix"], "Currently in your yard you have: a {0}".format(", and a".join(yard_items)))
    inp = raw_input("{0} Would you like to replace any of the items in your yard? Which one? ".format(data["prefix"]))
    if inp in yard_items:
        remove_from_yard(data, inp)
        try_to_place(data, item)
    else:
        printer.p(data["prefix"], "Sorry I don't see that item in your yard")

def remove_from_yard(data, item_name):
#TODO god help me
    to_remove = [item for item in data["yard"] if item["name"] == item_name]
    for item in to_remove:
       #TODO clear cats from this
       data["yard"].remove(item)
       item["in_yard"] = False


