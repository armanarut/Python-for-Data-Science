def all_thing_is_obj(object: any) -> int:
    if type(object) is list:
        print("List : ", end="")
        print(type(object))
    elif type(object) is tuple:
        print("Tuple : ", end="")
        print(type(object))
    elif type(object) is set:
        print("Set : ", end="")
        print(type(object))
    elif type(object) is dict:
        print("Dict : ", end="")
        print(type(object))
    elif type(object) is str:
        print("Brian is in the kitchen : ", end="")
        print(type(object))
    else:
        print("Type not found")
    return 42
