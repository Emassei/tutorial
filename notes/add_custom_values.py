objs_tuple=(
    ('xxxxxxx-9xxxxxxxxxxxxxxxxxxxxxxx','yes'),
    ('xxxxxxx-3xxxxxxxxxxxxxxxxxxxxxxx','yes'),
    ('xxxxxxx-3xxxxxxxxxxxxxxxxxxxxxxx','yes'),
    ('xxxxxxx-3xxxxxxxxxxxxxxxxxxxxxxx','yes'),
    ('xxxxxxx-dxxxxxxxxxxxxxxxxxxxxxxx','yes'),
)

def add_custom_values():
    field = CustomField.objects.get(label='06/2017 Distribution - Email')
    user_profile_count = 0
    for uuid, value in objs_tuple:
        try:
            CustomDatum.objects.get_or_create(
                field=field,
                user_profile=UserProfile.objects.get(uuid=uuid),
                defaults={
                    'value': value
                }
            )
            user_profile_count += 1
        except UserProfile.DoesNotExist:
            print(uuid)
    print('Loaded {}'.format(user_profile_count))

add_custom_values()