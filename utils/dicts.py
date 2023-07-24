def get_val(collection, key, default='git'):
    if collection == {}:
        return '{}'
    else:
        return collection[key] if key else default