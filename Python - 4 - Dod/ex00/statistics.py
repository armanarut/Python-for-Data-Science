def ft_statistics(*args: any, **kwargs: any) -> None:
    """Prints the statistics of the given arguments.

    Args:
        *args: Any number of arguments.
        **kwargs: Any number of keyword arguments."""
    for key, value in kwargs.items():
        try:
            if value == 'mean':
                print("mean:", sum(args) / len(args))
            elif value == 'median':
                print("median:", sorted(args)[len(args) // 2])
            elif value == 'quartile':
                sorted_args = sorted(args)
                q1 = float(sorted_args[len(args) // 4])
                q3 = float(sorted_args[len(args) // 4 * 3])
                print("quartile:", [q1, q3])
            elif value == 'std':
                print("std:", (sum([(x - sum(args) / len(args)) ** 2
                                    for x in args]) / len(args)) ** 0.5)
            elif value == 'var':
                print("var:", sum([(x - sum(args) / len(args)) ** 2
                                   for x in args]) / len(args))
        except Exception:
            print("ERROR")
