
.. _whatsnew_dev:

XXXX.0.0
--------

Element changes
~~~~~~~~~~~~~~~
* Remove InterconnectionPhase, InterconnectionPhaseType. These elements are replaced by PowerPhase and PowerPhaseType.
* Remove FrequencyAC and FrequenciesAC. These elements are replaced by LineFrequency and LineFrequencies.
* Remove OrientationAzimuth and OrientationTilt. These elements are duplicative of Azimuth and Tilt.
* Rename Roll to Rotation.

Object changes
~~~~~~~~~~~~~~
* Add VoltageTS, VoltageTSArray, EnergyTS, EnergyTSArray, PowerTS, PowerTSArray, CurrentTS, CurrentTSArray, ElectricalTS, LineFrequencies
* Remove FrequenciesAC from ACInput, ACOutput, 
* Remove InverterOutput, InverterOutputs 
* Add HumidityRelativeTS, HumidityRelativeTSArray
* Add PressureAtmosphericTS, PressureAtmosphericTSArray
* Add IrradianceTS, IrradianceTSArray
* Add WinddirectionTS, WinddirectionTSArray
* Add WindspeedTS, WindspeedTSArray
* Add TemperatureTS, TemperatureTSArray
* Add SnowfallTS, SnowfallTSArray
* Add RainfallTS, RainfallTSArray
* Remove OrientationInformation, duplicative of Orientation

Unit changes
~~~~~~~~~~~~
* Add VoltagePhaseItemType, PowerTypeItemType, LineFrequencyItemType, VoltagePhaseItemType

Bug fixes
~~~~~~~~~

Testing
~~~~~~~

Documentation
~~~~~~~~~~~~~

Contributors
~~~~~~~~~~~~
* Kevin Kirkley (kevinkirkl3y)
* Dan Kubler (DanKub-BB)
* Cliff Hansen (cwhanse)