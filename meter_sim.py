import threading
from pb_msg import PbMsg
from input_parser import InputParser
import mqtt_pub_sub
import time

# PUBLISH_RATE = 5

class MeterSim:

    def __init__(self):
        self.mq = mqtt_pub_sub.MQTTPub()
        self.pb = PbMsg()
        self.inp = InputParser()
        self.t1 = threading.Thread(target=self.meter_sim_run)

    def meter_sim_run(self,publish_rate=5):
        while True:
            # mq_sub = mqtt_pub_sub.MQTTSub("meter")
            # mq_sub.client.subscribe("meter", 0)
            self.mq = mqtt_pub_sub.MQTTPub()
            self.pb = PbMsg()
            inpt = self.inp.get_meter_telem_from_input(0)
            self.mq.publish_msg("meter/", self.pb.pb_encode_msg(inpt))
            print(self.pb.pb_encode_msg(inpt))
            time.sleep(publish_rate)

if __name__ == "__main__":
    ms = MeterSim()
    ms.meter_sim_run()


















