import toml


def sum(x, y):
    """Sum two numbers"""
    return x+y


def average(x, y):
    """Average two numbers"""
    return (x + y) / 2


def power(x, y):
    """Power two numbers"""
    return x ** y


def count_in_list(range: list, item):
    """Count the number of times an item appears in a list"""
    count = 0
    for i in range:
        if i == item:
            count += 1
    return count


def print_toml_data():
    """Print toml data"""
    with open('config.toml', 'r') as file:
        data = toml.load(file)

    print(data)
    print(data['section1']['key1'])  # Output: "value1"
    print(data['section2']['key3'])  # Output: True
