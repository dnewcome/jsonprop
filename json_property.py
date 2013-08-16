class json_property(object):
    def __init__(self, prefix, ser_if_null):
        self.prefix = prefix
        self._ser_if_null = ser_if_null

    def __call__(self, f):
        self.f = f
        return self

    def __get__(self, obj, objtype=None):
        return self.f(obj)
       
