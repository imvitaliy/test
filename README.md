### instalar aplicacion
si no existe python3.6 > pthon3.5
```sh
cd test
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
```

### run django rest

```sh
python manage.py runserver 0.0.0.0:8000 &
```


### run server aiohttp
```sh
python core/server.py &
```

### check Rest API
```sh
curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"title" : "one","sentence": "first sentence"}' http://127.0.0.1:8000/sentence/

curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"title" : "two","sentence": "second sentence"}' http://127.0.0.1:8000/sentence/

curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"title" : "tree","sentence": "third sentence"}' http://127.0.0.1:8000/sentence/


curl -X GET http://127.0.0.1:8000/sentence/

```

### check server aiohttp
```sh
curl -X GET http://127.0.0.1:8080/
curl -X GET http://127.0.0.1:8080/Paquito
```

![Alt Text](https://media.giphy.com/media/pqkBgz8JkfGrC/giphy.gif)

