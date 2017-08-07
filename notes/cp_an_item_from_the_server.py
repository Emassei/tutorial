# Set the ENV variable
doma-env [name of the machine]

# Look at the machines
docker ps

# Copy the file
docker cp 3fa7abff5f4d:/crowdstreet-src/sponsor_direct_analytics.csv .
docker cp 5f45dbbc05bd:/crowdstreet-src/sponsor_direct_score_card.csv .

docker cp ae5d231bfc28:/crowdstreet-src/sponsor_direct_score_card.csv .


scp ssh cs_marketing:~/../../etc/apache2/ssl/22960776.crt .
scp ssh cs_marketing:~/../..//etc/apache2/ssl/www.crowdstreet.com-ev.key .
scp ssh cs_marketing:~/../..//etc/apache2/ssl/22960776.ca-bundle .