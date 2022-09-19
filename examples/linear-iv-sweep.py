#!/usr/bin/env python3


import sys
import serial
import time

import libStrix

# Open connection to SMU
com = serial.Serial( sys.argv[1], 460800, timeout = 25.0 )
smu = libStrix.Strix( com, 1 )

# Settings 
smu.write( libStrix.PARAM_AVERAGES, 5 )
smu.write( libStrix.PARAM_AUTORANGING, libStrix.AUTORANGING_ON )

# Sweep paramters
v_start = -5.0
v_stop = 5.0    
dV = 0.1

N = int( abs(v_start - v_stop) / dV ) + 1

# Perform measurements 
smu.enable_output( True )


for i in range( N + 1 ):
    
    q = i / N
    v = v_start * ( 1 - q ) + v_stop * q
    
    smu.set_drive_voltage( v )

    v_meas = smu.measure_voltage() 
    i_meas = smu.measure_current()

    print( v_meas, i_meas )

smu.enable_output( False )
    
com.close()