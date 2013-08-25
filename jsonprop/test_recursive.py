import json
from json_field import json_field
from json_dict import JsonObject
from json_encoder import JsonObjectEncoder
import unittest

class MyClass(JsonObject):
    child = json_field('json_child', None, False)

class MyClass2(JsonObject):
    json_test = json_field('json_test_prop', 'foo', False)

class JsonFieldTests(unittest.TestCase):

    def test_kwargs(self):
        mychild = MyClass2()
        myparent = MyClass( child = mychild )

        expected = '{"json_child": {"json_test_prop": "foo"}}'
        actual = json.dumps( myparent._to_json_dict(), cls=JsonObjectEncoder)

        self.assertEqual(actual, expected) 

