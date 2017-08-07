# Grab a field
advisor = CustomField.objects.filter(fieldname__icontains='Financial')

# grab the instance from the query set
advisor = advisor.first()

#grab user profiles, list can be emails
ups = UserProfile.objects.filter(user__email__in=list)

# Create custom data
for up in ups:
    CustomDatum.objects.create(user_profile=up, value='Yes', field=advisor)