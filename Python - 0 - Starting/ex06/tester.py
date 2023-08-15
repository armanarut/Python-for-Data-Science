from ft_filter import ft_filter


def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u', 'k']
    if (variable in letters):
        return True
    else:
        return False


sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)

filtered = ft_filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)
