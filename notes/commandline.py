# This is how you download a remote database to your local
scp cs_production:/tmp/launchdump-2015-11-19-16-53-55.sql.gz ~/Desktop/

# This is how you apply a database instance to your local database
mysql -uroot crowdstreet < launchdump-2015-11-19-16-53-55.sql
