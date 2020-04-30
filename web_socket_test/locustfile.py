# -*- coding:utf-8 -*-
import time
import json
import gevent

from uuid import uuid4

from locust import TaskSet, events, task, Locust
import websocket


class SocketClient(object):
    TIMEOUT = 10
    REQUEST_TYPE = 'Socket'

    def __init__(self, host):
        self.host = host
        self.session_id = uuid4().hex
        self.connect()

    def connect(self):
        try:
            start_time = time.time()
            self.ws = websocket.WebSocket()
            self.ws.settimeout(self.TIMEOUT)
            self.ws.connect(self.host)
            elapsed = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type=self.REQUEST_TYPE, name='connect',
                                        response_time=elapsed,
                                        response_length=0)
        except Exception as e:
            events.request_failure.fire(request_type=self.REQUEST_TYPE, name='connect',
                                        response_time=0, exception=e)

    def send_with_response(self, payload):
        json_data = json.dumps(payload)

        g = gevent.spawn(self.ws.send, json_data)
        g.get(block=True, timeout=self.TIMEOUT)
        g = gevent.spawn(self.ws.recv)
        result = g.get(block=True, timeout=self.TIMEOUT)

        json_data = json.loads(result)
        return json_data

    def on_close(self):
        try:
            self.ws.close()
        except Exception as e:
            events.request_failure.fire(request_type=self.REQUEST_TYPE, name='close',
                                        response_time=0, exception=e)

    def send(self, payload):
        start_time = time.time()
        try:
            self.send_with_response(payload)

            elapsed = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type=self.REQUEST_TYPE, name='send',
                                        response_time=elapsed,
                                        response_length=0)
        except Exception as e:
            elapsed = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=self.REQUEST_TYPE, name='send',
                                        response_time=elapsed, exception=e)


class WSBehavior(TaskSet):
    def on_start(self):
        next_day_channel = {
            'command': 'subscribe',
            'identifier': '{"channel":"NextDaysChannel","event_id":3}'
        }
        self.client.send(next_day_channel)

        media_channel = {
            'command': 'subscribe',
            'identifier': '{"channel":"MediaChannel","day_id":12}'
        }
        self.client.send(media_channel)

        events_channel = {
            'command': 'subscribe',
            'identifier': '{"channel":"EventsChannel"}'
        }
        self.client.send(events_channel)

    @task(1)
    def media(self):
        pass


class WSUser(Locust):
    # task_set = WSBehavior
    min_wait = 300 * 1000
    max_wait = 300 * 1000

    def __init__(self, *args, **kwargs):
        super(WSUser, self).__init__(*args, **kwargs)
        self.client = SocketClient('ws://%s/cable' % self.host)
