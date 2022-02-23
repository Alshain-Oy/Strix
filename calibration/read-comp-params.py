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

params = {}

params["div10"] = []
params["div10"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_DIV10_0 ) )
params["div10"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_DIV10_1 ) )
params["div10"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_DIV10_2 ) )
params["div10"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_DIV10_3 ) )


params["1x"] = []
params["1x"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_1X_0 ) )
params["1x"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_1X_1 ) )
params["1x"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_1X_2 ) )
params["1x"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_1X_3 ) )


params["10x"] = []
params["10x"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_10X_0 ) )
params["10x"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_10X_1 ) )
params["10x"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_10X_2 ) )
params["10x"].append( smu.read_float( libStrix.PARAM_COMP_VDRIVE_10X_3 ) )

params["vmeas_1x"] = []
params["vmeas_1x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_1X_0 ) )
params["vmeas_1x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_1X_1 ) )
params["vmeas_1x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_1X_2 ) )
params["vmeas_1x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_1X_3 ) )

params["vmeas_8x"] = []
params["vmeas_8x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_8X_0 ) )
params["vmeas_8x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_8X_1 ) )
params["vmeas_8x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_8X_2 ) )
params["vmeas_8x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_8X_3 ) )

params["vmeas_64x"] = []
params["vmeas_64x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_64X_0 ) )
params["vmeas_64x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_64X_1 ) )
params["vmeas_64x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_64X_2 ) )
params["vmeas_64x"].append( smu.read_float( libStrix.PARAM_COMP_VMEAS_64X_3 ) )

params["imeas_1"] = []
params["imeas_1"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_1_0 ) )
params["imeas_1"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_1_1 ) )
params["imeas_1"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_1_2 ) )
params["imeas_1"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_1_3 ) )

params["imeas_2"] = []
params["imeas_2"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_2_0 ) )
params["imeas_2"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_2_1 ) )
params["imeas_2"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_2_2 ) )
params["imeas_2"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_2_3 ) )

params["imeas_3"] = []
params["imeas_3"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_3_0 ) )
params["imeas_3"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_3_1 ) )
params["imeas_3"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_3_2 ) )
params["imeas_3"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_3_3 ) )

params["imeas_4"] = []
params["imeas_4"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_4_0 ) )
params["imeas_4"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_4_1 ) )
params["imeas_4"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_4_2 ) )
params["imeas_4"].append( smu.read_float( libStrix.PARAM_COMP_IMEAS_4_3 ) )

params["idrive_1"] = []
params["idrive_1"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_1_0 ) )
params["idrive_1"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_1_1 ) )
params["idrive_1"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_1_2 ) )
params["idrive_1"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_1_3 ) )

params["idrive_2"] = []
params["idrive_2"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_2_0 ) )
params["idrive_2"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_2_1 ) )
params["idrive_2"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_2_2 ) )
params["idrive_2"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_2_3 ) )

params["idrive_3"] = []
params["idrive_3"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_3_0 ) )
params["idrive_3"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_3_1 ) )
params["idrive_3"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_3_2 ) )
params["idrive_3"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_3_3 ) )

params["idrive_4"] = []
params["idrive_4"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_4_0 ) )
params["idrive_4"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_4_1 ) )
params["idrive_4"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_4_2 ) )
params["idrive_4"].append( smu.read_float( libStrix.PARAM_COMP_IDRIVE_4_3 ) )


print( json.dumps( params, indent = 2))