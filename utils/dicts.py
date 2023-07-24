def get_val(collection, key, default='git'):
    if collection == {}:
        return '{}'
    elif key in collection.keys():
        return collection[key]
    else:
        return default