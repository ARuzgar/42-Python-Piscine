def NULL_not_found(object: any) -> int:
    title_dict = {
        "NoneType": "Nothing:",
        "float": "Cheese:" if object != object else None,
        "int": "Zero:" if object == 0 else None,
        "str": "Empty:" if object == "" else None,
        "bool": "Fake:" if object == False else None,
    }
    
    typ = type(object)
    name = typ.__name__
    title = title_dict.get(name)
    
    if title:
        print(f"{title} {object} {object.__class__}")
        return 0
    else:
        print("Type not Found")
        return 1

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))