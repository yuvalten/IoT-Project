from meter_telem import MeterTelem
from pb_msg import PbMsg
from input_parser import InputParser
import mqtt_pub_sub
import schedule
import time
PUBLISH_RATE = 5
#install schedule - pip install schedule

class MeterSim:

    def __init__(self):
        self.mq = mqtt_pub_sub.MQTTPub()
        self.pb = PbMsg()
        self.inp = InputParser()

    def meter_sim_run():
        # mq = mqtt_pub_sub.MQTTPub()
        mq = mqtt_pub_sub.MQTTPub()
        pb = PbMsg()
        inp = InputParser()
        inpt = inp.get_meter_telem_from_input(0)
        mq.publish_msg("meter/", pb.pb_encode_msg(inpt))
        # print(pb.pb_encode_msg(inpt))
        return

    schedule.every(PUBLISH_RATE).seconds.do(meter_sim_run)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
        ms = MeterSim()
        ms.meter_sim_run()






