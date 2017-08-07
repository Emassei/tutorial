data = [{u'first_name': u'Matthew', u'last_name': u'Murphy', u'created_at': None, u'email': u'matt.murphy@mac.com', u'meta': u'`created_at`, `verified_on`, and `verification_status` are now deprecated at the root level in this response and show junk values. Please try the user-specific endpoint and provide the `legal_name` as a param to check statuses. The legal name is not required for the Check Verification Request endpoint.', u'id': 5228}

, {u'first_name': u'Matthew', u'last_name': u'Murphy', u'created_at': None, u'email': u'mattmurphy505@gmail.com', u'meta': u'`created_at`, `verified_on`, and `verification_status` are now deprecated at the root level in this response and show junk values. Please try the user-specific endpoint and provide the `legal_name` as a param to check statuses. The legal name is not required for the Check Verification Request endpoint.', u'id': 4837}

, {u'first_name': u'Joe', u'last_name': u'Murphy', u'created_at': None, u'email': u'p2rinvest@mailzone.com', u'meta': u'`created_at`, `verified_on`, and `verification_status` are now deprecated at the root level in this response and show junk values. Please try the user-specific endpoint and provide the `legal_name` as a param to check statuses. The legal name is not required for the Check Verification Request endpoint.', u'id': 2300}

, {u'first_name': u'Matthew', u'last_name': u'Murphy', u'created_at': None, u'email': u'mandlproperties2@gmail.com', u'meta': u'`created_at`, `verified_on`, and `verification_status` are now deprecated at the root level in this response and show junk values. Please try the user-specific endpoint and provide the `legal_name` as a param to check statuses. The legal name is not required for the Check Verification Request endpoint.', u'id': 1999}

]

print [o['last_name'] for o in data if (o['last_name'] == 'Murphy')]

print [o.last_name for o in data if (o[last_name] == 'Murphy')]