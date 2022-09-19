#!/usr/bin/env python

import serial
import struct


OP_ERROR = 0x7f

OP_WRITE = 0x01
OP_READ = 0x02


OP_I2C_MEM_W = 0x19
OP_I2C_MEM_R = 0x20


OP_MEASURE  = 0x00
OP_DRIVE_VOLTAGE  = 0x12
OP_DRIVE_CURRENT  = 0x13

OP_GET_TEMPERATURE = 0x14
OP_RAW_VOLTAGES = 0x16

OP_MEASURE_VOLTAGE = (0x09)

OP_MEASURE_CURRENT = (0x10)
OP_MEASURE_EXT = (0x11)

OP_RAW_ADC = (0x22)


OP_READ_TRIGGER =			(0x18)
OP_ASYNC_MEASURE_VOLTAGE =	(0x30)
OP_ASYNC_MEASURE_CURRENT =	(0x31)
OP_ASYNC_MEASURE_EXT =		(0x32)
OP_ASYNC_DRIVE_VOLTAGE =	(0x33)
OP_ASYNC_DRIVE_CURRENT =	(0x34)
OP_ASYNC_START_SWEEP =		(0x35)

OP_SET_OUTPUT = 			(0x40)
OP_SET_LOW_CURRENT_MODE = 	(0x41)


### STRIX


PARAM_AUTORANGING =         (0)
PARAM_COMPLIANCE_VOLTAGE =  (1)
PARAM_COMPLIANCE_CURRENT =  (2)
PARAM_AVERAGES =            (3)
PARAM_TRIGGER_MODE =        (4)

PARAM_4WIRE_MODE =          (5)
PARAM_GUARD_MODE =          (6)

PARAM_THERMAL_MODE =        (7)
PARAM_TEMPCO_MODE =         (8)

PARAM_PLC_SYNC_MODE =       (9)

PARAM_ADC_VOLTAGE_GAIN =    (10)
PARAM_LARGE_CURRENT_GAIN =  (11)
PARAM_EXT_VOLTAGE_GAIN =    (12)

PARAM_HEATER_TARGET =       (13)

PARAM_ADC_SAMPLERATE =      (14)

PARAM_ASYNC_STATE =         (15)

PARAM_ASYNC_RETRIGGER =     (16)

PARAM_DATA_MAX_COUNT =      (17)

PARAM_HEATER_STATE =        (18)

PARAM_ASYNC_CHANNEL =       (19)




PARAM_COMP_VDRIVE_DIV10_0 = (20)
PARAM_COMP_VDRIVE_DIV10_1 = (21)
PARAM_COMP_VDRIVE_DIV10_2 = (22)
PARAM_COMP_VDRIVE_DIV10_3 = (23)

PARAM_COMP_VDRIVE_1X_0 = (24)
PARAM_COMP_VDRIVE_1X_1 = (25)
PARAM_COMP_VDRIVE_1X_2 = (26)
PARAM_COMP_VDRIVE_1X_3 = (27)

PARAM_COMP_VDRIVE_10X_0 = (28)
PARAM_COMP_VDRIVE_10X_1 = (29)
PARAM_COMP_VDRIVE_10X_2 = (30)
PARAM_COMP_VDRIVE_10X_3 = (31)


PARAM_COMP_VMEAS_1X_0 = (32)
PARAM_COMP_VMEAS_1X_1 = (33)
PARAM_COMP_VMEAS_1X_2 = (34)
PARAM_COMP_VMEAS_1X_3 = (35)

PARAM_COMP_VMEAS_8X_0 = (36)
PARAM_COMP_VMEAS_8X_1 = (37)
PARAM_COMP_VMEAS_8X_2 = (38)
PARAM_COMP_VMEAS_8X_3 = (39)

PARAM_COMP_VMEAS_64X_0 = (40)
PARAM_COMP_VMEAS_64X_1 = (41)
PARAM_COMP_VMEAS_64X_2 = (42)
PARAM_COMP_VMEAS_64X_3 = (43)

PARAM_COMP_IMEAS_1_0 = (44)
PARAM_COMP_IMEAS_1_1 = (45)
PARAM_COMP_IMEAS_1_2 = (46)
PARAM_COMP_IMEAS_1_3 = (47)

PARAM_COMP_IMEAS_2_0 = (48)
PARAM_COMP_IMEAS_2_1 = (49)
PARAM_COMP_IMEAS_2_2 = (50)
PARAM_COMP_IMEAS_2_3 = (51)

