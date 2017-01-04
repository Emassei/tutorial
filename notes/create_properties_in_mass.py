# from datetime import datetime

titles = ['StorQuest Temecula / Lyndie (8005)',
          'StorQuest Long Beach / South (8007)',
          'San Rafael Self Storage / San Rafael (9002)',
          'StorQuest Canoga Park / Canoga (9010)',
          'StorQuest Westlake Village / Corsa (9011)',
          ]

tag_lines = ['TBD',
             'TBD',
             'TBD',
             'TBD',
             'TBD',
             ]

slugs = ['storquest-temecula-lyndie',
         'storquest-long-beach-south',
         'san-rafael-self-storage-san-rafael',
         'storquest-canoga-park-canoga',
         'storquest-westlake-village-corsa',
         ]

address = ['TBD',
           'TBD',
           'TBD',
           'TBD',
           'TBD',
           ]

business_entity = ['TBD',
                   'TBD',
                   'TBD',
                   'TBD',
                   'TBD',
                   ]

city = ['TBD',
        'TBD',
        'TBD',
        'TBD',
        'TBD',
        ]

state = ['TBD',
         'TBD',
         'TBD',
         'TBD',
         'TBD',
         ]
zip_code = ['11111',
            '11111',
            '11111',
            '11111',
            '11111',
            ]
property_type = [11,
                 11,
                 11,
                 11,
                 11,
                 ]

# date_closed = [datetime(2014, 2, 27),
#                datetime(2006, 12, 18),
#                datetime(2015, 1, 20),
#                datetime(2011, 3, 15),
#                datetime(2015, 10, 19),
#                datetime(2013, 10, 21),
#                datetime(2015, 9, 21),
#                datetime(2015, 9, 28),
#                datetime(2016, 8, 19),
#                ]

initial_property = Property.objects.get(id=488)
sponsor = Sponsor.objects.get(id=20)


i = 0
for title in titles:
    _property = initial_property
    _property.long_description = '<div></div>'
    _property.sponsor = sponsor
    # _property.date_closed = date_closed[i]
    _property.pk = None
    _property.status = 5
    _property.total_value = 1
    _property.bank_loan = 1
    _property.sponsor_investment = 1
    _property.short_description = '<div></div>'
    _property.sponsor_esigner = None
    _property.address = address[i]
    _property.city = city[i]
    _property.state = state[i]
    _property.zip_code = zip_code[i]
    _property.property_type = property_type[i]
    _property.name = title
    _property.tagline = tag_lines[i]
    _property.slug = slugs[i]
    _property.save()
    print('Created', _property)

    i += 1
