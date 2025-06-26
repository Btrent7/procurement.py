# Dict for Price Updates
markup_dict = {
    "2A": 0.600, "2B": 0.500, "2C": 0.700, "2F": 0.200, "2Z"
}


def markup(category_code, tpp_value):
    try:
        divisor = markup_dict[category_code]
        tpp_value = float(tpp_value)
        list_price = (1.5 * tpp_value) / divisor
        return list_price
    except KeyError:
        print(f"Undefined Item Category: '{category_code}'")
        return None
    except (ValueError, TypeError):
        print("Invalid TPP value.")
        return None
