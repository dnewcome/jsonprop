from json_property import json_property   

class MyClass(object):
    def __init__(self):
        self._test_prop = None
        self._is_serializing = False 

    @json_property('json_test_prop', False)
    def get_test_prop(self):
        return self._test_prop 

    def set_test_prop(self, value):
        self._test_prop = value

    def to_json_dict(self):
        retval = {}
        for key in MyClass.__dict__:
            item = MyClass.__dict__[key] 
            if isinstance(item, json_property):
                #todo: shorter way to do this?
                retval[item.prefix] = item.__get__(self)

        return retval 
     
    
myclass = MyClass()
myclass._is_serializing = True
myclass.set_test_prop( 'foo' )
#myclass.test_prop_exclude = 'bar'
print "included: " + myclass.get_test_prop
#print "excluded: " + myclass.test_prop_exclude

print myclass.to_json_dict()

