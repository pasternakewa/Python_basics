# Task is to write a function that convert an object to query string:
# to_query_string({ "bar": [ 2, 3 ], "foo": 1 }) // => "bar=2&bar=3&foo=1"


def to_query_string(data):
    pairs_list = []
    for key, value in data.items():
        if not isinstance(value, list):
            final_value = value
            pair = str(key) + "=" + str(final_value)
            pairs_list.append(pair)
        else:
            index = 0
            for _ in value:
                final_value = value[index]
                index += 1
                pair = str(key) + "=" + str(final_value)
                pairs_list.append(pair)
    pairs_list.sort()
    result = "&".join(pairs_list)
    return result
