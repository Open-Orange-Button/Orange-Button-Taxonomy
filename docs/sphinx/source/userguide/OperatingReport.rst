OperatingReport
===============

An instance of OperatingReport contains a summary of operating and financial data for a period of time. The report offers both summary and more detailed reporting elements.

Summary elements include:

* EnergyAC - the total AC energy generated during the period. Use the primitives EnergyAC.StartTime and EnergyAC.EndTime to define the period of time.
* EnergyACCurtailed - AC energy that could have been generated, but was not, due to limitations of the PV system or external factors such as grid outages.
* Insolation - the total irradiation recieved.
* Scope identifies the scope of the operating report (e.g., portfolio, system, device).

Detailed elements include:

* AvailabilityReport - allows for reporting availability metrics.
* * AvailabilityStandard can indicate a document describing the calculation of the availability metrics.
* * Scope identifies the scope of the availability calculation (e.g., portfolio, system, device).
* * Availabilities is an array of the element Availability. For each entry in the array, you can record several availability metrics and data supporting the calculation of the metrics.

* Production - allows you to associate arrays of measured data (e.g., AC energy, AC power, irradiance, air temperature).

* PerformanceRatios - an array of PerformanceRatio. For each entry in the array, you can record a performance ratio calculation, which includes:
* * PerfRatio - the value of the performance ratio, which is measured AC energy divided by modeled AC energy.
* * EnergyAC - the measured AC energy.
* * EnergyACModeled - the modeled AC energy.
* * EnergyModelID - an identifier to associate the PerformanceRatio with details of the energy model (see ExpectedEnergyModel).

* ExpectedEnergyModel - records of an energy model applied to measured weather during the period of the operating report.
