# To run this locally
RUN_LOCAL_TESTS=True python manage.py test functional_tests --settings=settings.test --liveserver=127.0.0.1:8000 --behave_verbose

# Run webpack
npm run watch

# your ./manage.py runserver cannot be on the same port
# as the tests