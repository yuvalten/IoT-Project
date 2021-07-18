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
        mt_pb2 = self.pb_convert(inpt)
        with open("./meter_pb2.bin", "wb") as fd:
            self.bin_buffer = mt_pb2.SerializeToString()
            fd.write(self.bin_buffer)
        # print(self.bin_buffer)
        return self.bin_buffer

    def pb_convert(self, inpt):
        mt_pb2 = meter_pb2.XMeterTelem()
        mt_pb2.TimeStamp = inpt.TimeStamp
        mt_pb2.MeterType = inpt.MeterType
        mt_pb2.PosEnergy = int(inpt.PosEnergy)
        mt_pb2.NegEnergy = int(inpt.NegEnergy)
        mt_pb2.PosActivePowerTotal = int(inpt.PosActivePowerTotal)
        mt_pb2.NegActivePowerTotal = int(inpt.NegActivePowerTotal)
        mt_pb2.CurrentA = int(inpt.CurrentA)
        mt_pb2.CurrentB = int(inpt.CurrentB)
        mt_pb2.CurrentC = int(inpt.CurrentC)
        mt_pb2.VoltageAN = int(inpt.VoltageAN)
        mt_pb2.VoltageBN = int(inpt.VoltageBN)
        mt_pb2.VoltageCN = int(inpt.VoltageCN)
        mt_pb2.Freq = int(inpt.Freq)
        mt_pb2.PosActivePowerA = int(inpt.PosActivePowerA)
        mt_pb2.PosActivePowerB = int(inpt.PosActivePowerB)
        mt_pb2.PosActivePowerC = int(inpt.PosActivePowerC)
        mt_pb2.NegActivePowerA = int(inpt.NegActivePowerA)
        mt_pb2.NegActivePowerB = int(inpt.NegActivePowerB)
        mt_pb2.NegActivePowerC = int(inpt.NegActivePowerC)
        return mt_pb2

#     def pb_decode_msg(self):
#         mt_pb2 = self.pb_convert(self.inpt)
#         mt_pb2.ParseFromString(self.bin_buffer)
#         print(mt_pb2)

# if __name__ == "__main__":
#     # mt = MeterTelem()
#     inp = InputParser()
#     inpt = inp.get_meter_telem_from_input(0)
#     msg = PbMsg()
# #     # msg.pb_encode_msg(inpt)
#     msg.pb_decode_msg()







