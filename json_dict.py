from json_property import json_property
import json

class JsonObject:
    def _to_json_dict(self, cls, obj):
        retval = {}
        for key in cls.__dict__:
            item = cls.__dict__[key] 
            if isinstance(item, json_property):
                if item._ser_if_null:
                    retval[item.prefix] = item.__get__(obj)
                elif item.__get__(obj):
                    retval[item.prefix] = item.__get__(obj)

        return retval 

    def json(self, cls, obj):
        return json.dumps(self._to_json_dict(cls, obj))


def to_json_dict(cls, obj):
    retval = {}
    for key in cls.__dict__:
        item = cls.__dict__[key] 
        if isinstance(item, json_property):
            if item._ser_if_null:
                retval[item.prefix] = item.__get__(obj)
            elif item.__get__(obj):
                retval[item.prefix] = item.__get__(obj)

    return retval 
