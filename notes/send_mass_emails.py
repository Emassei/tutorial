for user_profile in UserProfile.objects.filter(private_portals__isnull=False, offers__isnull=True, investors__offers__isnull=False,private_portals__active=True):
    template_name = 'properties/emails/generic_investor_email.html'
    template_context = {}
    try:
        offer = user_profile.investors.first().offers.first()

        message = ("<p>This evening, Wednesday, 2/17 at 8:00PM PST, we will be"
                   " deploying a scheduled maintenance update that will result"
                   " in approximately 30 minutes of anticipated downtime"
                   " during which time the investment portal will be inaccessible.</p>"
                   "<p>Thank you for your patience during this maintenance period.</p>")
        subject = "Scheduled Downtime Notice - 2/17 @ 8:00PM PST"
        from_email = u'{} <{}>'.format(
            offer.property_obj.sponsor.email_display_name,
            offer.property_obj.sponsor.email_address
        )
        template_context.update({
            'offer': offer,
            'property': offer.property_obj,
            'portal_owner': offer.portal_name,
            'message': message,
            'from_email': u'{} <{}>'.format(
                offer.property_obj.sponsor.email_display_name,
                offer.property_obj.sponsor.email_address
            ),
        })
        kwargs = {
            'from_email': from_email,
            'subject': subject,
            'offer': offer,
            'template_name': template_name,
            'template_context': template_context,
        }
        for email in InvestorEmail.create_multiple_from_offer(**kwargs):
            email.send_and_record()
    except:
        pass