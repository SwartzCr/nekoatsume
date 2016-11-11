

def cats_in_yard(data):
    yard_cats = [data["cats"][cat]
                 for cat in data["cats"].keys()
                 if data["cats"][cat]["in_yard"] is True]
    return yard_cats

def cats_not_in_yard(data):
    non_yard_cats = [data["cats"][cat]
                 for cat in data["cats"].keys()
                 if data["cats"][cat]["in_yard"] is False]
    return non_yard_cats
