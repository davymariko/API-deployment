# Definition of Json schema

from listler import postcodes

global json_schema
json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Belgian real estate property",
    "description": "Features of a Belgian real estate property",
    "type": "object",
    "required": ["data"],
    "properties": {
        "data": {
            "title": "Input data",
            "type": "object",
            "required": ["area", "property-type", "rooms-number", "zip-code"],
            "properties": {
                "area": {"title": "Area", "type": "integer", "exclusiveMinimum": 0},
                "property-type": {
                    "title": "Type of property",
                    "type": "string",
                    "enum": ["APARTMENT", "HOUSE", "OTHERS"],
                },
                "rooms-number": {
                    "title": "Number of rooms",
                    "type": "integer",
                    "minimum": 1,
                },
                "zip-code": {"title": "Belgian zip-code", "enum": postcodes},
                "land-area": {"type": "integer", "default": 0},
                "garden": {"type": "boolean", "default": False},
                "garden-area": {"type": "integer"},
                "equipped-kitchen": {"type": "boolean", "default": False},
                "full-address": {"type": "string"},
                "swimmingpool": {"type": "boolean", "default": False},
                "furnished": {"type": "boolean", "default": False},
                "open-fire": {"type": "boolean", "default": False},
                "terrace": {"type": "boolean", "default": False},
                "terrace-area": {"type": "integer"},
                "facades-number": {"type": "integer"},
                "building-state": {
                    "type": "string",
                    "default": "GOOD",
                    "enum": [
                        "NEW",
                        "GOOD",
                        "TO RENOVATE",
                        "JUST RENOVATED",
                        "TO REBUILD",
                    ],
                },
            },
        },
    },
}

if __name__ == "__main__":
    print(json_schema)
