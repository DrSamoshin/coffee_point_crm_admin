# Docker
## Build
`docker build -t coffee_point_crm_admin:latest -f docker/Dockerfile .`
## Run
`docker run -d -p 8080:8080 coffee_point_crm_admin:latest`
## Work with docker
### Remove images
`docker rmi -f $(docker images -q)`
### Remove containers
`docker rm -f $(docker ps -aq)`
### Remove volumes
`docker volume rm $(docker volume ls -q)`
### Other commands
* `docker ps`                              # Показать запущенные контейнеры
* `docker ps -a`                           # Показать все (в том числе остановленные)
* `docker start <container_id|name>`      # Запустить контейнер
* `docker stop <container_id|name>`       # Остановить контейнер
* `docker restart <container_id|name>`    # Перезапустить контейнер
* `docker rm <container_id|name>`         # Удалить контейнер
* `docker images`                          # Список всех образов
* `docker build -t <имя>:<тег> .`         # Собрать образ из Dockerfile
* `docker rmi <image_id|name>`            # Удалить образ
* `docker volume ls`
* `docker volume rm db-data`

# Docker compose
## Build and run
docker/
`docker-compose build && docker-compose up`

## Stop
`docker compose down`
or
`docker compose -f docker/docker-compose.yml down`
