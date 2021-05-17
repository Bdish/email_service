# email_service

Сервис рассылки электронных писем + биллинг

docker-compose up

файл config.ini


[SMTP]

SERVER = smtp.mail.ru

USER = .....@mail.ru

PASSWORD = ......

SENDER = Piter


[LOGGER]

LOGFILE = email_service.log





Postmen

method: Post

url: http://0.0.0.0:8000/msg


header:

Content-Type:application/json

body:

{
    "template":{
        "id":1,
        "variables":{"first_name":"Иван Иванович!"}
    },
    "recipients":[".........@mail.ru"],
    "subject": "Супер пупер акция"
}
