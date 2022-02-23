#!/usr/bin/env python

import sys
import serial
import libStrix
import libKeysight
import numpy as np
import time
import json

com = serial.Serial( sys.argv[1], 460800, timeout = 1.0 )

smu = libStrix.Strix( com, 1 )


data = {}
with open( sys.argv[2], 'r') as handle:
    data = json.load( handle )





if "div10" in data:
    smu.write_float( 20, data["div10"][0] )
    smu.write_float( 21, data["div10"][1] )
    smu.write_float( 22, data["div10"][2] )
    smu.write_float( 23, data["div10"][3] )

if "1x" in data:
    smu.write_float( 24, data["1x"][0] )
    smu.write_float( 25, data["1x"][1] )
    smu.write_float( 26, data["1x"][2] )
    smu.write_float( 27, data["1x"][3] )

if "10x" in data:
    smu.write_float( 28, data["10x"][0] )
    smu.write_float( 29, data["10x"][1] )
    smu.write_float( 30, data["10x"][2] )
    smu.write_float( 31, data["10x"][3] )


if "vmeas_1x" in data:
    smu.write_float( 32, data["vmeas_1x"][0] )
    smu.write_float( 33, data["vmeas_1x"][1] )
    smu.write_float( 34, data["vmeas_1x"][2] )
    smu.write_float( 35, data["vmeas_1x"][3] )

if "vmeas_8x" in data:
    smu.write_float( 36, data["vmeas_8x"][0] )
    smu.write_float( 37, data["vmeas_8x"][1] )
    smu.write_float( 38, data["vmeas_8x"][2] )
    smu.write_float( 39, data["vmeas_8x"][3] )

if "vmeas_64x" in data:
    smu.write_float( 40, data["vmeas_64x"][0] )
    smu.write_float( 41, data["vmeas_64x"][1] )
    smu.write_float( 42, data["vmeas_64x"][2] )
    smu.write_float( 43, data["vmeas_64x"][3] )


if "imeas_1" in data:
    smu.write_float( 44, data["imeas_1"][0] )
    smu.write_float( 45, data["imeas_1"][1] )
    smu.write_float( 46, data["imeas_1"][2] )
    smu.write_float( 47, data["imeas_1"][3] )

if "imeas_2" in data:
    smu.write_float( 48, data["imeas_2"][0] )
    smu.write_float( 49, data["imeas_2"][1] )
    smu.write_float( 50, data["imeas_2"][2] )
    smu.write_float( 51, data["imeas_2"][3] )

if "imeas_3" in data:
    smu.write_float( 52, data["imeas_3"][0] )
    smu.write_float( 53, data["imeas_3"][1] )
    smu.write_float( 54, data["imeas_3"][2] )
    smu.write_float( 55, data["imeas_3"][3] )

if "imeas_4" in data:
    smu.write_float( 56, data["imeas_4"][0] )
    smu.write_float( 57, data["imeas_4"][1] )
    smu.write_float( 58, data["imeas_4"][2] )
    smu.write_float( 59, data["imeas_4"][3] )


if "idrive_1" in data:
    smu.write_float( 60, data["idrive_1"][0] )
    smu.write_float( 61, data["idrive_1"][1] )
    smu.write_float( 62, data["idrive_1"][2] )
    smu.write_float( 63, data["idrive_1"][3] )

if "idrive_2" in data:
    smu.write_float( 64, data["idrive_2"][0] )
    smu.write_float( 65, data["idrive_2"][1] )
    smu.write_float( 66, data["idrive_2"][2] )
    smu.write_float( 67, data["idrive_2"][3] )

if "idrive_3" in data:
    smu.write_float( 68, data["idrive_3"][0] )
    smu.write_float( 69, data["idrive_3"][1] )
    smu.write_float( 70, data["idrive_3"][2] )
    smu.write_float( 71, data["idrive_3"][3] )

if "idrive_4" in data:
    smu.write_float( 72, data["idrive_4"][0] )
    smu.write_float( 73, data["idrive_4"][1] )
    smu.write_float( 74, data["idrive_4"][2] )
    smu.write_float( 75, data["idrive_4"][3] )
