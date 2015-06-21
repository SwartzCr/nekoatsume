import printer

def menu(data):
    data["prefix"] = "[Item Shop]"
    printer.p(data["prefix"], "you have {0} silver fish and {1} gold fish to spend".format(data["s_fish"], data["g_fish"]))
    list_items(data)
    data["want_to_buy"] = True
    actions = {"buy": buy_item,
               "examine": ex_item,
               "check wallet": wallet,
               "list items": list_items,
               "leave shop": exit_buy}
    while data["want_to_buy"]:
        inp = raw_input("{0} What do you want to do? ".format(data["prefix"]))
        if inp in actions:
            actions[inp](data)
            continue
        else:
            printer.invalid(data["prefix"], actions.keys())

def list_items(data):
    catalog = [item for item in data["items"].values() if item["attributes"] == []]
    owned = [item for item in data["items"].values() if "owned" in item["attributes"]]
    for item in catalog:
        printer.p(data["prefix"], "You can buy a {0} for {1}{2}".format(item["name"], item["cost"], item["currency"]))
    if len(owned) > 0:
        printer.p(data["prefix"],"you already own a {0}".format(", and a ".join([item["name"] for item in owned])))

def exit_buy(data):
    data["want_to_buy"] = False

def wallet(data):
    printer.p(data["prefix"], "you have {0} silver fish and {1} gold fish to spend".format(data["s_fish"], data["g_fish"]))

def ex_item(data):
    items = data["items"].keys()
    printer.p(data["prefix"],"Here are the items you can see: "+", ".join(items))
    inp = raw_input("{0} which would you like to examine? ".format(data["prefix"]))
    if inp in items:
        print data["items"][inp]["description"]
    else:
        printer.p(data["prefix"],"uhhh sorry, I don't see that item")

def buy_item(data):
    buyable_items = [item for item in data["items"].keys() if data["items"][item]["attributes"] == []]
    printer.p(data["prefix"], "Here are the items up for purchase: {0}".format(", ".join(buyable_items))
    inp = raw_input("{0} Which would you like to buy? ".format(data["prefix"]))
    if inp in buyable_items:
        try_to_buy(data, inp)
    else:
        print "uhhh sorry, we don't carry that item"

def try_to_buy(data, item_name):
    item = data["items"][item_name]
    thing = item["currency"]+"_fish"
    money = data[thing]
    cost = item["cost"]
    if money < cost:
        print "I'm so sorry but you don't have enough money for that item!"
        return
    else:
        data[thing] = data[thing] - cost
        data["items"][item_name]["attributes"] = ["owned"]
        print "Ah! A splendid choice!"
        return
