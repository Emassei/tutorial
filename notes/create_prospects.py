
users = ['email@email.com'
         ]

ids = [o.user_profile.id for o in users]


def create_prospects():
    property_obj = Property.objects.get(slug='torrey-pines')
    i = 0
    for user_profile in UserProfile.objects.filter(id__in=ids):
        Offer.objects.create(property_obj=property_obj,
                             user_profile=user_profile,
                             stage=Offer.PROSPECT
                             )
        i += 1
    print("created {} prospects".format(i))

create_prospects()