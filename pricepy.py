#For newPart Markup Price
markup_dict = {
    "5A": 0.45, "5B": 0.75, "5C": 0.66, "6Q": 0.42
}

def markup(category_code, tpp_value):
    divisor = markup_dict.get(category_code)
    if divisor:
        return (1.2 * tpp_value) / divisor
    else:
        print(f"Undefined Item Category: '{category_code}'")
        return None
