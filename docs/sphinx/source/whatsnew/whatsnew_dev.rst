
.. _whatsnew_dev:

XXXX.0.0
--------

Element changes
~~~~~~~~~~~~~~~
* Removes InterconnectionPhase, InterconnectionPhaseType. These elements are replaced by PowerPhase and PowerPhaseType.
* Removes FrequencyAC and FrequenciesAC. These elements are replaced by LineFrequency and LineFrequencies.

Object changes
~~~~~~~~~~~~~~
* Adds VoltageTS, VoltageTSArray, EnergyTS, EnergyTSArray, PowerTS, PowerTSArray, CurrentTS, CurrentTSArray, ElectricalTS, LineFrequencies
* Removes FrequenciesAC from ACInput, ACOutput, 
* Removes InverterOutput, InverterOutputs 
* Adds HumidityRelativeTS, HumidityRelativeTSArray
* Adds PressureAtmosphericTS, PressureAtmosphericTSArray
* Adds IrradianceTS, IrradianceTSArray
* Adds WinddirectionTS, WinddirectionTSArray

Unit changes
~~~~~~~~~~~~
* Adds VoltagePhaseItemType, PowerTypeItemType, LineFrequencyItemType, VoltagePhaseItemType

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