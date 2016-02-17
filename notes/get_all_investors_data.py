offs = 'hello'

for o in offs:
    print('Investing Entity Name:', o.investor,
          'Investor First Name:', o.investor.user_profiles.first().user.first_name,
          'Investor Last Name:', o.investor.user_profiles.first().user.last_name,
          'Investor Email:', o.investor.user_profiles.first().user.email,
          'Investor Phone:', o.investor.user_profiles.first().phone,
          'Investor Address:', o.investor.user_profiles.first().address,
          'Investor City:', o.investor.user_profiles.first().city,
          'Investor State:', o.investor.user_profiles.first().state,
          'Investor Zip:', o.investor.user_profiles.first().zip_code,
          'Amount Invested:', o.amount_invested,
          'Date Invested:', o.date_committed)
