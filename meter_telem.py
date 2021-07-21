from enum import Enum

#the equivalent XMeterTelem c struct

class MeterTelem:

	def __init__(self):
		self.TimeStamp=""
		self.MeterType=0
		self.PosEnergy=0
		self.NegEnergy=0
		self.NegEnergy=0
		self.PosActivePowerTotal=0
		self.NegActivePowerTotal=0
		self.CurrentA=0
		self.CurrentB=0
		self.CurrentC=0
		self.VoltageAN=0
		self.VoltageBN=0
		self.VoltageCN=0
		self.Freq=0
		self.PosActivePowerA=0
		self.PosActivePowerB=0
		self.PosActivePowerC=0
		self.NegActivePowerA=0
		self.NegActivePowerB=0
		self.NegActivePowerC=0
#Enum class equivalent XMeterTelem Enum

	class EMeterType(Enum):
		#00
		METER_TYPE_NONE = 0
		#01
		METER_TYPE_PRODUCTION =1
		#02
		METER_TYPE_FEED_IN =2
		#03
		METER_TYPE_CONSUMPTION =3
		#04
		METER_TYPE_PURCHASED =4
		#05
		METER_TYPE_FEED_IN_PURCHASED =5
		#06
		METER_TYPE_SELF_CONSUMPTION =6
		#07
		METER_TYPE_STORAGE_CHARGE_PV =7
		#08
		METER_TYPE_STORAGE_CHARGE_AC =8
		#09
		METER_TYPE_PV =9
		#10 Non - SE AC production
		METER_TYPE_PRODUCTION_EXT =10
		#11
		METER_TYPE_NUM =11



