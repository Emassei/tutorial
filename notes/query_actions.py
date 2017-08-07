
# This is how you query a action
# The target_object_id can be whatever object
Action.objects.filter(target_object_id=9240, verb__icontains='received an email')

# Read the Dam docs https://django-activity-stream.readthedocs.io/en/latest/

# Query no user actions and assign them to a placeholder user

l=[]
def reassign_null_action_actors():
    import types
    sponsor = Sponsor.objects.get(id=31)
    offers = Offer.objects.filter(property_obj__sponsor=sponsor)
    for offer in offers:
        offer_actions = offer.get_actions()
        for action in offer_actions:
            if isinstance(action.actor, types.NoneType):
                l.append(action.pk)
            else:
                pass
    list(set(l))

    bad_actions = Action.objects.filter(pk__in=l)
    import ipdb; ipdb.set_trace()

    user = User.objects.get(id=68392)
    for o in bad_actions:
        o.actor = user
        print(o)
        o.save()

reassign_null_action_actors()