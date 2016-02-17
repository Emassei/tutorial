from common.utils import MockRequest
from Property import Offer
from a import User

off = Offer.objects.get(id=11169)

jr = User.objects.get(
    email="jrobertson@crowdstreet.com",
    userprofile__is_a_crowdstreet_marketplace_investor=True)

request = MockRequest(jr)

request.POST = {'comment': 'VerifyInvestor has no record of investor'
                'verification.'}

'''You can mark it in whatever way you want, adding items to the dictionary as
necessary'''

off.mark_verification_missing(request)

off.mark_offer_invested(request)
