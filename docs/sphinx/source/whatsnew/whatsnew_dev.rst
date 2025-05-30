
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
* Removes FrequenciesAC from ACInput, ACOutput, InverterOutput

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