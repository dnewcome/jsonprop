# About

Control JSON serialization of python objects using decorators.

# Usage

    from jsonprop import JsonObject, json_property

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

        json = myclass.json()

# API

The general form of the decorator is:

    json_property(name, include_null)

where name is the desired JSON field name for the python property and 
include_null is a boolean that indicates whether or not null values will 
be included in the serialization. By default this value is True and null values
will be serialized. If this is set to False, the field will be omitted entirely
in the serialized JSON output in the event that the value of the field is
None.


# Hacking

Serializing properties as collections, maybe extend this to (gasp) xml. 
Take a look at serialization properties in c# for more.
