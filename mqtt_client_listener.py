#!/usr/bin/python3.4

import os
import sys

from mqtt_pub_sub import MQTTSub
from meter_pb2 import Meter

import time
import threading
import argparse
import datetime
import input_parser
import meter_telem
import pb_msg
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
    def __init__(self, topic, file_path=None):
        self.ip = BROKER_IP
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
            if "meter" in topic:
                msg = Meter()
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
        topic = "meter"
    if ARGS.DEST_IP:
        BROKER_IP = ARGS.DEST_IP 
    Sniffer(topic)


main()
