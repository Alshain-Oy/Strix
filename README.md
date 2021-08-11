# Strix
Strix SMU scripts &amp; libraries


## Quickstart

1) Connect usb data cable to _Data in_ port
2) Connect power adapter to Strix

```python
import libStrix
import serial

# replace "COM3" with corresponding port on your computer
com = serial.Serial( "COM3", 460800, timeout = 10.0 )

# Connect to SMU with address = 1 (default)
smu = libStrix.Strix( com, 1 )

# Measure both voltage and current
voltage, current = smu.measure()
```
