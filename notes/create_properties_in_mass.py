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

initial_property = Property.objects.get(id=331)

i = 0
for title in titles:
    _property = initial_property
    _property.pk = None
    _property.name = title
    _property.tagline = tag_lines[i]
    _property.slug = slugs[i]
    _property.save()
    print('Created', _property)

    i += 1