PARAM_COMP_IMEAS_3_0 = (52)
PARAM_COMP_IMEAS_3_1 = (53)
PARAM_COMP_IMEAS_3_2 = (54)
PARAM_COMP_IMEAS_3_3 = (55)

PARAM_COMP_IMEAS_4_0 = (56)
PARAM_COMP_IMEAS_4_1 = (57)
PARAM_COMP_IMEAS_4_2 = (58)
PARAM_COMP_IMEAS_4_3 = (59)


PARAM_COMP_IDRIVE_1_0 = (60)
PARAM_COMP_IDRIVE_1_1 = (61)
PARAM_COMP_IDRIVE_1_2 = (62)
PARAM_COMP_IDRIVE_1_3 = (63)

PARAM_COMP_IDRIVE_2_0 = (64)
PARAM_COMP_IDRIVE_2_1 = (65)
PARAM_COMP_IDRIVE_2_2 = (66)
PARAM_COMP_IDRIVE_2_3 = (67)

PARAM_COMP_IDRIVE_3_0 = (68)
PARAM_COMP_IDRIVE_3_1 = (69)
PARAM_COMP_IDRIVE_3_2 = (70)
PARAM_COMP_IDRIVE_3_3 = (71)

PARAM_COMP_IDRIVE_4_0 = (72)
PARAM_COMP_IDRIVE_4_1 = (73)
PARAM_COMP_IDRIVE_4_2 = (74)
PARAM_COMP_IDRIVE_4_3 = (75)

PARAM_TEMPCO_VDRIVE_DIV10_GAIN =  (76)
PARAM_TEMPCO_VDRIVE_DIV10_T0 =    (77)

PARAM_TEMPCO_VDRIVE_1X_GAIN =     (78)
PARAM_TEMPCO_VDRIVE_1X_T0 =       (79)

PARAM_TEMPCO_VDRIVE_10X_GAIN =    (80)
PARAM_TEMPCO_VDRIVE_10X_T0 =      (81)

PARAM_TEMPCO_VMEAS_1X_GAIN =      (82)
PARAM_TEMPCO_VMEAS_1X_T0 =        (83)

PARAM_TEMPCO_VMEAS_8X_GAIN =      (84)
PARAM_TEMPCO_VMEAS_8X_T0 =        (85)

PARAM_TEMPCO_VMEAS_64X_GAIN =     (86)
PARAM_TEMPCO_VMEAS_64X_T0 =       (87)

PARAM_TEMPCO_IMEAS_1_GAIN =       (88)
PARAM_TEMPCO_IMEAS_1_T0 =         (89)

PARAM_TEMPCO_IMEAS_2_GAIN =       (90)
PARAM_TEMPCO_IMEAS_2_T0 =         (91)

PARAM_TEMPCO_IMEAS_3_GAIN =       (92)
PARAM_TEMPCO_IMEAS_3_T0 =         (93)

PARAM_TEMPCO_IMEAS_4_GAIN =       (94)
PARAM_TEMPCO_IMEAS_4_T0 =         (95)

PARAM_TEMPCO_IDRIVE_1_GAIN =       (96)
PARAM_TEMPCO_IDRIVE_1_T0 =         (97)

PARAM_TEMPCO_IDRIVE_2_GAIN =       (98)
PARAM_TEMPCO_IDRIVE_2_T0 =         (99)

PARAM_TEMPCO_IDRIVE_3_GAIN =       (100)
PARAM_TEMPCO_IDRIVE_3_T0 =         (101)

PARAM_TEMPCO_IDRIVE_4_GAIN =       (102)
PARAM_TEMPCO_IDRIVE_4_T0 =         (103)


PARAM_COMP_4W_VMEAS_0 =             (104)
PARAM_COMP_4W_VMEAS_1 =             (105)
PARAM_COMP_4W_VMEAS_2 =             (106)
PARAM_COMP_4W_VMEAS_3 =             (107)

PARAM_COMP_4W_VDRIVE_0 =             (108)
PARAM_COMP_4W_VDRIVE_1 =             (109)
PARAM_COMP_4W_VDRIVE_2 =             (110)
PARAM_COMP_4W_VDRIVE_3 =             (111)


PARAM_TEMPCO_4W_VMEAS_GAIN =        (112)
PARAM_TEMPCO_4W_VMEAS_T0 =          (113)

