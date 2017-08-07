fields = ('user_profile', 'table_name', 'name', 'is_private')
tups = TableSettings.objects.values(*fields).annotate(Count('id')).filter(id__count__gt=1).values_list(*fields)

for upid, table_name, name, is_private in tups:
    up = UserProfile.objects.get(pk=upid)
    qs = up.tablesettings_set.filter(table_name=table_name, name=name, is_private=is_private)
    for ts in qs[1:]:
        ts.delete()