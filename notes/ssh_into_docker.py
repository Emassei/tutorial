If it wont let you in:
chmod 600 /Users/Crowdstreet/.docker/machine/machines/cs-app-demo-20160921/id_rsa

If it says "Cannot connect to the Docker daemon", 
sudo usermod -aG docker ubuntu, then log out and back in

docker-machine ssh cs-app-production-20160926
docker ps
docker exec -i -t 41d8f5a84cd2 /bin/bash
./manage.py shell_plus