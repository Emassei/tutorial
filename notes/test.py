
from properties.models import Property
from time import sleep

objs_tuple = (
    (495, '<h3>Section Coming Soon</h3>', [('xx', 'xxx'), ('Property Website', 'xxx'), ('xxx', 'xxx'), ('xxx', 'xxx'), ('xxx', '$xxx'), ('xxx', 'xxx')]),
)

def create_detail_page(objs_tuple):
    prop_count = 0
    for property_id, long_description, summary_list_items in objs_tuple:
        property = Property.objects.get(id=property_id)
        property.long_description = long_description
        i = 0
        for o in summary_list_items:
            PropertySummaryItem.objects.create(label='o[0]',
                                               value='o[1]',
                                               order=i,
                                               property_obj=property)
            i += 1
        prop_count += 1


        sleep(2)
        print('Loaded {}!'.format(property))


    print('Created {} detail pages.'.format(prop_count))


create_detail_page(objs_tuple)