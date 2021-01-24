def reverse_dict(dict):
    # swap keys and values within dict and return dict
    new_dicts = {v: k for k, v in dict.items()}
    return new_dicts