PARAM_TEMPCO_4W_VDRIVE_GAIN =        (114)
PARAM_TEMPCO_4W_VDRIVE_T0 =          (115)


PARAM_COMP_VEXT_1X_0 =             (116)
PARAM_COMP_VEXT_1X_1 =             (117)
PARAM_COMP_VEXT_1X_2 =             (118)
PARAM_COMP_VEXT_1X_3 =             (119)

PARAM_COMP_VEXT_8X_0 =             (120)
PARAM_COMP_VEXT_8X_1 =             (121)
PARAM_COMP_VEXT_8X_2 =             (122)
PARAM_COMP_VEXT_8X_3 =             (123)

PARAM_COMP_VEXT_64X_0 =             (124)
PARAM_COMP_VEXT_64X_1 =             (125)
PARAM_COMP_VEXT_64X_2 =             (126)
PARAM_COMP_VEXT_64X_3 =             (127)

PARAM_TEMPCO_VEXT_1X_GAIN =        (128)
PARAM_TEMPCO_VEXT_1X_T0 =          (129)

PARAM_TEMPCO_VEXT_8X_GAIN =        (130)
PARAM_TEMPCO_VEXT_8X_T0 =          (131)

PARAM_TEMPCO_VEXT_64X_GAIN =        (132)
PARAM_TEMPCO_VEXT_64X_T0 =          (133)


PARAM_COMPLIANCE_MODE =     (134)
PARAM_ASYNC_SWEEP_DWELL =   (135)
PARAM_SERIAL_NUMBER =       (136)
PARAM_FIRMWARE_VER =		    (137)
PARAM_UPTIME =			        (138)


DATA_PTR =             (139)
DATA_START =           (140)

PARAM_OUTPUT_STATE = (699)



DISABLE_4WIRE_MODE = 0
ENABLE_4WIRE_MODE = 1

GUARD_MODE_DRIVE = 0
GUARD_MODE_SENSE = 1

AUTORANGING_ON = 0
AUTORANGING_OFF = 1

MODE_TRIGGER_FREE =           (0)
MODE_TRIGGER_50Hz =           (1)
MODE_TRIGGER_60Hz =           (2)
MODE_TRIGGER_EDGE_SINGLE_1 =  (3)
MODE_TRIGGER_EDGE_SYNC_1 =    (4)
MODE_TRIGGER_EDGE_SINGLE_2 =  (5)
MODE_TRIGGER_EDGE_SYNC_2 =    (6)

MODE_TRIGGER_EDGE_SINGLE_12 = (7)
MODE_TRIGGER_EDGE_SYNC_12 =   (8)

SET_TRIGGER_1 =           (1)
SET_TRIGGER_2 =           (2)
SET_TRIGGER_12 =          (3)
RELEASE_TRIGGER_1 =       (4)
RELEASE_TRIGGER_2 =       (5)
RELEASE_TRIGGER_12 =      (6)

MODE_HEATER_OFF = 0
MODE_HEATER_AUTO = 1

MODE_TEMPCO_OFF =         (0)
MODE_TEMPCO_ON =          (1)

MODE_RETRIGGER_SINGLE =   (0)
MODE_RETRIGGER_BURST =    (1)
MODE_RETRIGGER_LOOP =     (2)
MODE_RETRIGGER_SWEEP =    (3)

MODE_PLC_SYNC_NONE =         (0)
MODE_PLC_SYNC_50HZ =         (1)
MODE_PLC_SYNC_60HZ =         (2)




ASYNC_IDLE =					(0)
ASYNC_M_WAIT_TRIGGER_EDGE = 	(1)
ASYNC_M_AUTORANGING =			(2)
ASYNC_M_WAIT_SYNC_TRIGGER =		(3)
ASYNC_M_PLC_SYNC =				(4)
ASYNC_M_READ_ADC =				(5)

ASYNC_DV_WAIT_TRIGGER_EDGE = 	(10)
ASYNC_DV_SET_DRIVE =			(11)

ASYNC_DC_WAIT_TRIGGER_EDGE = 	(20)
ASYNC_DC_SET_DRIVE =			(21)
ASYNC_DWELL =					(30)

ASYNC_CHANNEL_VOLTAGE =			(0)
ASYNC_CHANNEL_CURRENT =			(1)
ASYNC_CHANNEL_EXT =				(2)


MODE_COMPLIANCE_LIMIT =   (0)
MODE_COMPLIANCE_DISABLE_OUTPUT = (1)

