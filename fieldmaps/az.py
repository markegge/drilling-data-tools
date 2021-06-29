layout = {
    'date_field': 'statusdate',
    'api_field': 'apino',
    'type_field': 'commodityofinterest',
    'status_field': 'status',
    'lat_field': 'latdegree',
    'lon_field': 'longdegree',
    'location_src_field': None,
    'description_layout': '\n'.join(['Well Name: %s',
                             'Operator: %s',
                             'County: %s',
                             'Field: %s', 
                             'AZ OGCC Notes: %s'
                            ]),
    'description_fields': ['wellname', 'operator', 'county', 'field', 'notes'],
    'type_map': {
        'Carbon Dioxide': 'OTHER',
        'OilAndGas': 'OILANDGAS',
        'information': 'TEST',
        'water': 'WATER',
        'Information': 'TEST',
        'GeothermalEnergy': 'OTHER',
        'Helium': 'OTHER',
        'Unknown': 'UNKNOWN',
        'Geotechnical': 'OTHER',
        'Gas': 'GAS',
        'Brine': 'OTHER',
        'Monitor': 'OBSERVATION',
        'Water': 'WATER',
        'Observation': 'OBSERVATION',
        'Oil': 'OIL',
        'Liquified gas': 'GAS',
        'unknown': 'UNKNOWN',
        'CarbonDioxide': 'OTHER',
        'Salt': 'OTHER',
        'nil:missing': 'UNKNOWN'
    },
    'status_map': {
        'Capped': 'PA',
        'Not completed': 'CANCELLED',
        'Abandoned': 'A',
        'Abandoned junked': 'A',
        'Abandoned plugged': 'PA',
        'Active': 'ACTIVE',
        'Groundwater sampling date': 'UNKNOWN',
        'Never drilled': 'CANCELLED',
        'Status': 'UNKNOWN',
        'Unknown': 'UNKNOWN',
        'unknown': 'UNKNOWN',
        'Abondoned': 'PA',
        'Shut in': 'SI',
        'Abandoned temporary': 'TA',
        'Temoprarily abandoned': 'TA',
        'nil:missing': 'UNKNOWN',
    }
}