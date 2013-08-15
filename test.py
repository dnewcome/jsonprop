from json_property import json_property   
from json_dict import to_json_dict
import unittest


class MyClass(object):
    def __init__(self):
        self._test_prop = None
        self._is_serializing = False 

    @json_property('json_test_prop', False)
    def get_test_prop(self):
        return self._test_prop 

class JsonPropertyTests(unittest.TestCase):
    def test_nominal(self):
        myclass = MyClass()
        myclass._is_serializing = True
        myclass._test_prop = 'foo' 
        #myclass.test_prop_exclude = 'bar'
        print "included: " + myclass.get_test_prop
        #print "excluded: " + myclass.test_prop_exclude

        expected = {'json_test_prop': 'foo'}
        actual = to_json_dict(MyClass, myclass)

        self.assertEqual(actual, expected) 
