import datetime
import json
import data_constructor
import buy_menu, placement
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

# this should be remade but where we just take the time diff
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
    toys = [item for item in data["items"].values() if "in_yard" in item["attributes"]]
    for toy in toys:
        occupants = toy["occupant"]
        if len(occupants) == 0:
            print "You have a {0} and it isn't being used".format(toy)
        else:
            print "You have a {0} and it is being used by {1}".format(toy, ", ".format(occupants))
    print "You have {0} open spaces on your lawn".format(6-len(toys))

def check_status(data):
    desc_yard(data)
    check_food(data)

def check_food(data):
    print "you have {0} minutes of food remaining".format(data["food_remaining"])

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
               "look": check_status,
               "shop" : buy_menu.menu,
               "place items": placement.menu,
               "check food" : check_food,
               "help": print_help}
    data["prefix"] = "[Main Menu]"
    check_status(data)
    while data["want_to_play"] == True:
        data["prefix"] = "[Main Menu]"
        inp = raw_input("{0} Choose an action! ".format(data["prefix"]))
        if inp in actions:
            actions[inp](data)
            continue
        else:
            printer.invalid(data["prefix"], actions.keys())

main()