OUTPUT_DISABLED =         (0)
OUTPUT_ENABLED =          (1)

LOW_CURRENT_MODE_OFF =   (0)
LOW_CURRENT_MODE_ON  =   (1)




# Functions to encode messages

def gen_write_msg( addr, key, value ):
	return struct.pack( ">BBIi", addr, OP_WRITE, key, value )

def gen_write_float_msg( addr, key, value ):
	return struct.pack( ">BBIf", addr, OP_WRITE, key, value )

def gen_read_msg( addr, key):
	return struct.pack( ">BBIi", addr, OP_READ, key, 0 )

def gen_action_msg( addr, action, key, value ):
	return struct.pack( ">BBIi", addr, action, key, value )

def gen_action_msg_float( addr, action, key, value ):
	return struct.pack( ">BBIf", addr, action, key, value )


def gen_action_msg( addr, action, key, value ):
	return struct.pack( ">BBIi", addr, action, key, value )
	
def gen_action_msg_mem( addr, action, key, value ):
	return struct.pack( ">BBII", addr, action, key, value )

def gen_action_msg_mem_float( addr, action, key, value ):
	return struct.pack( ">BBIf", addr, action, key, value )


# Functions to decode message

def decode_error( msg ):
	(addr, op, error, extra) = struct.unpack( ">BBIi", msg )
	return error, extra

def decode_read( msg ):
	(addr, op, key, value) = struct.unpack( ">BBIi", msg )
	return key, value

def decode_read_float( msg ):
	(addr, op, key, value) = struct.unpack( ">BBIf", msg )
	return key, value

def decode_action( msg ):
	(addr, op, key, value) = struct.unpack( ">BBIi", msg )
	return key, value

def decode_action_mem( msg ):
	(addr, op, key, value) = struct.unpack( ">BBII", msg )
	return key, value

def decode_action_mem_float( msg ):
	(addr, op, key, value) = struct.unpack( ">BBIf", msg )
	return key, value


def decode_header( msg ):
	(addr, op) = struct.unpack_from( ">BB", msg )
	
	return addr, op 

def decode_measure( msg ):
	(addr, op, voltage, current) = struct.unpack( ">BBff", msg )
	return voltage, current



class MemoryMap( object ):
	def __init__( self, device ):
		self.device = device
		self.addr0 = DATA_START
	
	def __getitem__(self, addr):
		return self.device.read_float( self.addr0 + addr )
	
	def __setitem__(self, addr, value):
		return self.device.write_float( self.addr0 + addr, value )
	



