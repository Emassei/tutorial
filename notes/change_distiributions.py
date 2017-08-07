list = []


def delete_distributions():
    distributions = Distribution.objects_unfiltered.filter(offer__id__in=list)
    for distribution in distributions:
        distributions.delete()


property_obj = Property.objects.get(slug='legacy-opportunity-fund-member')

def delete_distributions():
    distributions = Distribution.objects_unfiltered.filter(offer__property_obj=property_obj,
                                                           month=3,
                                                           year=2017)
    for distribution in distributions:
        print(distribution)
        distributions.delete()

delete_distributions()


l = [10938,6868,13698,47744]

user_list = []
user_profile_list = []
for o in l:
    user = User.objects.get(id=o)
    user_list.append(user)
    user_profile = UserProfile.objects.get(user=user)
    user_profile_list.append(user_profile)


filters = (inactive, "delete")

distributions = Distribution.objects.filter(
    offer__property_obj__sponsor__slug='castle-lanterra-properties').exclude(
    cash_flow_type=3)

properties = [o.offer.property_obj for o in distributions]

properties = set(properties)


def retrieve_deleted_distributions():
    """
    This allows us to retrieve deleted distributions, we in effect create new
    ones using the old as kwargs
    """
    from django.core.exceptions import ValidationError
    l = ['xxx']

    distributions = Distribution.objects_unfiltered.filter(
        offer__property_obj__sponsor__slug='trueline-capital',
        date_deleted__isnull=False).exclude(id__in=l)

    bad = []

    for distribution in distributions:
        try:
            dictionary = dict(distribution.__dict__)
            del dictionary['id']
            del dictionary['_state']
            del dictionary['date_deleted']
            created = Distribution.objects.create(**dictionary)
            print(created)
            distribution.delete()
        except ValidationError:
            bad.append(distribution)
