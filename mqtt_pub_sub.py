import socket
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import queue
import time
from threading import Lock, Thread

NUMBER_OF_SUBSCRIBERS = 0
NUMBER_OF_PUBLISHER = 0
MAX_BUFFER_SIZE = 16*1024  # 16KB
LOOP_TIME = 0.01  # 10ms

lock = Lock()


class MQTTSub:
    def __init__(self, topic, host="localhost", port=1883, qos=0, fifo_max_size=0):
        global NUMBER_OF_SUBSCRIBERS
        lock.acquire(blocking=True)
        self.client_id = "subscriber_pmanager_" + str(NUMBER_OF_SUBSCRIBERS)
        NUMBER_OF_SUBSCRIBERS += 1
        lock.release()
        if fifo_max_size > 0:
            self.queue = queue.Queue(fifo_max_size)
        else:
            self.queue = queue.Queue()
        self.lock_queue = Lock()
        self.topic = topic
        self.qos = qos
        self.connected = True
        self.client = mqtt.Client() 
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.connect(host, port, 10)#localhost
        self.client.socket().setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 16*1024)  # TODO:change to 16*1024
        self.running_iter = True
        self.t = Thread(target=self.iter)
        self.t.start()


    def on_connect(self, client, userdata, flags, rc):
        """
        FROM MQTT/client.py
        The value of rc indicates success or not:
        0: Connection successful
        1: Connection refused - incorrect protocol version
        2: Connection refused - invalid client identifier
        3: Connection refused - server unavailable
        4: Connection refused - bad username or password
        5: Connection refused - not authorised
        6-255: Currently unused.
        """
        if rc != 0:
            raise Exception(self.client_id + " couldn't connect to broker, failed: " + str(rc))
        client.subscribe(self.topic, qos=self.qos)
        # print("on_connect")

    def on_message(self, client, userdata, msg):
        # print(msg)

        # print("pmanger: ", msg.topic + " " + str(msg.qos) + " " + str(msg.payload) + " " + str(msg.mid))
        # print(self.a.ParseFromString(msg.payload))
        try:
            self.lock_queue.acquire()
            if self.queue.full():
                self.queue.get()
            self.queue.put((msg.payload, msg.topic))
        finally:
            self.lock_queue.release()

    def on_disconnect(self, client, userdata, rc):
        self.connected = False
        self.running_iter = False

    def iter(self):
        while True:
            while self.running_iter:
                self.client.loop()
                time.sleep(LOOP_TIME)
                # print("im in iter")
            if self.connected:
                break

            while not self.connected:
                try:
                    self.client.reconnect()
                    self.connected = True
                    self.running_iter = True
                except Exception as _:
                    time.sleep(0.1)
        self.client.unsubscribe(self.topic)

    def read_msg(self):
        try:
            self.lock_queue.acquire()

            if self.queue.empty():
                return ("", "")
            # (msg, topic) = self.queue.get()
            return self.queue.get()
        finally:
            self.lock_queue.release()

    def peek_topic(self):
        try:
            self.lock_queue.acquire()
            if self.queue.empty():
                return ""
            (_, topic) = self.queue.queue[0]
            return topic
        finally:
            self.lock_queue.release()

    def stop_subscriber(self):
        self.running_iter = False
        self.t.join()


class MQTTPub:
    def __init__(self, host="localhost", port=1883):
        global NUMBER_OF_PUBLISHER
        lock.acquire(blocking=True)
        self.client_id = "publisher_pmanager_" + str(NUMBER_OF_PUBLISHER)
        NUMBER_OF_PUBLISHER += 1
        lock.release()

    def publish_msg(self, topic, msg, host="localhost", port=1883, qos=0, retain=False):
        # print("publish msg ", topic)
        publish.single(topic, msg, qos=qos, retain=retain, hostname=host, port=port)
