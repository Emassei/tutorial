If it wont let you in:
chmod 600 /Users/Crowdstreet/.docker/machine/machines/cs-app-demo-20160921/id_rsa

If it says "Cannot connect to the Docker daemon", 
sudo usermod -aG docker ubuntu
then log out and back in

docker-machine ssh cs-app-production-20161014-a
docker ps
docker exec -i -t 261b99a7753a /bin/bash
./manage.py shell_plus