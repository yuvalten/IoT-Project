from meter_telem import MeterTelem
from pb_msg import PbMsg
import mqtt_pub_sub
import schedule
import time



class MeterSim:

    def __init__(self):
        self.mq = mqtt_pub_sub.MQTTPub()



    def meter_sim_run():
        mq = mqtt_pub_sub.MQTTPub()
        pb = PbMsg()
        mt = MeterTelem()
        # print(pb.pb_encode_msg(mt))
        mq.publish_msg("meter/", pb.pb_encode_msg(mt))
        return

    publish_rate = 5
    schedule.every(publish_rate).seconds.do(meter_sim_run)

    while True:
        schedule.run_pending()
        time.sleep(1)


def Main():
    global ms
    ms = MeterSim()
    ms.meter_sim_run()

# if __name__ == "__main__":
#     ms = MeterSim()

    # mt = MeterTelem()
    # pub = ms.meter_sim_run()

