from json_property import json_property

def to_json_dict(cls, obj):
    retval = {}
    for key in cls.__dict__:
        item = cls.__dict__[key] 
        if isinstance(item, json_property):
            #todo: shorter way to do this?
            retval[item.prefix] = item.__get__(obj)

    return retval 
