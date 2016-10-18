If it wont let you in:
chmod 600 /Users/Crowdstreet/.docker/machine/machines/cs-app-demo-20160921/id_rsa

If it says "Cannot connect to the Docker daemon", 
sudo usermod -aG docker ubuntu
then log out and back in

docker-machine ssh cs-app-sales-20161004
docker ps
docker exec -i -t c285fe3c8557 /bin/bash
./manage.py shell_plus