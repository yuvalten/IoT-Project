import input_parser
import meter_telem
import pb_msg
import paho.mqtt.client as mqtt
import mqtt_pub_sub


class MeterSim:

    def __init__(self,publish_rate,input_parser,pb_msg,meter_telem):
        self.input_parser = input_parser.InputParser()
        self.bin_buffer = pb_msg.PbMsg()
        self.MeterTelem = meter_telem.MeterTelem()
        self.publish_rate = publish_rate
        # self.client = mqtt.Client()
        # self.on_connect = mqtt.connect()

        self.mqtt_pub = mqtt_pub_sub.MQTTPub()
        self.mqtt_sub = mqtt_pub_sub.MQTTSub()
        # connect to broker - make sure thr broker run as a service

    def meter_sim_run(self,publish_rate):
        i=0
        for i in range(publish_rate):

            self.input_parser.get_meter_telem_from_input(sampling_index)
            self.message = pb_msg.PbMsg.pb_encode_msg(MeterTelem)
            self.pub_msg = mqtt_pub_sub.MQTTPub.publish_msg("meter")
            #publish message with: mqtt_client-meter to metetr Topic

    # client = mqtt.Client()
    # client.on_connect = mqtt_pub_sub.MQTTSub.on_connect()
    # client.on_message = on_message

    # client.connect("localhost", 1883, 60)



def cb(callback,topics):
    print("hello")

def main():
    # meter_sim = MeterSim()
    # meter_sim.meter_sim_run()
    mq_sub = mqtt_pub_sub.MQTTSub("meter/")
    mq=mqtt_pub_sub.MQTTPub()
    mq.publish_msg("meter/", bin_buffer)
    mq_sub.client.message_callback_add("meter/", cb)

main()









#     def on_connect(client,userdata,flags,rc):
#         if rc==0:
#             print("connected OK")
#         else:
#             print("bad connection Returned code=", rc)
# mqtt_client_listener = mqtt_client_listener.Sniffer()
# BROKER_IP = mqtt_client_listener.ip
# mqtt_client_meter = mqtt.Client("Meter") #topic is Meter
# client.on_connect=on_connect

# import paho.mqtt.client as mqtt

    # The callback for when the client receives a CONNACK response from the server.
    # def on_connect(client, userdata, flags, rc):
    #     print("Connected with result code "+str(rc))
    #
    #     # Subscribing in on_connect() means that if we lose the connection and
    #     # reconnect then subscriptions will be renewed.
    #     client.subscribe("$SYS/#")
    #
    # # The callback for when a PUBLISH message is received from the server.
    # def on_message(client, userdata, msg):
    #     print(msg.topic+" "+str(msg.payload))

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
# client.loop_forever()