def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print("Nothing: ", end="")
            print(object, end=" ")
            print(type(object))
        elif isinstance(object, float) and object != object:
            print("Cheese: ", end="")
            print(object, end=" ")
            print(type(object))
        elif object is False:
            print("Fake: ", end="")
            print(object, end=" ")
            print(type(object))
        elif object == 0:
            print("Zero: ", end="")
            print(object, end=" ")
            print(type(object))
        elif object == '':
            print("Empty: ", end="")
            print(type(object))
        else:
            print("Type not found")
        return 1
    except TypeError:
        return 0
