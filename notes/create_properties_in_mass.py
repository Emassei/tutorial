<<<<<<< HEAD
from datetime import datetime

titles = ['xxx',

          ]

tag_lines = ['xxx',

             ]

slugs = ['x',
         ]

address = ["tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           "tbd",
           ]


city = ["tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        "tbd",
        ]

state = ["IL",
         "IL",
         "IL",
         "IN",
         "MN",
         "IL",
         "IL",
         "IL",
         "IL",
         "MD",
         "NY",
         "IL",
         "tbd",
         "tbd",
         "tbd",
         ]

zip_code = ["tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            "tbd",
            ]
property_type = [10,
                 10,
                 10,
                 10,
                 10,
                 10,
                 10,
                 10,
                 10,
                 10,
                 10,
                 10,
                 8,
                 8,
                 8,
                 ]

date_closed = [datetime(1984, 1, 1, 15, 23, 1, 0),
               datetime(1986, 1, 1, 15, 23, 1, 0),
               datetime(1986, 1, 1, 15, 23, 1, 0),
               datetime(1986, 1, 1, 15, 23, 1, 0),
               datetime(1988, 1, 1, 15, 23, 1, 0),
               datetime(1996, 1, 1, 15, 23, 1, 0),
               datetime(1996, 1, 1, 15, 23, 1, 0),
               datetime(1997, 1, 1, 15, 23, 1, 0),
               datetime(1998, 1, 1, 15, 23, 1, 0),
               datetime(2000, 1, 1, 15, 23, 1, 0),
               datetime(2002, 1, 1, 15, 23, 1, 0),
               datetime(2003, 1, 1, 15, 23, 1, 0),
               datetime(2004, 1, 1, 15, 23, 1, 0),
               datetime(2006, 1, 1, 15, 23, 1, 0),
               datetime(2012, 1, 1, 15, 23, 1, 0),
               ]

total_value = [460,
               ]

targeted_irr = [12,
                ]

risk_profile = [3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                ]

lot_size = [123,
            ]


initial_property = Property.objects.get(id=935)
sponsor = Sponsor.objects.get(id=146)
=======
titles = ['Lakeside Parking',
          'Kuykendahl Professional Plaza I',
          'Kuykendahl Professional Plaza II',
          'College Park Medical Plaza',
          'Coppell Freestanding ED',
          'Mansfield Freestanding ED',
          '2950 FM 2920',
          'Harmony Medical Plaza',
          'Frisco Freestanding ED',
          'Terramont Village Shopping Center',
          'Six Pines at Research Plaza 2',
          ]
tag_lines = ['TBD',
             'TBD',
             'TBD',
             'TBD',
             'TBD',
             'TBD',
             'TBD',
             'TBD',
             'TBD',
             'TBD',
             'TBD',
             ]
slugs = ['lakeside-parking',
         'kuykendahl-professional-plaza-i',
         'kuykendahl-professional-plaza-ii',
         'college-park-medical-plaza',
         'coppell-freestanding-ed',
         'mansfield-freestanding-ed',
         '2950-fm-2920',
         'harmony-medical-plaza',
         'frisco-freestanding-ed',
         'terramont-village-shopping-center',
         'six-pines-at-research-plaza-2',
         ]
>>>>>>> parent of 4fd5f1e... Add webinar button.

initial_property = Property.objects.get(id=331)

i = 0
for title in titles:
    _property = initial_property
<<<<<<< HEAD
    _property.long_description = '<div></div>'
    _property.sponsor = sponsor
    _property.date_closed = date_closed[i]
    _property.pk = None
    _property.status = 5
    _property.total_value = total_value[i]
    _property.targeted_irr = targeted_irr[i]
    _property.bank_loan = 1
    _property.risk_profile = risk_profile[i]
    _property.sponsor_investment = 1
    _property.short_description = '<div></div>'
    _property.sponsor_esigner = None
    _property.address = address[i]
    _property.city = city[i]
    _property.state = state[i]
    _property.zip_code = zip_code[i]
    _property.property_type = property_type[i]
=======
    _property.pk = None
>>>>>>> parent of 4fd5f1e... Add webinar button.
    _property.name = title
    _property.tagline = tag_lines[i]
    _property.slug = slugs[i]
    _property.lot_size = lot_size[i]
    _property.save()
    print('Created', _property)

    i += 1
