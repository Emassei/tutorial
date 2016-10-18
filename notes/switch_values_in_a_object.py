for u in users:
   u.first_name, u.last_name = u.last_name, u.first_name
   .save()