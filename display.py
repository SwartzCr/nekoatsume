import datetime
import json
import data_constructor
import buy_menu
import printer

def store_data(data):
    with open("data.json", 'w') as f:
        json.dump(data, f)

def load_data():
    with open("data.json", 'r') as f:
        data = json.load(f)
    return data

def prep_data_on_close(data):
    cur_time = datetime.datetime.now()
    start = data["start"]
    data["food_remaining"] -= (cur_time - start).total_seconds()
    #TODO: datetimes aren't serializable
    data["start"] = cur_time.isoformat()
    store_data(data)

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
    toys = [item for item in data["items"].values() if "in_yard" in item["attributes"]]
    for toy in toys:
        second = ""
        second = toy["occupant"]
        if second == "":
            second = "no cat"
        print "You have a {0} and it is being used by {1}".format(toy, second)
    print "You have {0} open spaces on your lawn".format(6-len(toys))
    print "Your food is {0}".format(data["food_remaining"])
    return

def check_food(data):
    print "you have {0} food remaining".format(data["food_remaining"])

def print_help(data):
    print "Welcome to Neko Atsume 3000!"
    print "In this game cats come to visit you and you feed them"
    print "it's pretty cool, so you should play more"

def quit(data):
    data["want_to_play"] = False
    print "saving game!"
    prep_data_on_close(data)

def main():
    cur_time = datetime.datetime.now()
    try:
        data = load_data()
    except:
        data_constructor.build_data()
        data = load_data()
    # some code for the first time this is run
    #state = compute_interactions(data)
    # update game state
    # interaction loop
    #data["start"] = datetime.datetime.strptime(data["start"],).time()
    data["want_to_play"] = True
    actions = {"quit": quit,
               "look": desc_yard,
               "shop" : buy_menu.menu,
               "check food" : check_food,
               "help": print_help}
    while data["want_to_play"] == True:
        data["prefix"] = "[Main Menu] "
        inp = raw_input("{0} Choose an action! ".format(data["prefix"]))
        if inp in actions:
            actions[inp](data)
            continue
        else:
            printer.invalid(data["prefix"], actions.keys())

main()
