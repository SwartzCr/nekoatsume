import json
import datetime

def store_data(data):
    with open("data.json", 'w') as f:
        json.dump(data, f)

def build_data():
    #TODO fid a way to ge time
    #cur_time = datetime.datetime.now().time().isoformat()
    cur_time = 0
    data = {}
    data["items"] = {}
    data["yard"] = []
    data["space"] = 6
    data["food_remaining"] = 0
    data["prefix"] = ""
    data["g_fish"] = 10
    data["s_fish"] = 300
    data["seen_cats"] = []
    data["start"] = cur_time
    build_items(data)
    store_data(data)

def make_item(name, cost, cur, size, desc):
    return {"cost": cost,
            "currency": cur,
            "description": desc,
            "attributes": [],
            "occupant": [],
            "in_yard": False,
            "size": size,
            "name": name}

def build_items(data):
    data["items"]["ball of yarn"] = make_item("ball of yarn", 10, "s", 1, "a ball of yarn, it's red!")
    data["items"]["scratching post"] = make_item("scratching post", 5, "g", 1, "A post for your cats to scratch!")
