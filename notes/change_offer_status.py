uuids=[x,x]


def change_property_for_offers():
    new_property = Property.objects.get(slug='x')
    offers = Offer.objects.filter(property_obj__slug='cci-mbm-xi-lp')
    offer_count = 0
    for o in offers:
        o.property_obj = new_property
        o.save()
        offer_count+=1
        print(o)
    print('changed {}'.format(offer_count))

change_property_for_offers()

def change_docs_to_new_property():
  new_property = Property.objects.get(slug='x')
  docs = Document.objects.filter(property_obj__slug='cci-mbm-xi-lp')
  doc_count = 0
  for doc in docs:
    doc.property_obj = new_property
    doc.save()
    doc_count+=1
    print(doc)
  print('changed {}'.format(doc_count))

change_docs_to_new_property()


def change_offer_status():
    property = Property.objects.get(slug='torrey-pines')
    emails = InvestorEmail.objects.filter(subject='New on the CrowdStreet Marketplace: Torrey Pines')
    ids = (o.user_profile.id for o in emails)
    offers = Offer.objects.filter(user_profile__id__in=ids, property_obj=property, stage=-6)
    i=0
    for o in offers:
        o.stage = -4
        o.save()
        i+=1
    print("changed {} offers".format(i))

change_offer_status()

import datetime

def change_offer_status_to_divested():
    property = Property.objects.get(slug='rose-villas-apartments')
    offers = Offer.objects.filter(property_obj=property, stage=100)
    i=0
    for o in offers:
        o.stage = 101
        o.date_divested = datetime.datetime(2017, 6, 1, 0, 0)
        o.amount_requested = o.amount_invested
        o.amount_invested = 0
        o.net_amount_invested = 0
        print(o)
        o.save()
        i+=1
    print("changed {} offers".format(i))

change_offer_status_to_divested()



def change_offer_amount():
    private_portal = PrivatePortal.objects.get(sponsor__slug='hamilton-zanze')
# investor__name__icontains="(B Shares)",
    offers = Offer.objects.filter(private_portal=private_portal,
                                  amount_invested=3.00,
                                  stage__gte=100)
    i = 0
    for o in offers:
        o.amount_invested = 0.00
        o.amount_requested = 0.00
        o.net_amount_invested = 0.00
        o.save()
        print("changed {}".format(o))
        i += 1
    print("changed {} offers".format(i))

change_offer_amount()


from datetime import datetime

def change_offer_date():
    private_portal = PrivatePortal.objects.get(sponsor__slug='hamilton-zanze')
    property = Property.objects.get(slug='lodge-at-mccarran-ranch')

    bad_ids = [149412, 196768]

    offers = Offer.objects.filter(private_portal=private_portal,
                                  property_obj=property,
                                  stage=100)

    offers = offers.exclude(id__in=bad_ids)

    i = 0
    new_date = datetime(2016, 11, 10, 0, 0)
    for o in offers:
        o.date_committed = new_date
        o.date_closed = new_date
        o.save()
        print("changed {}".format(o))
        i += 1
    print("changed {} offers".format(i))

change_offer_date()


list = [81238,
        167145
        ]

def delete_offers():
    distributions = Distribution.objects_unfiltered.filter(offer__id__in=list)
    for distribution in distributions:
        distributions.delete()

    documents = Document.objects_unfiltered.filter(offers__id__in=list)
    for document in documents:
        document.delete()

    offers = Offer.objects.filter(id__in=list)
    for offer in offers:
        print(offer)
        offer.delete()
   
    emails = InvestorEmail.objects_unfiltered.filter(offer__id__in=list)
    for email in emails:
        email.delete()  

delete_offers()

'''
This will create closing documents for docusign envelopes
'''

from esign.tasks import download_and_save_docusign_docs_as_offer_docs
from datetime import datetime
from time import sleep
import time

envelopes = DocumentEnvelope.objects.filter(document__isnull=True,
                                           date_created__gte=datetime(2017, 4, 10, 11, 6, 55, 951147),
                                           offer__stage__gte=21)
for e in envelopes:
     download_and_save_docusign_docs_as_offer_docs(e.pk)
     print(e)   
     time.sleep(2)

all(o=='torrey-pines' for o in  offers.values_list('property_obj__slug', flat=True))


def delete_duplicate_offers():
    '''
    These initial quieries 
    '''
    all_offers = Offer.objects.filter(property_obj__slug='loftin')
    up_ids = [o.user_profile.id for o in all_offers]
    dupe_up_ids =  [item for item, count in collections.Counter(up_ids).items() if count > 1]

    for o in dupe_up_ids:
        offers = Offer.objects.filter(user_profile__id=o,property_obj__slug='high-street')
        print(offers[1:])
        '''
        Splitting it like 1:, will start the delete after the first one
        thus preserving the first one
        '''
        for o in offers[1:]:
            o.delete()
        print(offers.count())

delete_duplicate_offers()


objs_tuple = (
    ('xxx','xxx'),


)

