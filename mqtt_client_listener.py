#!/usr/bin/python3.4

import os
import sys
from mqtt_pub_sub import MQTTSub
#from meter_pb2 import Meter
from meter_pb2 import XMeterTelem
import time
import threading
import argparse
import datetime

PARSER = argparse.ArgumentParser(description='This is a MQTT sniffer tool',
                                 formatter_class=argparse.RawTextHelpFormatter, add_help=False)

PARSER.add_argument('-h', '--help', action='store_true', dest='HELP', help='This script is used as MQTT sniffer\n'
                                                              './sniffer.py [-i|--ip <dest_ip>] [-t|--topic <topic>]\n'                                                              
                                                              'e.g.\n\t'
                                                              './sniffer.py -i localhost -t meter\n\n')
PARSER.add_argument('-i', '--ip', type=str, dest='DEST_IP', help='destination ip (Broker)')
PARSER.add_argument('-t', '--topic', type=str, dest='TOPIC', help='wifi network name (default "meter")')

ARGS = PARSER.parse_args()

MAX_PROTO_PER_LINE = 80


class Sniffer:
    def __init__(self, topic="meter/", file_path=None):
        self.ip = "127.0.0.1"
        print("Running MQTT sniffer at {}, topic {}".format(self.ip, topic))
        self.client = MQTTSub(topic=topic, host=self.ip, qos=0)
        self.listener = True
        self.t = threading.Thread(target=self.iter)
        self.t.start()
        self.check_input()
        pass

    def check_input(self):
        try:
            print("Listening... press ENTER exit\n")
            sys.stdin.read(1)
        finally:
            self.listener = False
            while not self.listener:
                time.sleep(0.1)
            print("Exiting")
            exit(0)

    def iter(self):
        time.sleep(3)
        while self.listener:
            (data, topic) = self.client.read_msg()
            if data != "":
                self.print_msg(self.deserialize_message(data, topic), topic)
            else:
                time.sleep(0.1)
        self.client.stop_subscriber()
        self.listener = True

    def print_msg(self, msg, topic):
        msg = msg.__str__().replace('\n', " ")
        info = msg.split(" ")
        msg = []
        tmp_msg = ""
        for i in range(len(info)):
            if len(info[i]) > 0:
                if (len(info[i]) + len(tmp_msg)) < MAX_PROTO_PER_LINE:
                    tmp_msg += info[i] + " "
                else:
                    msg.append(tmp_msg)
                    tmp_msg = info[i] + " "
        msg.append(tmp_msg)
        msg_to_print = "{:<50} {} {}\n".format(topic, "|", msg[0])
        for i in range(len(msg) - 1):
            msg_to_print += "{:<50} {} {}\n".format("", "|", msg[i+1])
        msg_to_print += "------------------------------------------------------------------------------------------" \
                        "--------------------------------------------"
        print(msg_to_print)

    @staticmethod
    def deserialize_message(data, topic):
        try:
            if "meter/" in topic:
                msg = XMeterTelem
            else:
                return data
            msg.ParseFromString(data)
            return msg
        except Exception as ex:
            print("This isn't a known message type ", ex)
            return data

def main():
    global BROKER_IP
    if ARGS.HELP:
        PARSER.print_help()
        return
    if ARGS.TOPIC:
        topic = ARGS.TOPIC
    else:
        topic = "meter/"
    if ARGS.DEST_IP:
        BROKER_IP = ARGS.DEST_IP
    Sniffer(topic)


main()


























