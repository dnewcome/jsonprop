from json_property import json_property

def to_json_dict(cls, obj):
    retval = {}
    for key in cls.__dict__:
        item = cls.__dict__[key] 
        if isinstance(item, json_property):
            print 'item text ' + str(item._ser_if_null)
            if item._ser_if_null:
                retval[item.prefix] = item.__get__(obj)
            elif item.__get__(obj):
                retval[item.prefix] = item.__get__(obj)

    return retval 
