[Demo](https://hack-learning.herokuapp.com/api/)

[See Frontend](https://github.com/hack-learn/frontend)

## Initialize

1. Change to the root of your project directory.

```
  sudo chown -R $USER:$USER.
```

```
  docker-compose up
```

2. List running containers.

```
docker ps
```

## Shut down services and clean up

Ctrl-C

or

```
docker-compose down
```

## Run remote migrations

heroku run --app hack-learning python manage.py makemigrations

heroku run --app hack-learning python manage.py migrate

## Run local migrations

docker exet -ti #no_or_name_container
