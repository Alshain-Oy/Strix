#!/usr/bin/env python3

from . import libStrix
import serial

from qcodes.instrument.parameter import Parameter
from qcodes.instrument import Instrument
from qcodes.utils import validators as vals

_COM_PORTS = {}


class AlshainStrix( Instrument ):
    def __init__(self, name, address, **kwargs):
        global _COM_PORTS
        super().__init__(name, **kwargs)
        parts = address.split("::")
        self._comport = parts[0].replace("ASRL", "COM")
        self._strix_id = int( parts[1] )

        if self._comport not in _COM_PORTS:
            self._com = serial.Serial( self._comport, 460800, timeout = 2.5 )
            _COM_PORTS[self._comport] = self._com
        else:
            self._com = _COM_PORTS[self._comport]
        self._smu = libStrix.Strix( self._com, self._strix_id )


        self.voltage = Parameter(
            "voltage",
            unit = "V",
            set_cmd = self._set_voltage,
            get_cmd = self._get_voltage,
            label = "Voltage",
            vals=vals.Numbers(min_value=-21.5, max_value=21.5),
            instrument = self,
        )

        self.current = Parameter(
            "current",
            unit = "A",
            set_cmd = self._set_current,
            get_cmd = self._get_current,
            label = "Current",
            vals=vals.Numbers(min_value=-21.5, max_value=21.5),
            instrument = self,
        )

        self.ext_voltage = Parameter(
            "ext_voltage",
            unit = "V",
            set_cmd = self._set_ext_voltage,
            get_cmd = self._get_ext_voltage,
            label = "Ext voltage",
            vals=vals.Numbers(min_value=-2.6, max_value=2.6),
            instrument = self,
        )

        self.output = Parameter(
            "output",
            get_cmd=self._get_output,
            set_cmd=self._set_output,
            instrument=self,
            vals=vals.Bool(),
            docstring="Output enable",
        )

        self.averages = Parameter(
            "averages",
            get_cmd=self._get_averaging,
            set_cmd=self._set_averaging,
            instrument=self,
            vals=vals.Ints(min_value=1, max_value=100),
            docstring="Number of averages per measurement",
        )

        self.autoranging = Parameter(
            "autoranging",
            get_cmd=self._get_autoranging,
            set_cmd=self._set_autoranging,
            vals=vals.Bool(),
            instrument=self,
            docstring="Autoranging enabled",
        )

        self.voltage_fixed_gain = Parameter(
            "voltage_fixed_gain",
            get_cmd=self._get_voltage_fixed_gain,
            set_cmd=self._set_voltage_fixed_gain,
            vals = vals.Enum(1, 8, 64),
            instrument=self,
            docstring="Fixed gain for voltage measurement, 1 = 17V, 8 = 2.5V, 64 = 300mV",
        )
        
        self.current_fixed_range = Parameter(
            "current_fixed_range",
            get_cmd=self._get_current_fixed_range,
            set_cmd=self._set_current_fixed_range,
            vals = vals.Enum(1, 2, 3, 4),
            instrument=self,
            docstring="Fixed range for current measurement, 1 = 17mA, 2 = 100uA, 3 = 1uA, 4 = 10nA",
        )
        
        self.ext_voltage_fixed_gain = Parameter(
            "ext_voltage_fixed_gain",
            get_cmd=self._get_ext_fixed_gain,
            set_cmd=self._set_ext_fixed_gain,
            vals = vals.Enum(1, 8, 64),
            instrument=self,
            docstring="Fixed gain for ext voltage measurement, 1 = 2.5V, 8 = 125mV, 64 = 35mV",
        )
        
        self.heater_mode = Parameter( 
            "heater_mode",
            get_cmd=self._get_heater_mode,
            set_cmd=self._set_heater_mode,
            vals=vals.Bool(),
            instrument=self,
            docstring="Internal heater control -> enabled or not",
        )

        self.heater_state = Parameter(
            "heater_state",
            get_cmd=self._get_heater_state,
            set_cmd=self._set_heater_state,
            vals=vals.Bool(),
            instrument=self,
            docstring="Current internal heater state (heating or not)",
        )

        self.temperature_adc = Parameter(
            "temperature_adc",
            get_cmd=self._get_temperature_adc,
            set_cmd=self._set_temperature,
            unit = "degC",
            label = "Temperature",
            docstring="Temperature of the ADC",

        )

        self.temperature_drive = Parameter(
            "temperature_drive",
            get_cmd=self._get_temperature_drive,
            set_cmd=self._set_temperature,
            unit = "degC",
            label = "Temperature",
            docstring="Temperature of the drive circuitry",

        )

        self.compliance_voltage = Parameter(
            "compliance_voltage",
            unit="V",
            get_cmd=self._get_compliance_voltage,
            set_cmd=self._set_compliance_voltage,
            label="Compliance voltage",
            vals=vals.Numbers(min_value=-21.5, max_value=21.5),
            docstring="Compliance voltage limit",
        )

        self.compliance_current = Parameter(
            "compliance_current",
            unit="A",
            get_cmd=self._get_compliance_current,
            set_cmd=self._set_compliance_current,
            label="Compliance current",
            vals=vals.Numbers(min_value=-21.5, max_value=21.5),
            docstring="Compliance current limit",
        )

        self.fourwire_mode = Parameter(
            "fourwire_mode",
            get_cmd=self._get_fourwire_mode,
            set_cmd=self._set_fourwire_mode,
            vals=vals.Bool(),
            docstring="Is four-wire mode enabled",
        )

    def _set_voltage( self, voltage ):
        self._smu.set_drive_voltage( voltage )
    
    def _get_voltage( self ):
        return self._smu.measure_voltage()
    
    def _set_current( self, current ):
        self._smu.set_drive_current( current )
    
    def _get_current( self ):
        return self._smu.measure_current()
    
    def _set_output( self, value ):
        if value:
            self._smu.enable_output( True )
        else:
            self._smu.enable_output( False )
    
    def _get_output( self ):
        self._smu.read( libStrix.PARAM_OUTPUT_STATE ) == libStrix.OUTPUT_ENABLED
    
    def _set_averaging( self, Navg ):
        self._smu.write( libStrix.PARAM_AVERAGES, Navg )
    
    def _get_averaging( self ):
        return self._smu.read( libStrix.PARAM_AVERAGES )
    
    def _set_autoranging( self, state ):
        if state:
            self._smu.write( libStrix.PARAM_AUTORANGING, libStrix.AUTORANGING_ON )
        else:
            self._smu.write( libStrix.PARAM_AUTORANGING, libStrix.AUTORANGING_OFF )

    def _get_autoranging( self ):
        state = self._smu.read( libStrix.PARAM_AUTORANGING )
        
        if state == libStrix.AUTORANGING_ON:
            return True
        else:
            return False
    
    def _set_ext_voltage( self, value ):
        pass

    def _get_ext_voltage( self ):
        return self._smu.measure_ext()

    def _set_voltage_fixed_gain( self, value ):
        self._smu.write( libStrix.PARAM_ADC_VOLTAGE_GAIN, value )
    
    def _get_voltage_fixed_gain( self ):
        return self._smu.read( libStrix.PARAM_ADC_VOLTAGE_GAIN )
    
    def _set_current_fixed_range( self, value ):
        self._smu.write( libStrix.PARAM_LARGE_CURRENT_GAIN, value )
    
    def _get_current_fixed_range( self ):
        return self._smu.read( libStrix.PARAM_LARGE_CURRENT_GAIN )
    
    def _set_ext_fixed_gain( self, value ):
        self._smu.write( libStrix.PARAM_EXT_VOLTAGE_GAIN, value )
    
    def _get_ext_fixed_gain( self ):
        return self._smu.read( libStrix.PARAM_EXT_VOLTAGE_GAIN )
    
    def _set_heater_mode( self, value ):
        if value:
            self._smu.write( libStrix.PARAM_THERMAL_MODE, libStrix.MODE_HEATER_AUTO )
        else:
            self._smu.write( libStrix.PARAM_THERMAL_MODE, libStrix.MODE_HEATER_OFF )
    
    def _get_heater_mode( self ):
        mode = self._smu.read( libStrix.PARAM_THERMAL_MODE )
        if mode == libStrix.MODE_HEATER_AUTO:
            return True
        else:
            return False
    
    def _get_heater_state( self ):
        return self._smu.read( libStrix.PARAM_HEATER_STATE ) == 1

    def _set_heater_state( self, value ):
        pass
    
    def _get_temperature_adc( self ):
        T_drive, T_adc = self._smu.get_temperature()
        return T_adc

    def _get_temperature_drive( self ):
        T_drive, T_adc = self._smu.get_temperature()
        return T_drive

    def _set_temperature( self, value ):
        pass 

    def _set_compliance_voltage( self, value ):
        self._smu.write_float( libStrix.PARAM_COMPLIANCE_VOLTAGE, value )
    
    def _get_compliance_voltage( self ):
        return self._smu.read_float( libStrix.PARAM_COMPLIANCE_VOLTAGE )
    
    def _set_compliance_current( self, value ):
        self._smu.write_float( libStrix.PARAM_COMPLIANCE_CURRENT, value )
    
    def _get_compliance_current( self ):
        return self._smu.read_float( libStrix.PARAM_COMPLIANCE_CURRENT )
    
    def _set_fourwire_mode( self, value ):
        if value:
            self._smu.write( libStrix.PARAM_4WIRE_MODE, libStrix.ENABLE_4WIRE_MODE )
        else:
            self._smu.write( libStrix.PARAM_4WIRE_MODE, libStrix.DISABLE_4WIRE_MODE )
    
    def _get_fourwire_mode( self ):
        state = self._smu.read( libStrix.PARAM_4WIRE_MODE )
        if state == libStrix.ENABLE_4WIRE_MODE:
            return True
        else:
            return False