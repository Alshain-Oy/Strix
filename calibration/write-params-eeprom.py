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
    smu.mem_write_float( 16, data["div10"][0] )
    smu.mem_write_float( 20, data["div10"][1] )
    smu.mem_write_float( 24, data["div10"][2] )
    smu.mem_write_float( 28, data["div10"][3] )

if "1x" in data:
    smu.mem_write_float( 32, data["1x"][0] )
    smu.mem_write_float( 36, data["1x"][1] )
    smu.mem_write_float( 40, data["1x"][2] )
    smu.mem_write_float( 44, data["1x"][3] )

if "10x" in data:
    smu.mem_write_float( 48, data["10x"][0] )
    smu.mem_write_float( 52, data["10x"][1] )
    smu.mem_write_float( 56, data["10x"][2] )
    smu.mem_write_float( 60, data["10x"][3] )

if "vmeas_1x" in data:
    smu.mem_write_float( 64, data["vmeas_1x"][0] )
    smu.mem_write_float( 68, data["vmeas_1x"][1] )
    smu.mem_write_float( 72, data["vmeas_1x"][2] )
    smu.mem_write_float( 76, data["vmeas_1x"][3] )

if "vmeas_8x" in data:
    smu.mem_write_float( 80, data["vmeas_8x"][0] )
    smu.mem_write_float( 84, data["vmeas_8x"][1] )
    smu.mem_write_float( 88, data["vmeas_8x"][2] )
    smu.mem_write_float( 92, data["vmeas_8x"][3] )

if "vmeas_64x" in data:
    smu.mem_write_float( 96, data["vmeas_64x"][0] )
    smu.mem_write_float( 100, data["vmeas_64x"][1] )
    smu.mem_write_float( 104, data["vmeas_64x"][2] )
    smu.mem_write_float( 108, data["vmeas_64x"][3] )


if "imeas_1" in data:
    smu.mem_write_float( 112, data["imeas_1"][0] )
    smu.mem_write_float( 116, data["imeas_1"][1] )
    smu.mem_write_float( 120, data["imeas_1"][2] )
    smu.mem_write_float( 124, data["imeas_1"][3] )

if "imeas_2" in data:
    smu.mem_write_float( 128, data["imeas_2"][0] )
    smu.mem_write_float( 132, data["imeas_2"][1] )
    smu.mem_write_float( 136, data["imeas_2"][2] )
    smu.mem_write_float( 140, data["imeas_2"][3] )

if "imeas_3" in data:
    smu.mem_write_float( 144, data["imeas_3"][0] )
    smu.mem_write_float( 148, data["imeas_3"][1] )
    smu.mem_write_float( 152, data["imeas_3"][2] )
    smu.mem_write_float( 156, data["imeas_3"][3] )

if "imeas_4" in data:
    smu.mem_write_float( 160, data["imeas_4"][0] )
    smu.mem_write_float( 164, data["imeas_4"][1] )
    smu.mem_write_float( 168, data["imeas_4"][2] )
    smu.mem_write_float( 172, data["imeas_4"][3] )

if "idrive_1" in data:
    smu.mem_write_float( 176, data["idrive_1"][0] )
    smu.mem_write_float( 180, data["idrive_1"][1] )
    smu.mem_write_float( 184, data["idrive_1"][2] )
    smu.mem_write_float( 188, data["idrive_1"][3] )

if "idrive_2" in data:
    smu.mem_write_float( 192, data["idrive_2"][0] )
    smu.mem_write_float( 196, data["idrive_2"][1] )
    smu.mem_write_float( 200, data["idrive_2"][2] )
    smu.mem_write_float( 204, data["idrive_2"][3] )

if "idrive_3" in data:
    smu.mem_write_float( 208, data["idrive_3"][0] )
    smu.mem_write_float( 212, data["idrive_3"][1] )
    smu.mem_write_float( 216, data["idrive_3"][2] )
    smu.mem_write_float( 220, data["idrive_3"][3] )

