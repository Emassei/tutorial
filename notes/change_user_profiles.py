def deactivate_users():
    portal = PrivatePortal.objects.get(sponsor__slug='hamilton-zanze')

    user_profiles = UserProfile.objects.filter(user__last_name__icontains='(delete)',
                                               user__is_active=True,
                                               private_portal=portal)

    for user_profile in user_profiles:
        user_profile.user.is_active = False
        user_profile.user.save()
        print(user_profile,'is inactive')

deactivate_users()



def delete_users():
    portal = PrivatePortal.objects.get(sponsor__slug='dlp-capital-advisors')

    from django.db.models import Q

    do_not_delete_list = ['email@email.com'
                          ]

    # cs_users = UserProfile.objects.filter(Q(user__email__icontains='@crowdstreet.com'), private_portal=portal)
    # cs_user_ids = [o.id for o in cs_users]

    user_profiles = UserProfile.objects.filter(private_portal=portal)
    user_profiles = user_profiles.exclude(user__email__in=do_not_delete_list)
    # user_profiles = user_profiles.exclude(id__in=cs_user_ids)
    user_profiles = UserProfile.objects.filter(private_portal__sponsor__slug='hamilton-zanze')
    user_profiles = user_profiles.filter(user__last_name__icontains='delete')
    
    user_ids = [o.user.id for o in user_profiles]

    users = User.objects.filter(id__in=user_ids)

    investors = Investor.objects.filter(user_profiles__user__id__in=user_ids,
                                        offers__isnull=True)

    for o in investors:
        o.delete()
        print(o)

    for o in user_profiles:
        o.delete()
        print(o)

    # for o in users:
    #     o.delete()
    #     print(o.email)


delete_users()

user_profiles_to_delete = []
users_to_delete = []
entities_to_delete = []

portal = PrivatePortal.objects.get(id=70)

def delete_filtered_users():
    user_profiles = UserProfile.objects.filter(
        user__is_active=False,
        private_portal__isnull=False,
        private_portal=portal
    )
    for user_profile in user_profiles:
        try:
            offers = Offer.objects.filter(
                user_profile=user_profile)
            for offer in offers:
                investor = offer.investor
                if investor == None:
                    pass
                else:
                    new_user_profile = investor.user_profiles.first()
                    offer.user_profile = new_user_profile
                    offer.save()
                    print('changed {}').format(offer)
                    entities = Investor.objects.filter(
                        user_profiles=user_profile,
                        offers__isnull=False
                    )
                    entities_to_delete.append(entities)
        except Offer.DoesNotExist:
            pass
        user_profiles_to_delete.append(user_profile)
        users_to_delete.append(user_profile.user)

delete_filtered_users()


user_profiles_to_be_removed = []
portal = PrivatePortal.objects.get(id=70)

def put_users_in_a_list():
    """
    The investment amount does not show up here:
    offer_ids = [168529, 158257, 168702]
    investor_id = 65859
    """
    user_profiles = UserProfile.objects.filter(
        private_portal=portal,
        investors__isnull=True
    )
    for user_profile in user_profiles:
        try:
            offers = Offer.objects.filter(
                user_profile=user_profile
            )
            for offer in offers:
                if offer.investor:
                    user_profiles_in_entity = offer.investor.user_profiles.all()
                    if user_profile not in user_profiles_in_entity:
                        user_profiles_to_be_removed.append(user_profile)
                        good_user_profile = offer.investor.user_profiles.first()
                        offer.user_profile = good_user_profile
                        offer.save()
                    else:
                        pass
                else:
                    pass
        except Offer.DoesNotExist:
            pass
put_users_in_a_list()








def create_leads():
    from datetime import datetime, timedelta
    days_ago_30 = datetime.today() - timedelta(days=30)

    private_portal = PrivatePortal.objects.get(sponsor__slug='crowdstreet')
    property_obj = Property.objects.get(slug='high-street')

    # This one is for SKB
    user_profiles = UserProfile.objects.filter(
        investment_preference__isnull=False,
        approval_status=1,
        user__date_joined__lte=days_ago_30,
        is_marketplace_investor=True,
        investors__is_accredited=True
    )
    # This is for Castle lantera
    offer_ids = [o.id for o in Offer.objects.filter(
        stage__gte=5,
    )]

    user_profiles = UserProfile.objects.filter(
        approval_status=1,
        user__date_joined__lte=days_ago_30,
        offers__id__in=offer_ids,
        is_marketplace_investor=True,
        investors__is_accredited=True
    )

    for user_profile in users_profiles:
        Offer.objects.create(
            property_obj=property_obj,
            user_profile=user_profile,
            private_access_granted=False,
            private_portal=private_portal,
            stage=Offer.ACCESS_GRANTED,
            investors__is_accredited=True
        )



objs_tuple = (
    ('cnbraymer@yahoo.com','PA'),
    ('tram@rcn.com','PA'),
    ('placeholder897254@dlpplaceholder.com','PA'),
    ('placeholder57028@dlpplaceholder.com','PA'),
)

def add_values_to_user_profile(objs_tuple):
    portal = PrivatePortal.objects.get(sponsor__slug='dlp-capital-advisors')
    user_profile_count = 0
    for email, state in objs_tuple:
        user_profile = UserProfile.objects.get(user__email=email,private_portal=portal)
        if user_profile.state:
            user_profile.save()
            print("Didn't change {}".format(user_profile))
        else:
            user_profile.state = state
            user_profile.save()
            print("Changed {}".format(user_profile))
            user_profile_count+=1
    print('changed {} user_profiles'.format(user_profile_count))


add_values_to_user_profile(objs_tuple)






l = [
    ('aalexander@castlelanterra.com', 'TX'),
    ('aalexander@castlelanterra.com', 'TX'),
    ('aalexander@castlelanterra.com', 'TX'),
]

# Changing to a set to kill the dupes
l = list(set(l))
# then back to a tuple so we can parce the data, prob not necesarry
objs_tuple = tuple(l)

def add_value_to_user_profile():
    user_count = 0
    for email, state in objs_tuple:
        print(email)
        user = User.objects.get(email=email)
        if user.user_profile.state:
            print("NO change for {}".format(user.email))
        else:
            user.user_profile.state = state
            print("CHANGED {}".format(user.email))
            user.user_profile.save()

add_value_to_user_profile()

https://www.youtube.com/watch?v=GBkw2vtW6AE




investors = Investor.objects.filter(
    user_profiles__isnull=False
)

bad = []


for investor in investors:
    up = investor.user_profiles.first()
    email = up.user.email
    for user_profile in investor.user_profiles.exclude(id=up.id):
        if email == user_profile.user.email:
            bad.append(investor)
        else:
            pass

new_list = []

for investor in bad:
    up1, up2 = investor.user_profiles.all()
    if up1.private_portal is None and up2.private_portal is not None:
        new_list.append(investor)
    elif up2.private_portal is None and up1.private_portal is not None:
        new_list.append(investor)
    else:
        None

new_list = set(new_list)
new_list = list(new_list)

orphans = []

for investor in new_list:
    up1, up2 = investor.user_profiles.all()
    if up1.private_portal is None:
        up1.membership_set.all().delete()
        orphans.append(up1)
    elif up2.private_portal is None:
        up2.membership_set.all().delete()
        orphans.append(up2)
    else:
        pass






            