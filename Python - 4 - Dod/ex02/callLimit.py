def callLimit(limit: int):
    """Decorator that limits the number of calls to a function

    Args:
        limit (int): The maximum number of calls to the function"""
    count = 0

    def callLimiter(function):
        """Decorator that limits the number of calls to a function

        Args:
            function (function): The function to limit the number of calls"""

        def limit_function(*args: any, **kwds: any):
            """Decorator that limits the number of calls to a function

            Args:
                *args (any): The arguments of the function
                **kwds (any): The keyword arguments of the function"""
            nonlocal count
            if (count < limit):
                count += 1
                return function(*args, **kwds)
            else:
                print("Error: <function", function.__name__, "at",
                      hex(id(function)), "> call too many times")
        return limit_function
    return callLimiter
