#!/usr/bin/env python3


import sys
import serial
import time

import numpy as np
import scipy.optimize

import libStrix


# Open connection to SMU
com = serial.Serial( sys.argv[1], 460800, timeout = 25.0 )
smu = libStrix.Strix( com, 1 )



## Settings 
smu.write( libStrix.PARAM_AVERAGES, 5 )
smu.write( libStrix.PARAM_AUTORANGING, libStrix.AUTORANGING_ON )



# Voltage sweep range
v_start = -1.0
v_stop = 0.7    


# Generate sweep voltages
v_points = []

dV = 0.05
v_cur = v_start
while v_cur < 0.3:
    v_points.append( v_cur )
    v_cur += dV

# Finer stepping near diode forward voltage
dV = 0.005
while v_cur < v_stop:
    v_points.append( v_cur )
    v_cur += dV


Vmeas = []
Imeas = []


# Perform measurments

for vset in v_points:
    smu.set_drive_voltage( vset )
    i_meas = smu.measure_current()

    Vmeas.append( vset )
    Imeas.append( i_meas )

smu.set_drive_voltage( 0 )


# Diode model
def shockley( V, Is, n, Rl):
    T = 273.15 + 27
    q = 1.602176634e-19
    k = 1.380649e-23
    return Is * ( np.exp( q * V / ( n*k*T ) ) - 1 ) + V / Rl

# Fit model to data
popt, pcov = scipy.optimize.curve_fit(shockley, Vmeas, Imeas)

# Estimate series resistance
I_sh0 = shockley(-1e-3, *popt)
I_sh1 = shockley(1e-3, *popt)

dIdV = (I_sh1 - I_sh0)/2e-3

Rs = 1 / dIdV


# Show results
print( "Is: %.2f nA" % ( popt[0]*1e9) )
print( "n:  %.2f "% ( popt[1] ) )
print( "Rl: %.2f Gohm "% ( popt[2]/1e9 ) )
print( "Rs: %.2f Mohm" % (Rs/1e6))


com.close()