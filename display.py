import buy_menu
import data_constructor
import datetime
import json
import placement
import printer
import sys
import time
import update


def store_data(data):
    with open("data.json", 'w') as f:
        json.dump(data, f)


def load_data():
    with open("data.json", 'r') as f:
        data = json.load(f)
    return data


def prep_data_on_close(data):
    store_data(data)


# TODO: this should be remade but where we just take the time diff
# and do itterative deletions to it until we get to some minimal
# amt and store it, rather than this time left precomputation
def compute_interactions(data):
    cur_time = datetime.datetime.now()
    time_since = (cur_time - data["start"]).total_seconds()
    if time_since < data["food_remaining"]:
        data["food_remaining"] -= time_since
        return compute_with_food(time_since)
    else:
        time_w_food = data["food_remaining"]
        time_wo_food = time_since - time_w_food
        data["food_remaining"] = 0
        return compute_with_food(time_w_food)
    return compute


def desc_yard(data):
    toys = [item for item in data["yard"]]
    printer.p(data["prefix"], "You have {0} total spaces on your lawn".format(6))
    for toy in toys:
        occupants = toy["occupant"] or ["no one"]
        printer.p(data["prefix"], "You have a {0} and it is being used by {1}".format(toy["name"], ", and ".join(occupants)))
    # TODO: have this reflect size


def check_status(data):
    # desc_yard(data)
    placement.list_yard_items(data)
    check_food(data)


def check_food(data):
    if data["food"]:
        printer.p(data["prefix"], "You have a {0} in your yard with {1} minutes of food remaining".format(data["food"], data["food_remaining"]))
    else:
        printer.p(data["prefix"], "Oh no! There's no food in your yard! No cats will show up if you don't have any food!")


def collect_money(data):
    if len(data["pending_money"]) == 0:
        printer.p("[$$$$$$]", "Sorry, no cats have left you anything")
        return
    for i in range(len(data["pending_money"])):
        money = data["pending_money"].pop()
        printer.p("[$$$$$$]", "Yes! {0} left you {1} fish!".format(money[0], str(money[1])))
        data["s_fish"] += money[1]


def print_help(data):
    temp = "[Help!]"
    printer.p(temp, "Welcome to Neko Atsume!")
    printer.p(temp, "In this game cats come to visit you and you feed them")
    printer.p(temp, "it's pretty cool, so you should play more")


def quit(data):
    data["want_to_play"] = False
    printer.p("[Goodbye!]", "Saving game! See you later!")
    prep_data_on_close(data)


def main():
    try:
        data = load_data()
        data = update.update(data)
    except:
        print sys.exc_info()[0]
        data_constructor.build_data()
        data = load_data()
    data["want_to_play"] = True
    data["start"] = time.time()
    actions = {"quit": quit,
               "look": check_status,
               "shop": buy_menu.menu,
               "yard": placement.menu,
               "collect money": collect_money,
               "check food": check_food,
               "help": print_help}
    data["prefix"] = "[Welcome!]"
    check_status(data)
    data["prefix"] = "[Main Menu]"
    while data["want_to_play"] is True:
        data["prefix"] = "[Main Menu]"
        printer.prompt(data["prefix"], actions.keys())
        inp = raw_input("{0} Choose an action! ".format(data["prefix"]))
        if inp in actions:
            actions[inp](data)
            continue
        else:
            printer.invalid(data["prefix"], actions.keys())

main()
