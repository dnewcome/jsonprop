class json_property(object):
    def __init__(self, prefix, ser_if_null=True):
        print '__init__()'
        #self.f = f
        self.prefix = prefix
        self.ser_if_null = ser_if_null

    def __call__(self, f):
        print '__call__()'
        self.f = f
        return self

    def __get__(self, obj, objtype=None):
        print 'running getter'
        print obj._is_serializing
        if obj._is_serializing and self.ser_if_null:
            #return self.prefix + ' '  +  self.f.__name__ + self.f(obj) 
            return self.prefix 
        else:
            return self.f(obj)
       
