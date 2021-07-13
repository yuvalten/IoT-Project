import input_parser
import meter_telem
import pb_msg
import paho.mqtt.client as mqtt
import mqtt_client_listener

class MeterSim:

    def __init__(self,publish_rate,):
        self.input_parser = input_parser.InputParser()
        self.bin_buffer = pb_msg.PbMsg()
        self.MeterTelem = meter_telem.MeterTelem()
        self.publish_rate = publish_rate
        self.client = mqtt.Client()
        self.connect = mqtt.connect()

        # connect to broker - make sure thr broker run as a service

    def meter_sim_run(self,publish_rate):
        i=0
        for i in range(publish_rate):

            input_parser.InputParser.get_meter_telem_from_input(0)
            message = pb_msg.PbMsg.pb_encode_msg(self)
            #publish message with: mqtt_client-meter to metetr Topic


    def on_connect(client,userdata,flags,rc):
        if rc==0:
            print("connected OK")
        else:
            print("bad connection Returned code=", rc)
mqtt_client_listener = mqtt_client_listener.Sniffer()
BROKER_IP = mqtt_client_listener.ip
mqtt_client_meter = mqtt.Client("Meter") #topic is Meter
client.on_connect=on_connect

    def main(self):
        meter_sim = MeterSim()
        meter_sim.meter_sim_run()




