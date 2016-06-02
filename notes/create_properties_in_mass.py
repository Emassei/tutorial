titles = ['StorQuest: Centennial / Jordan (1004)',
     'StorQuest: Riverside / Magnolia (1005)',
     'StorQuest: Los Angeles / Figueroa (1007)',
     'StorQuest: Glendale / Union Hills (1008)',
     'StorQuest: Los Angeles / Hill (1009)',
     'StorQuest: Hollywood / Sunset (1010)',
     "StorQuest: Honolulu / Kaka'ako (1012)",
     'StorQuest: Honolulu / Umi (1013)',
     'StorQuest: La Quinta / Dune Palms (1014)',
     'StorQuest: San Rafael / Golden Gate (1015)',
     'StorQuest: Mission Hills / Laurel (1016)',
     'StorQuest: Moreno Valley / Spruce (1017)',
     'StorQuest: Oakland / Shattuck (1018)',
     'StorQuest: Oxnard / Jones (1023)',
     'StorQuest: Parker / Cottonwood (1024)',
     'StorQuest: Sun City / N 107th (1025)',
     'StorQuest: Los Angeles / Jefferson (1026)',
     'StorQuest: Rancho Cucamonga / Arrow (1027)',
     'StorQuest: Rancho Cucamonga / Hampshire (1028)',
     'StorQuest: San Leandro / Davis (1029)',
     'StorQuest: Thousand Oaks / Skyline (1032)',
     'StorQuest: Torrance / Earl (1033)',
     'StorQuest: Vallejo / Magazine (1034)',
     'StorQuest: Phoenix / Indian School (1035)',
     'StorQuest: West Los Angeles / Sawtelle (1037)',
     'StorQuest: Oakland / San Pablo (1040)',
     'StorQuest: Denver / Evans (1041)',
     'StorQuest: Waipahu / Farrington (1043)',
     'StorQuest: Tucson / Commerce (1045)',
     'StorQuest: Glendale / N 67th (1046)',
     'StorQuest: Apache Junction / Apache (1047)',
     'StorQuest: Tempe / Warner Rd (1063)',
     'StorQuest: Indio / Adobe (1064)',
     ]
tag_lines = ["A 629 unit StorQuest facility in Centennial, CO.",
     "A 599 unit StorQuest facility in Riverside, CA.",
     "A 663 unit StorQuest facility in Los Angeles, CA.",
     "A 799 unit StorQuest facility in Glendale, AZ.",
     "A 1634 unit StorQuest facility in Los Angeles, CA.",
     "A 499 unit StorQuest facility in Hollywood, CA.",
     "A 1911 unit StorQuest facility in Honolulu, HI.",
     "A 617 unit StorQuest facility in Honolulu, HI.",
     "A 554 unit StorQuest facility in La Quinta, CA.",
     "A 735 unit StorQuest facility in San Rafael, CA.",
     "A 635 unit StorQuest facility in Mission Hills, CA.",
     "A 408 unit StorQuest facility in Moreno Valley, CA.",
     "A 402 unit StorQuest facility in Oakland, CA.",
     "A 687 unit StorQuest facility in Oxnard, CA.",
     "A 711 unit StorQuest facility in Parker, CO.",
     "A 742 unit StorQuest facility in Sun City, AZ.",
     "A 887 unit StorQuest facility in Los Angeles, CA.",
     "A 558 unit StorQuest facility in Rancho Cucamonga, CA.",
     "A 629 unit StorQuest facility in Rancho Cucamonga, CA.",
     "A 501 unit StorQuest facility in San Leandro, CA.",
     "A 612 unit StorQuest facility in Thousand Oaks, CA.",
     "A 715 unit StorQuest facility in Torrance, CA.",
     "A 357 unit StorQuest facility in Vallejo, CA.",
     "A 397 unit StorQuest facility in Phoenix, AZ.",
     "A 359 unit StorQuest facility in West Los Angeles, CA.",
     "A 945 unit StorQuest facility in Oakland, CA.",
     "A 634 unit StorQuest facility in Denver, CO.",
     "A 729 unit StorQuest facility in Waipahu, HI.",
     "A 485 unit StorQuest facility in Tucson, AZ.",
     "A 706 unit StorQuest facility in Glendale, AZ.",
     "A 436 unit StorQuest facility in Apache Junction, AZ.",
     "A 412 unit StorQuest facility in Tempe, AZ.",
     "A 926 unit StorQuest facility in Indio, CA.",
     ]
slugs = ['storquest-centennial-jordan',
         'storquest-riverside-magnolia',
         'storquest-los-angeles-figueroa',
         'storquest-glendale-union-hills',
         'storquest-los-angeles-hill',
         'storquest-hollywood-sunset',
         "storquest-honolulu-kakaako",
         'storquest-honolulu-umi',
         'storquest-la-quinta-dune-palms',
         'storquest-san-rafael-golden-gate',
         'storquest-mission-hills-laurel',
         'storquest-moreno valley-spruce',
         'storquest-oakland-shattuck',
         'storquest-oxnard-jones',
         'storquest-parker-cottonwood',
         'storquest-sun-city-n-107th',
         'storquest-los-angeles-jefferson',
         'storquest-rancho-cucamonga-arrow',
         'storquest-rancho-cucamonga-hampshire',
         'storquest-san-leandro-davis',
         'storquest-thousand-oaks-skyline',
         'storquest-torrance-earl',
         'storquest-vallejo-magazine',
         'storquest-phoenix-indian-school',
         'storquest-west-los-angeles-sawtelle',
         'storquest-oakland-san-pablo',
         'storquest-denver-evans',
         'storquest-waipahu-farrington',
         'storquest-tucson-commerce',
         'storquest-glendale-n-67th',
         'storquest-apache-junction-apache',
         'storquest-tempe-warner rd',
         'storquest-indio-adobe',
        ]

initial_property = Property.objects.get(id=240)

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