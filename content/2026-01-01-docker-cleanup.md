Title: TIL: Docker Cleanup / Fresh Start Options
Date: 2025-10-27
Category: Today I Learned
Status: published

## Level 1: Containers \+ Volumes

```
docker compose down \-v
```

**Removes:** Containers, networks, named volumes **Keeps:** Images, anonymous volumes, build cache

## Level 2: \+ Remove Images

```
docker compose down \-v \--rmi all
```

**Removes:** Everything from Level 1 \+ all images used by services **Keeps:** Build cache, unused images, anonymous volumes

## Level 3: \+ Remove Anonymous Volumes

```
docker compose down \-v \--rmi all \--remove-orphans

docker volume prune \-f
```

**Removes:** Everything from Level 2 \+ orphaned containers \+ unused volumes **Keeps:** Build cache, unrelated images

## Level 4: Complete Docker Cleanup

*\# Stop all Docker containers*  
```docker stop $(docker ps \-aq)```

*\# Remove everything*  
```docker system prune \-a \--volumes \-f```

*\# Or more selectively:*  
```
docker container prune \-f    *\# Remove stopped containers*  
docker image prune \-a \-f     *\# Remove unused images*  
docker volume prune \-f       *\# Remove unused volumes*  
docker network prune \-f      *\# Remove unused networks*

docker builder prune \-a \-f   *\# Remove build cache*
```

## Level 5: Reset Docker Desktop

*\# Via Docker Desktop GUI: Settings \> Troubleshoot \> Clean / Purge data*

*\# Or restart Docker Desktop entirely*

## What Each Component Stores

**Volumes:** Database data, uploaded files, persistent storage 
**Images:** Your built application code, dependencies 
**Build cache:** Dockerfile layer cache (speeds up rebuilds) 
**Containers:** Runtime state, temporary files 
**Networks:** Custom networking configuration


## **Disk Space Recovery**

Check what's taking space:

```
docker system df        *\# Show Docker disk usage*  
docker image ls         *\# List all images*

docker volume ls        *\# List all volumes*
```

The higher levels progressively reclaim more disk space but require more time to rebuild everything from scratch.

Via: [https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes](https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes)

Via: [https://docs.docker.com/engine/manage-resources/pruning/](https://docs.docker.com/engine/manage-resources/pruning/)



