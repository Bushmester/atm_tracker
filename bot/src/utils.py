def concatenate_dicts(*dict_list: list) -> dict:
    base = {}
    for dict_obj in dict_list:
        base.update(dict_obj)
    return base
