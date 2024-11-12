def all_thing_is_obj(object: any) -> int:
    try:
        print(f"{type(object).__name__} : {type(object)}")
    except TypeError:
        print("Type not found")
    return 42