def change_investing_entity(objs_tuple):
  """
  Change entity names to a single one, and associate to one entity
  """
    private_portal = PrivatePortal.objects.get(id=50)
    for uuid, new_entity_name in objs_tuple:
        offer = Offer.objects.get(uuid=uuid)
        investor = Investor.objects.get(offers=offer)
        if investor.name == new_entity_name:
            print(u'Didnt change {}.'.format(investor.name.decode('utf-8')))
        else:
            investor.name = new_entity_name
            investor.save()
            print(u'Changed {}.'.format(new_entity_name.decode('utf-8')))
        investor_name = investor.name
        offers = Offer.objects.filter(investor__name=investor_name,
                                      private_portal=private_portal)
        for offer in offers:
            offer.investor = investor
            offer.save()
            print(u'Changed {} to new entity.'.format(offer.investor.name.decode('utf-8')))

change_investing_entity(objs_tuple)

objs_tuple=(
    (319511,17309.6, 17000),
    (319512,24922.48, 22547.84),
    (319513,13468.44, 12631.13),
    (319514,43359.9, 40000),
    (319515,77879.01, 50000),

)


def change_offer_amounts(objs_tuple):
    """
    change offer amounts
    """
    private_portal = PrivatePortal.objects.get(id=96)
    for id, amount_invested, net_amount_invested in objs_tuple:
        offer = Offer.objects.get(id=id,private_portal=private_portal)
        offer.amount_invested = amount_invested
        offer.net_amount_invested = net_amount_invested
        offer.save()
        print(offer,offer.id)

change_offer_amounts(objs_tuple)

objs_tuple = (
    ('d3cb521f-be69-4f73-95db-81cb27e964ef', 90449),
    ('11d04094-7e31-4132-9b6d-f6d091d6bba9', 7148),
    ('6b574adb-e697-442f-bc40-bfd3624203fb', 100000),
    ('680e8624-b6bd-4da1-8fcf-01d245a7fe70', 414103),

)


def change_offer_amount():
    for uuid, amount_invested in objs_tuple:
        offer = Offer.objects.get(uuid=uuid)
        offer.amount_invested = amount_invested
        offer.save()
        print(offer.amount_invested, offer)

change_offer_amount()


def create_leads():
    from datetime import datetime, timedelta
    days_ago_30 = datetime.today() - timedelta(days=30)

    private_portal = PrivatePortal.objects.get(sponsor__slug='crowdstreet')
    property_obj = Property.objects.get(slug='loftin')

    # This one is for SKB
    user_profiles = UserProfile.objects.filter(
        approval_status=1,
        user__date_joined__lte=days_ago_30,
        is_marketplace_investor=True,
        investors__is_accredited=True,
        investment_preference__expected_12mo_cre_investment_amt__isnull=False,
        user__is_active=True
    )
    # This is for Castle lantera
    offer_ids = [o.id for o in Offer.objects.filter(
        stage__gte=5,
    )]

    user_profiles_with_an_offer = UserProfile.objects.filter(
        approval_status=1,
        user__date_joined__gte=days_ago_30,
        offers__id__in=offer_ids,
        is_marketplace_investor=True,
        investors__is_accredited=True
    )
    user_profiles_on_cs = UserProfile.objects.filter(
        approval_status=1,
        user__date_joined__lt=days_ago_30,
        is_marketplace_investor=True,
        investors__is_accredited=True
    )

    for user_profile in user_profiles_on_cs:
        Offer.objects.create(
            property_obj=property_obj,
            user_profile=user_profile,
            private_access_granted=False,
            private_portal=private_portal,
            stage=Offer.ACCESS_GRANTED,
            lead_owner=1,
        )
        print(user_profile,user_profile.id)

UserProfile.objects.filter(
  investors__offers__stage__gt=Offer.SUBMITTED
).aggregate(num_offers=Count('investors__offers')).filter(num_offers__gte=1)



property = Property.objects.get(slug='pavilions-at-silver-sage')

def change_offer_amount_from_actions():
    offer = Offer.objects.filter(property_obj=property)
    actions = offer.get_actions()
    data = [action.data for action in actions.values() if 'new' in action.data]
    [action.data.values() for action in actions if 'new' in action.data.values()]



objs_tuple = (
    (150437, 287741.47),
    (233024, 1),
    (150364, 10606.84),
    (150404, 20596.86),
    (150361, 6629.27),
    (150360, 5306.24),
    (150358, 19965.45),
    (150357, 26517.09),
    (233022, 1),
)

for offer_id, amount_invested in objs_tuple:
    try:
        offer = Offer.objects.get(id=offer_id)
        offer.amount_invested = amount_invested
        offer.net_amount_invested = amount_invested
        offer.amount_requested = amount_invested
        offer.save()
        print(offer.id)
    except Offer.DoesNotExist:
        print('{} Does not exist'.format(offer_id))


objs_tuple = (
    ('x',"x","x", "", datetime.datetime(2017, 3, 21, 0, 0)),
    ('x',"x","x", "x",datetime.datetime(2017, 3, 21, 0, 0))
)

offer_list = []
no_offer_list = []
for property_slug, investing_entity, tax_entity, amount_invested, date_invested in objs_tuple:
    try:
        offer = Offer.objects.get(
            property_obj__slug=property_slug,
            investor__name=investing_entity,
            tax_entity=tax_entity,
            amount_invested=amount_invested
        )
        offer.date_closed = date_invested
        offer.save()
        offer_list.append(offer)
    except Offer.DoesNotExist:
        no_offer_list.append(investing_entity)

