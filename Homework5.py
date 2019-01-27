import collections
import functools

from helper import key_construct


def lru_cache(maxsize=3):
    """"LRU cache decorator function"""

    def decorating_function(func):
        cache = collections.OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = key_construct(args, kwargs)

            try:
                result = cache.pop(key)
                wrapper.hits += 1
            except KeyError:
                result = func(*args, **kwargs)
                wrapper.misses += 1

                if len(cache) >= maxsize:
                    cache.popitem()

            cache[key] = result

            return result

        def cache_info():
            """LRU cache statistics"""
            print({
                'cache': dict(cache),
                'hits': wrapper.hits,
                'misses': wrapper.misses

            })

        def cache_clear():
            """Clear the cache and cache statistics"""

            cache.clear()
            wrapper.hits = wrapper.misses = 0

        wrapper.hits = wrapper.misses = 0
        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return wrapper

    return decorating_function


@lru_cache()
def main(a, b):
    return a + b


# main(20, 5)

# main.cache_info()
if __name__ == '__main__':
    main(20, 5)
    main(5, 2)
    main(10, 2)
    main(10, 20)
    main(10, 20)

    main.cache_info()

