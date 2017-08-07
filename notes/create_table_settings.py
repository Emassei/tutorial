portal = PrivatePortal.objects.get(sponsor__slug='hamilton-zanze')

def create_table_settings():
    user_profiles = UserProfile.objects.filter(private_portal=portal)
    count = 0
    for user_profile in user_profiles:
        table = TableSettings.objects.create(user_profile=user_profile,
                                             table_name='my-investments',
                                             name='',
                                             )
        table.columns_name.remove('amount_distributed')
        table.save()
        count=+1
    print('created {} tables!'.format(count))

create_table_settings()