if "idrive_4" in data:
    smu.mem_write_float( 224, data["idrive_4"][0] )
    smu.mem_write_float( 228, data["idrive_4"][1] )
    smu.mem_write_float( 232, data["idrive_4"][2] )
    smu.mem_write_float( 236, data["idrive_4"][3] )


if "vext_1x" in data:
    smu.mem_write_float( 352, data["vext_1x"][0] )
    smu.mem_write_float( 356, data["vext_1x"][1] )
    smu.mem_write_float( 360, data["vext_1x"][2] )
    smu.mem_write_float( 364, data["vext_1x"][3] )

if "vext_8x" in data:
    smu.mem_write_float( 368, data["vext_8x"][0] )
    smu.mem_write_float( 372, data["vext_8x"][1] )
    smu.mem_write_float( 376, data["vext_8x"][2] )
    smu.mem_write_float( 380, data["vext_8x"][3] )

if "vext_64x" in data:
    smu.mem_write_float( 384, data["vext_64x"][0] )
    smu.mem_write_float( 388, data["vext_64x"][1] )
    smu.mem_write_float( 392, data["vext_64x"][2] )
    smu.mem_write_float( 396, data["vext_64x"][3] )

if "4w_meas" in data:
    smu.mem_write_float( 424, data["4w_vmeas"][0] )
    smu.mem_write_float( 428, data["4w_vmeas"][1] )
    smu.mem_write_float( 432, data["4w_vmeas"][2] )
    smu.mem_write_float( 436, data["4w_vmeas"][3] )

if "4w_drive" in data:
    smu.mem_write_float( 440, data["4w_vdrive"][0] )
    smu.mem_write_float( 444, data["4w_vdrive"][1] )
    smu.mem_write_float( 448, data["4w_vdrive"][2] )
    smu.mem_write_float( 452, data["4w_vdrive"][3] )



### empty tempcos

smu.mem_write_float( 240, 0.0 )
smu.mem_write_float( 244, 0.0 )

smu.mem_write_float( 248, 0.0 )
smu.mem_write_float( 252, 0.0 )

smu.mem_write_float( 256, 0.0 )
smu.mem_write_float( 260, 0.0 )

smu.mem_write_float( 264, 0.0 )
smu.mem_write_float( 268, 0.0 )

smu.mem_write_float( 272, 0.0 )
smu.mem_write_float( 276, 0.0 )

smu.mem_write_float( 280, 0.0 )
smu.mem_write_float( 284, 0.0 )

smu.mem_write_float( 288, 0.0 )
smu.mem_write_float( 292, 0.0 )

smu.mem_write_float( 296, 0.0 )
smu.mem_write_float( 300, 0.0 )

smu.mem_write_float( 304, 0.0 )
smu.mem_write_float( 308, 0.0 )

smu.mem_write_float( 312, 0.0 )
smu.mem_write_float( 316, 0.0 )

smu.mem_write_float( 320, 0.0 )
smu.mem_write_float( 324, 0.0 )

smu.mem_write_float( 328, 0.0 )
smu.mem_write_float( 332, 0.0 )

smu.mem_write_float( 336, 0.0 )
smu.mem_write_float( 340, 0.0 )

smu.mem_write_float( 344, 0.0 )
smu.mem_write_float( 348, 0.0 )

smu.mem_write_float( 400, 0.0 )
smu.mem_write_float( 404, 0.0 )

smu.mem_write_float( 408, 0.0 )
smu.mem_write_float( 412, 0.0 )

smu.mem_write_float( 416, 0.0 )
smu.mem_write_float( 420, 0.0 )

smu.mem_write_float( 456, 0.0 )
smu.mem_write_float( 460, 0.0 )

smu.mem_write_float( 464, 0.0 )
smu.mem_write_float( 468, 0.0 )
