# Activate ENV
source /home/ubuntu/webapps/crowdstreet/bin/activate

# Grab snapshot
aws s3 cp s3://backup-app-qa-psql/crowdstreet-ip-172-31-42-196-2016-07-15-095751.psql.gpg .

# Move Snapshot to current directory
mv /home/ubuntu/crowdstreet-ip-172-31-42-196-2016-07-15-095751.psql.gpg .

# Now restore the DB
./manage.py dbrestore -c -I crowdstreet-ip-172-31-42-196-2016-07-15-095751.psql.gpg