# #!/usr/bin/python3.4
#
# import os
# import sys
#
# from mqtt_pub_sub import MQTTSub
# from meter_pb2 import XMeterTelem #??????
# # from meter_sim import MeterSim
# from pb_msg import PbMsg
# from input_parser import InputParser
# import time
# import threading
# import argparse
#
# PARSER = argparse.ArgumentParser(description='This is a MQTT sniffer tool',
#                                  formatter_class=argparse.RawTextHelpFormatter, add_help=False)
#
# PARSER.add_argument('-h', '--help', action='store_true', dest='HELP', help='This script is used as MQTT sniffer\n'
#                                                               './sniffer.py [-i|--ip <dest_ip>] [-t|--topic <topic>]\n'
#                                                               'e.g.\n\t'
#                                                               './sniffer.py -i localhost -t meter\n\n')
# PARSER.add_argument('-i', '--ip', type=str, dest='DEST_IP', help='destination ip (Broker)')
# PARSER.add_argument('-t', '--topic', type=str, dest='TOPIC', help='wifi network name (default "meter")')
#
# ARGS = PARSER.parse_args()
#
# MAX_PROTO_PER_LINE = 80
# FILE_PATH="/usr/bin/python3.8 /home/osboxes/Embedded/yuval-tenenbaum"
#
# class Sniffer:
#     def __init__(self, topic, file_path=FILE_PATH):
#         self.ip = "127.0.0.1"
#         self.topic = "meter/"
#         print("Running MQTT sniffer at {}, topic {}".format(self.ip, topic))
#         self.client = MQTTSub(topic=topic, host=self.ip, qos=0)
#         self.listener = True
#         self.t = threading.Thread(target=self.iter)
#         self.t.start()
#         self.check_input()
#         self.pb = PbMsg()
#
#
#
#     def check_input(self):
#         try:
#             print("Listening... press ENTER exit\n")
#             sys.stdin.read(1)
#         finally:
#             self.listener = False
#             while not self.listener:
#                 time.sleep(0.1)
#             print("Exiting")
#             exit(0)
#
#     def iter(self):
#         # print("im in iter")
#         time.sleep(3)
#         while self.listener:
#
#             (data, topic) = self.client.read_msg()
#             # print(data)
#             # self.print_msg(self.deserialize_message(data, topic), topic)
#             if data != "":
#
#                 self.print_msg(self.deserialize_message(data, topic), topic)
#             else:
#                 time.sleep(0.1)
#         self.client.stop_subscriber()
#         self.listener = True
#
#     def print_msg(self, msg, topic):
#         msg = msg.__str__().replace('\n', " ")
#         info = msg.split(" ")
#         msg = []
#         tmp_msg = ""
#         for i in range(len(info)):
#             if len(info[i]) > 0:
#                 if (len(info[i]) + len(tmp_msg)) < MAX_PROTO_PER_LINE:
#                     tmp_msg += info[i] + " "
#                 else:
#                     msg.append(tmp_msg)
#                     tmp_msg = info[i] + " "
#         msg.append(tmp_msg)
#         msg_to_print = "{:<50} {} {}\n".format(topic, "|", msg[0])
#         for i in range(len(msg) - 1):
#             msg_to_print += "{:<50} {} {}\n".format("", "|", msg[i+1])
#         msg_to_print += "------------------------------------------------------------------------------------------" \
#                         "--------------------------------------------"
#         mq_sub = MQTTSub("meter")
#         mq_sub.client.subscribe("meter", 0)
#         print(msg_to_print)
#         self.pb = PbMsg()
#         print(self.pb.bin_buffer)
#
#     @staticmethod
#     def deserialize_message(data, topic):
#         try:
#             if "meter" in topic:
#                 pb = PbMsg()
#                 msg = pb.bin_buffer
#             else:
#                 return data
#             msg.ParseFromString()
#             print(msg)
#             return msg
#         except Exception as ex:
#             print("This isn't a known message type ", ex)
#             return data
#
#     # def pb_decode_msg(self):
#     #     inp = InputParser()
#     #     inpt = inp.get_meter_telem_from_input(0)
#     #     mt_pb2 = self.pb_convert(self.inpt)
#     #     mt_pb2.ParseFromString(self.bin_buffer)
#     #     print(mt_pb2)
#
#
#
# def main():
#     global BROKER_IP
#     # ms = MeterSim()
#     if ARGS.HELP:
#         PARSER.print_help()
#         return
#     if ARGS.TOPIC:
#         topic = ARGS.TOPIC
#     else:
#         topic = "meter"
#     if ARGS.DEST_IP:
#         BROKER_IP = ARGS.DEST_IP
#     Sniffer(topic)
#     # Sniffer.deserialize_message(ms.meter_sim_run)
#
# # main()
#
# if __name__ == "__main__":
#     sn = Sniffer("meter", FILE_PATH)

