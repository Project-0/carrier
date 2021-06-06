#!/usr/bin/env python


ATLANTA_CARRIER = {
    'name': {'type': 'string'},                                                     # "default carrier configuration",
    'templates_volume_type': {'type': 'string', 'allowed': ['bind', 'volume']},     # "bind",
    'templates_volume_source': {'type': 'string'},      # "./src",
    'strains_volume_type': {'type': 'string', 'allowed': ['bind', 'volume']},       # "volume",
    'strains_volume_source': {'type': 'string'},        # "strains",
}

DOMAINS = {
    'atlanta-carrier': {
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'name'
        },
        'resource_methods': ['GET', 'POST'],
        'schema': ATLANTA_CARRIER
    }
}

# curl --request POST --header "Content-Type: application/json" localhost:5000/atlanta-carrier/ --data '{"name": "test", "templates_volume_type": "bind", "templates_volume_source": "./src", "strains_volume_type": "volume", "strains_volume_source": "strains"}'