obj_tuple = (
    ('xxx','xxx','xxx'),

)

def return_uuids(obj_tuple):
    for slug, investor_name, business_entity in obj_tuple:
        offer = Offer.objects.get(property_obj__slug=slug, 
                                  investor__name__icontains=investor_name,
                                  business_entity__icontains=business_entity,
                                  )
        print(offer.uuid,offer)

return_uuids(obj_tuple)





