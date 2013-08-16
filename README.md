# About

Control json serialization using decorators.

# Usage

Inherit from JsonObject
    class MyJsonObjectClass(JsonObject):
        def __init__(self):
            self._test_prop = None

Decorate getter method with @json_property

    ...
        @json_property('json_test_prop', False)
        def get_test_prop(self):
            return self._test_prop 

use json() method inherited from JsonObject to serialize

        actual = myclass.json(MyClass, myclass)
