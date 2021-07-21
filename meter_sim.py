from pb_msg import PbMsg
import mqtt_pub_sub
import time

class MeterSim:

    def __init__(self):
# Create mqtt client instance
        self.mq = mqtt_pub_sub.MQTTPub()
        self.pb = PbMsg()

    def meter_sim_run(self, publish_rate=5):
        while True:
# Publish bin_buffer to "meter" topic
            self.mq.publish_msg("meter", self.pb.bin_buffer)
            time.sleep(publish_rate)



















