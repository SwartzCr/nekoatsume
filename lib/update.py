"""
Update game state.

These functions are responsible for the game state updates.
"""

import time
import random


def update(data):
    """Update game data."""
    prev_start = data["start"]
    time_left = time.time() - data["start"]
    # TODO: set data["start"] to cur datetime
    while time_left > 0:
        tick(time_left, data)
        time_left = max(time_left - 60, 0)
    return data


def tick(time_left, data):
    """Pass the time."""
    if data["food_remaining"] > 0:
        new_cats(data)
        data["food_remaining"] = max(data["food_remaining"] - 1, 0)
    else:
        data["food"] = ""
    update_yard_cats(data)


def update_yard_cats(data):
    """Update status of cats in yard."""
    #TODO don't double place cats
    yard_cats = [data["cats"][cat]
                 for cat in data["cats"].keys()
                 if data["cats"][cat]["in_yard"] is True]
    for cat in yard_cats:
        cat["time_in_yard"] += 1
        if time_to_leave(cat):
            pay_up(data, cat)
            free_up_toy_cat(data, cat)


def time_to_leave(cat):
    """Decide when it's time for cat to leave yard."""
    upper_bound = random.randint(10, 20)
    lower_bound = random.randint(2, 7)
    if random.randint(lower_bound, upper_bound) < cat["time_in_yard"]:
        return True
    return False


def pay_up(data, cat):
    """Leave money for player."""
    amount = cat["time_in_yard"]
    percent = random.randint(5, 10) / 10.0
    money_to_pay = int(round(amount * percent))
    data["pending_money"].append((cat["name"], money_to_pay))


def free_up_toy_cat(data, cat):
    """Cat stops playing with toy."""
    toy = [toy for toy in data["yard"] if toy["name"] == cat["on_toy"]][0]
    cat["on_toy"] = ""
    cat["in_yard"] = False
    cat["total_time_in_yard"] += cat["time_in_yard"]
    cat["time_in_yard"] = 0
    toy["occupant"].remove(cat)
    if len(toy["occupant"]) == 0:
        toy["occupied"] = False


def new_cats(data):
    """A new cat appears."""
    open_toys = [toy for toy in data["yard"] if len(toy["occupant"]) < toy["size"]]
    random.shuffle(open_toys)
    eligible_cats = [data["cats"][cat]
                     for cat in data["cats"].keys()
                     if not data["cats"][cat]["in_yard"]]
    for cat in eligible_cats:
        if len(open_toys) == 0:
            return
        if random.random() + cat["mod"] > 1:
            toy = open_toys.pop(0)
            toy["occupied"] = True
            toy["occupant"].append(cat)
            cat["on_toy"] = toy["name"]
            cat["in_yard"] = True
            if cat["total_time_in_yard"] > 3000 and not cat["given_treasure"]:
                cat["given_treasure"] = True
                data["pending_treasures"].append((cat["name"], cat["treasure"]))
