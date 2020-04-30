# Locustio

## Instalação

Siga as instruções em: http://docs.locust.io/en/latest/installation.html

Executar:

`$ pip install -r requirements.txt`

## Execução

### Unitário

`$ locust --host=qa1-api-events.[$host]`

### master

`$ locust --host=qa1-api-events.[$host]` --master

### slave

`$ locust --host=qa1-api-events.[$host]` --slave --master-host=192.168.10.3

## Saída

```
[2017-09-08 11:56:20,931] Ares.local/INFO/stdout: Connecting Socket...
[2017-09-08 11:56:20,931] Ares.local/INFO/stdout: 
[2017-09-08 11:56:20,946] Ares.local/INFO/stdout: Data received: {u'type': u'welcome'}
[2017-09-08 11:56:20,946] Ares.local/INFO/stdout: 
[2017-09-08 11:56:20,948] Ares.local/INFO/stdout: Sending Data: {'identifier': '{"channel":"NextDaysChannel","event_id":3}', 'command': 'subscribe'}
[2017-09-08 11:56:20,948] Ares.local/INFO/stdout: 
[2017-09-08 11:56:20,949] Ares.local/INFO/stdout: Sending Data: {'identifier': '{"channel":"MediaChannel","day_id":3}', 'command': 'subscribe'}
```
