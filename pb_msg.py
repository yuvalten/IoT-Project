from input_parser import InputParser
from meter_telem import MeterTelem
import meter_pb2
# # files path = /usr/bin/python3.8 /home/osboxes/Embedded/yuval-tenenbaum

class PbMsg:
    def __init__(self):
        self.inp = InputParser()
        self.inpt = self.inp.get_meter_telem_from_input(0)
        self.bin_buffer = self.pb_encode_msg(self.inpt)
        self.mt_pb2 = self.bin_buffer

    # serializing meter_pb2
    def pb_encode_msg(self, inpt):
        mt_pb2 = self.pb_convert(self.inpt)
        with open("./meter_pb2.bin", "wb") as fd:
            self.bin_buffer = mt_pb2.SerializeToString()
            fd.write(self.bin_buffer)
        # print(type(self.mt_pb2))
        # print("self.bin_buffer type is:", type(self.bin_buffer))
        # print(self.bin_buffer)
        return self.bin_buffer

    def pb_convert(self, inpt):
        self.mt_pb2 = meter_pb2.XMeterTelem()
        self.mt_pb2.TimeStamp = self.inpt.TimeStamp
        self.mt_pb2.MeterType = self.inpt.MeterType
        self.mt_pb2.PosEnergy = int(self.inpt.PosEnergy)
        self.mt_pb2.NegEnergy = int(self.inpt.NegEnergy)
        self.mt_pb2.PosActivePowerTotal = int(self.inpt.PosActivePowerTotal)
        self.mt_pb2.NegActivePowerTotal = int(self.inpt.NegActivePowerTotal)
        self.mt_pb2.CurrentA = int(self.inpt.CurrentA)
        self.mt_pb2.CurrentB = int(self.inpt.CurrentB)
        self.mt_pb2.CurrentC = int(self.inpt.CurrentC)
        self.mt_pb2.VoltageAN = int(self.inpt.VoltageAN)
        self.mt_pb2.VoltageBN = int(self.inpt.VoltageBN)
        self.mt_pb2.VoltageCN = int(self.inpt.VoltageCN)
        self.mt_pb2.Freq = int(self.inpt.Freq)
        self.mt_pb2.PosActivePowerA = int(self.inpt.PosActivePowerA)
        self.mt_pb2.PosActivePowerB = int(self.inpt.PosActivePowerB)
        self.mt_pb2.PosActivePowerC = int(self.inpt.PosActivePowerC)
        self.mt_pb2.NegActivePowerA = int(self.inpt.NegActivePowerA)
        self.mt_pb2.NegActivePowerB = int(self.inpt.NegActivePowerB)
        self.mt_pb2.NegActivePowerC = int(self.inpt.NegActivePowerC)
        return self.mt_pb2

    # def pb_decode_msg(self):
    #     self.mt_pb2 = self.pb_convert(self.inpt)
    #     self.mt_pb2.ParseFromString(self.bin_buffer)
    #     print(self.mt_pb2)

        # print(type(self.mt_pb2))
if __name__ == "__main__":
    # mt = MeterTelem()
    inp = InputParser()
    inpt = inp.get_meter_telem_from_input(0)
    msg = PbMsg()
    msg.pb_encode_msg(inpt)
    # msg.pb_decode_msg()








