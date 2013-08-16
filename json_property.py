class json_property(object):
    def __init__(self, prefix, ser_if_null):
        print '__init__()'
        self.prefix = prefix
        self.text = 'foo'
        self._ser_if_null = ser_if_null

    def __call__(self, f):
        print '__call__()'
        print '_ser_if_null: ' + str(self._ser_if_null)
        self.f = f
        return self

    def __get__(self, obj, objtype=None):
        print 'running getter'
        return self.f(obj)
       