class Strix( object ):
	def __init__( self, com, address ):
		self.com = com
		self.address = address
		self.data = MemoryMap( self )
	

	def _clear_buffer( self ):
		if self.com.in_waiting > 0:
			self.com.read( self.com.in_waiting )

	def write( self, key, value ):
		self._clear_buffer()

		self.com.write( gen_write_msg( self.address, int(key), int(value) ) )
		response = self.com.read( 10 )
		addr, op = decode_header( response )
		if op == OP_ERROR:
			raise IndexError

	def write_float( self, key, value ):
		self._clear_buffer()
		
		self.com.write( gen_write_float_msg( self.address, int(key), value ) )
		response = self.com.read( 10 )
		addr, op = decode_header( response )
		if op == OP_ERROR:
			raise IndexError



	def read( self, key ):
		self._clear_buffer()
		
		self.com.write( gen_read_msg( self.address, int( key ) ) )
		response = self.com.read( 10 )
		#print(repr(response))
		addr, op = decode_header( response )
		if op == OP_ERROR:
			raise IndexError
		
		key, value = decode_read( response )
		return value

	def read_float( self, key ):
		self._clear_buffer()
		
		self.com.write( gen_read_msg( self.address, int( key ) ) )
		response = self.com.read( 10 )
		#print(repr(response))
		addr, op = decode_header( response )
		if op == OP_ERROR:
			raise IndexError
		
		key, value = decode_read_float( response )
		return value

	def mem_write( self, addr, value ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_mem( self.address, OP_I2C_MEM_W, addr, value ) )
		response = self.com.read( 10 )
		key, value = decode_action( response )
		return value 
	
	def mem_read( self, addr ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg( self.address, OP_I2C_MEM_R, addr, 0 ) )
		response = self.com.read( 10 )
		key, value = decode_action_mem( response )
		return value 


	def mem_write_float( self, addr, value ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_mem_float( self.address, OP_I2C_MEM_W, addr, value ) )
		response = self.com.read( 10 )
		key, value = decode_action( response )
		return value 
	
	def mem_read_float( self, addr ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg( self.address, OP_I2C_MEM_R, addr, 0 ) )
		response = self.com.read( 10 )
		key, value = decode_action_mem_float( response )
		return value 

	def set_drive_voltage( self, voltage ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_DRIVE_VOLTAGE, 0, voltage ) )
		response = self.com.read( 10 )
		key, value = decode_action( response )
		return value 

	def set_drive_current( self, current ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_DRIVE_CURRENT, 0, current ) )
		response = self.com.read( 10 )
		key, value = decode_action( response )
		return value 


	def measure( self ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_MEASURE, 0, 0 ) )
		response = self.com.read( 10 )
		voltage, current = decode_measure( response )
		return voltage, current

	def get_temperature( self ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_GET_TEMPERATURE, 0, 0 ) )
		response = self.com.read( 10 )
		key, value = decode_action( response )
		temp_driver = value * 0.0078125
		temp_adc = key * 0.03125
		return temp_driver, temp_adc
	
	def get_raw_voltages( self ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_RAW_VOLTAGES, 0, 0 ) )
		response = self.com.read( 10 )
		voltage, current = decode_measure( response )
		return voltage, current


	def measure_voltage( self ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_MEASURE_VOLTAGE, 0, 0 ) )
		response = self.com.read( 10 )
		voltage, current = decode_measure( response )
		return voltage
	
	def measure_current( self ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_MEASURE_CURRENT, 0, 0 ) )
		response = self.com.read( 10 )
		voltage, current = decode_measure( response )
		return current

	def _read_raw_adc( self, cfg ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg( self.address, OP_RAW_ADC, cfg, 0 ) )
		response = self.com.read( 10 )
		key, value = decode_action( response )
		return key, value


	def measure_ext( self ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_MEASURE_EXT, 0, 0 ) )
		response = self.com.read( 10 )
		voltage, current = decode_measure( response )
		return voltage

	def async_set_drive_voltage( self, voltage ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_ASYNC_DRIVE_VOLTAGE, 0, voltage ) )
		response = self.com.read( 10 )
		key, value = decode_action( response )
		return value 

	def async_set_drive_current( self, current ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_ASYNC_DRIVE_CURRENT, 0, current ) )
		response = self.com.read( 10 )
		key, value = decode_action( response )
		return value 

	def async_set_drive_current( self, current ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_ASYNC_DRIVE_CURRENT, 0, current ) )
		response = self.com.read( 10 )
		key, value = decode_action( response )
		return value 


	def is_async_done( self ):
		async_state = self.read( PARAM_ASYNC_STATE )
		return async_state == ASYNC_IDLE


	def async_measure_voltage( self ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_ASYNC_MEASURE_VOLTAGE, 0, 0 ) )
		response = self.com.read( 10 )
		voltage, current = decode_measure( response )
		
	def async_measure_current( self ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_ASYNC_MEASURE_CURRENT, 0, 0 ) )
		response = self.com.read( 10 )
		voltage, current = decode_measure( response )

	def async_measure_ext( self ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_ASYNC_MEASURE_EXT, 0, 0 ) )
		response = self.com.read( 10 )
		voltage, current = decode_measure( response )

	def async_start_sweep( self, read_channel, write_channel  ):
		self._clear_buffer()
		
		self.com.write( gen_action_msg_float( self.address, OP_ASYNC_START_SWEEP, read_channel, write_channel ) )
		response = self.com.read( 10 )
		voltage, current = decode_measure( response )

	def enable_output( self, output_state ):
		self._clear_buffer()
		
		if output_state:
			self.com.write( gen_action_msg( self.address, OP_SET_OUTPUT, 1, 1 ) )
		else:
			self.com.write( gen_action_msg( self.address, OP_SET_OUTPUT, 0, 0 ) )
			
		response = self.com.read( 10 )
		key, value = decode_action( response )
	
	def set_low_current_mode( self, mode ):
		self._clear_buffer()
		
		if mode:
			self.com.write( gen_action_msg( self.address, OP_SET_LOW_CURRENT_MODE, 1, 1 ) )
		else:
			self.com.write( gen_action_msg( self.address, OP_SET_LOW_CURRENT_MODE, 0, 0 ) )
			
		response = self.com.read( 10 )
		key, value = decode_action( response )
