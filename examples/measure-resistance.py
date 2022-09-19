#!/usr/bin/env python3


import sys
import serial
import time

import libStrix

# Open connection to SMU
com = serial.Serial( sys.argv[1], 460800, timeout = 25.0 )
smu = libStrix.Strix( com, 1 )

## Settings 
smu.write( libStrix.PARAM_AVERAGES, 10 )
smu.write( libStrix.PARAM_4WIRE_MODE, libStrix.ENABLE_4WIRE_MODE )


# Examples for test current
# R < 100 Ω -> 10 mA
# R ~ 1 kΩ -> 1 mA 
# R ~ 10 kΩ -> 100 µA
# R ~ 100 kΩ -> 10 µA
# R > 100kΩ -> use voltage drive

# for measuring small resistances
test_current = 10e-3


# Measure voltage (and current) with two test currents
smu.enable_output( True )


smu.set_drive_current( -test_current )
time.sleep(0.25)
v0 = smu.measure_voltage()
i0 = smu.measure_current()

smu.set_drive_current( test_current )
time.sleep(0.25)
v1 = smu.measure_voltage()
i1 = smu.measure_current()

smu.enable_output( False )


# Compute resistance
dV = v1 - v0
dI = i1 - i0

R = dV / dI

print( "R: %.2e ohm" % R )



com.close()