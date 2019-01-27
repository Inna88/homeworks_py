def key_construct(args, kwargs):
    key = args
    if kwargs:
        key += tuple(sorted(kwargs.items()))
    return key

