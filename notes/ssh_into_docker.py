If it wont let you in:
chmod 600 /Users/Crowdstreet/.docker/machine/machines/cs-app-production-20161118-b/id_rsa

If it says "Cannot connect to the Docker daemon", 
sudo usermod -aG docker ubuntu
then log out and back in

docker-machine ssh cs-app-production-20161118-b
docker ps
docker exec -i -t 43416d57646b /bin/bash
./manage.py shell_plus