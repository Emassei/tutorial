portal = PrivatePortal.objects.get(sponsor__slug='hamilton-zanze')

def update_investors():
    user_profiles = UserProfile.objects.filter(private_portal=portal)
    up_ids = [o.id for o in user_profiles]
    investors = Investor.objects.filter(user_profiles__id__in=up_ids,
                                        accreditation=0)
    investor_count = 0
    for o in investors:
        o.accreditation = 10
        o.save()
        investor_count += 1
    print('updated {} investors!'.format(investor_count))

update_investors()


ts.column_names = [n for n in ts.column_names if n != 'distriutions']