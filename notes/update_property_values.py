def update_property_values():
    properties = Property.objects.filter(sponsor__slug='hamilton-zanze',
                                         status=5)
    status = 5
    hide_after_close = True
    prop_count = 0
    for o in properties:
        o.status = status
        o.hide_after_closed_private_portal = hide_after_close
        o.save()
        prop_count += 1
        print('Changed {} values'.format(o))

    print('Updated {}.'.format(prop_count))


update_property_values()

properties = Property.objects.filter(sponsor__slug='hamilton-zanze',
                                     summary_items__isnull=True)