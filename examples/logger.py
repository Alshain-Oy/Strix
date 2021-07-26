#!/usr/bin/env python3


import sys
import serial
import time
import math
import libStrix



# Open connection to SMU
com = serial.Serial( sys.argv[1], 460800, timeout = 25.0 )
smu = libStrix.Strix( com, 1 )

## Settings 
smu.write( libStrix.PARAM_AVERAGES, 1 )

# Delay between two measurements
t_dwell = 1.0

# Filename for logfile as the second command line parameter
logfile = sys.argv[2]


# Write timestamp to first line
with open( logfile, 'w' ) as handle:
    print( "# %s" % time.strftime("%Y%m%d %H:%M:S"), file = handle )


N = 0
t_start = time.time()


try:
    while True:
        # Compute timestamp
        t_now = time.time()
        t_diff = t_now - t_start
        t_fractional = t_now - math.floor( t_now ) 
        
        ts_clock = time.strftime( "%H:%M:%S") + ".%.3f" % t_fractional

        # Measure voltage (as an example)
        V = smu.measure_voltage()

        # Format output line
        line = '%i, "%s", %.3f, %f' % (N, ts_clock, t_diff, V )

        # Print it to terminal
        print( line )

        # Append to log file
        with open( logfile, 'a' ) as handle:
            print( line, file = handle )

        # Wait until next round
        time.sleep( t_dwell )
        N += 1

except KeyboardInterrupt:
    pass






com.close()