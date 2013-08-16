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

class MyClassSerializeNulls(object):
    def __init__(self):
        self._test_prop = None
        self._is_serializing = False 

    @json_property('json_test_prop', True)
    def get_test_prop(self):
        return self._test_prop 

class JsonPropertyTests(unittest.TestCase):

    def test_nominal(self):
        myclass = MyClass()
        myclass._is_serializing = True
        myclass._test_prop = 'foo' 

        expected = {'json_test_prop': 'foo'}
        actual = to_json_dict(MyClass, myclass)

        self.assertEqual(actual, expected) 

    def test_excluded(self):
        myclass = MyClass()
        myclass._is_serializing = True

        expected = {}
        actual = to_json_dict(MyClass, myclass)

        self.assertEqual(actual, expected) 
    
    def test_serialize_null(self):
        myclass = MyClassSerializeNulls()
        myclass._is_serializing = True

        expected = {'json_test_prop': None}
        actual = to_json_dict(MyClassSerializeNulls, myclass)

        self.assertEqual(actual, expected) 
