import printer
DEMARCATION = 6

try:
    input = raw_input
except NameError:
    pass


def menu(data):
    data["prefix"] = "[Item Shop]"
    printer.shop(data["prefix"], "you have {0} silver fish and {1} gold fish to spend".format(data["s_fish"], data["g_fish"]))
    list_items(data)
    data["want_to_buy"] = True
    actions = {"buy": buy_item,
               "examine": ex_item,
               "check wallet": wallet,
               "list items": list_items,
               "leave shop": exit_buy}
    while data["want_to_buy"]:
        printer.prompt("{.SHOP}{}{.ENDC}".format(printer.PColors, data["prefix"], printer.PColors), actions.keys())
        inp = input("{.SHOP}{}{.ENDC} What do you want to do? ".format(printer.PColors, data["prefix"], printer.PColors))
        if inp in actions:
            actions[inp](data)
            continue
        else:
            printer.invalid(data["prefix"], actions.keys())


def list_items(data):
    catalog = [item for item in data["items"].values() if item["attributes"] == [] and item["size"] < DEMARCATION]
    food = [item for item in data["items"].values() if item["attributes"] == [] and item["size"] > DEMARCATION]
    owned = [item for item in data["items"].values() if "owned" in item["attributes"]]
    for item in catalog:
        printer.shop(data["prefix"], "{0} You can buy a {1} for {2}{3}".format("(toy)", item["name"], item["cost"], item["currency"]))
    for item in food:
        printer.shop(data["prefix"], "{0} You can buy a {1} for {2}{3}".format("(food)", item["name"], item["cost"], item["currency"]))
    if len(owned) > 0:
        printer.shop(data["prefix"], "you already own a {0}".format(", and a ".join([item["name"] for item in owned])))


def exit_buy(data):
    data["want_to_buy"] = False


def wallet(data):
    printer.shop(data["prefix"], "you have {0} silver fish and {1} gold fish to spend".format(data["s_fish"], data["g_fish"]))


def ex_item(data):
    items = data["items"].keys()
    printer.shop(data["prefix"], "Here are the items you can see: " + ", ".join(items))
    inp = input("{.SHOP}{}{.ENDC} which would you like to examine? ".format(printer.PColors, data["prefix"], printer.PColors))
    if inp in items:
        print("{.SHOP}{}{.ENDC}".format(printer.PColors, data["items"][inp]["description"], printer.PColors))
    else:
        printer.warn(data["prefix"], "Uhhh sorry, I don't see that item")


def buy_item(data):
    buyable_items = [item for item in data["items"].keys() if data["items"][item]["attributes"] == []]
    # printer.p(data["prefix"], "Here are the items up for purchase: {0}".format(", ".join(buyable_items)))
    inp = input("{.SHOP}{}{.ENDC} What item would you like to buy? ".format(printer.PColors, data["prefix"], printer.PColors))
    if inp in buyable_items:
        try_to_buy(data, inp)
    else:
        printer.warn(data["prefix"], "Uhhh sorry, we don't carry that item")


def try_to_buy(data, item_name):
    item = data["items"][item_name]
    currency = item["currency"] + "_fish"
    money = data[currency]
    cost = item["cost"]
    if money < cost:
        printer.fail(data["prefix"], "I'm so sorry but you don't have enough money for that item!")
        return
    else:
        data[currency] = data[currency] - cost
        if item["size"] < 6:
            data["items"][item_name]["attributes"] = ["owned"]
        else:
            data["owned_food"].append(item.copy())
        printer.success(data["prefix"], "Ah! A splendid choice!")
        return
