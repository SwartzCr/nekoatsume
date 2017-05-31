"""
Update game state.

These functions are responsible for the game state updates.
"""

import time
import random
from query import cats_in_yard, cats_not_in_yard

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
    eligable_cats = cats_not_in_yard(data)
    update_yard_cats(data)
    if data["food"]:
        for cat in eligable_cats:
            if roll_to_enter(cat):
                toy = pick_toy(data, cat)
                if not toy:
                    continue
                if is_open(toy):
                    join_toy(data, cat, toy)
                else:
                    try_push(data, cat, toy)
        reduce_food(data)

def reduce_food(data):
    if data["food_remaining"] > 0:
        data["food_remaining"] = max(data["food_remaining"] - 1, 0)
        if data["food_remaining"] == 0:
            data["food"] = ""
    else:
        data["food"] = ""

def roll_to_enter(cat):
    if random.random() < cat["entry_chance"]:
        return True
    return False

def pick_toy(data, cat):
    yard_toys = [toy for toy in data["yard"]]
    fav_toy = [toy for toy in yard_toys if toy["name"] == cat["fav_toy"]]
    if cat["exclusive"]:
        if fav_toy:
            return fav_toy[0]
        else:
            return None
    return random.choice(yard_toys)

def is_open(toy):
    return len(toy["occupant"]) < toy["size"]

def join_toy(data, cat, toy):
    toy["occupied"] = True
    toy["occupant"].append(cat["name"])
    cat["on_toy"] = toy["name"]
    cat["in_yard"] = True
    if cat["total_time_in_yard"] > 3000 and not cat["given_treasure"]:
        cat["given_treasure"] = True
        data["pending_treasures"].append((cat["name"], cat["treasure"]))

def try_push(data, cat, toy):
    for occupant in toy["occupant"]:
        if data["cats"][occupant]["strength"] < cat["strength"]:
            remove_cat(data, data["cats"][occupant], toy)
            join_toy(data, cat, toy)
            return

def remove_cat(data, cat, toy):
    toy["occupant"].remove(cat["name"])
    pay_up(data, cat)
    cat["on_toy"] = ""
    cat["in_yard"] = False
    cat["total_time_in_yard"] += cat["time_in_yard"]
    cat["time_in_yard"] = 0

def update_yard_cats(data):
    """Update status of cats in yard."""
    yard_cats = cats_in_yard(data)
    for cat in yard_cats:
        cat["time_in_yard"] += 1
        if time_to_leave(cat):
            free_up_toy_cat(data, cat)


def time_to_leave(cat):
    """Decide when it's time for cat to leave yard."""
    upper_bound = random.randint(10, 20)
    lower_bound = random.randint(2, 7)
    if random.randint(lower_bound, upper_bound) + cat["time_in_yard"] > cat["time_limit"]:
        return True
    return False


def pay_up(data, cat):
    """Leave money for player."""
    #TODO add cat modifier
    amount = cat["time_in_yard"]
    percent = random.randint(5, 10) / 10.0
    money_to_pay = int(round(amount * percent))
    data["pending_money"].append((cat["name"], money_to_pay, "g" if (random.randint(1, 30) == 1) else "s"))


def free_up_toy_cat(data, cat):
    """Cat stops playing with toy."""
    toy = [toy for toy in data["yard"] if toy["name"] == cat["on_toy"]][0]
    remove_cat(data, cat, toy)
    if len(toy["occupant"]) == 0:
        toy["occupied"] = False


def new_cats(data):
    """A new cat appears."""
    open_toys = [toy for toy in data["yard"] if len(toy["occupant"]) < toy["size"]]
    random.shuffle(open_toys)
    eligible_cats = cats_in_yard(data)
    for cat in eligible_cats:
        if len(open_toys) == 0:
            return
        if random.random() + cat["mod"] > 1:
            toy = open_toys.pop(0)
            toy["occupied"] = True
            toy["occupant"].append(cat["name"])
            cat["on_toy"] = toy["name"]
            cat["in_yard"] = True
            if cat["total_time_in_yard"] > 3000 and not cat["given_treasure"]:
                cat["given_treasure"] = True
                data["pending_treasures"].append((cat["name"], cat["treasure"]))
