x = [1,3,2,7,8,1]

def evens(sort_list):
    y = []
    for i in sort_list:
        if i % 2 == 0:
            y.append(i)
    return y

print evens(x)

def add(add_list):
    y = 0
    for i in add_list:
        y += i

    return y

print add(x)

def filter(filter_list, filters='none'):
    y = []
    if filters == "even":
        for i in filter_list:
            if i % 2 == 0:
                y.append(i)
        return y

    elif filters == "odd":
        for i in filter_list:
            if i % 2 != 0:
                y.append(i)
        return y

    else:
        return filter_list

def summarise_filter(filter_list, filters="none"):
    x = 0

    if filters == "even":
        y = filter(filter_list, "even")

    elif filters == "odd":
        y = filter(filter_list, "odd")

    else:
        y = filter(filter_list)

    for i in y:
        x += i

    return x

summarise_filter(x)