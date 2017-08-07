If it wont let you in:
chmod 600 /Users/xxx
If it says "Cannot connect to the Docker daemon", 

then log out and back in

# Set the variable 
docker ps
docker exec -i -t xxx /bin/bash
# or 
giddyup xxx
./manage.py shell_plus