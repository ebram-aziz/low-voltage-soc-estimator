
# Munich Motorsport LV BMS — Final SOC Estimator
# Author: Ebram Aziz
This project combines:

- Original Munich Motorsport LTC2943 firmware
- Modular SOC estimator framework
- Coulomb counting
- OCV lookup
- Extended Kalman Filter (EKF)

## Architecture

```text
LTC2943 Hardware
        ↓
Current / Voltage / Temperature
        ↓
SOC Estimator Layer
 ├── Coulomb Counting
 ├── OCV Lookup
 └── EKF Correction
        ↓
Filtered SOC %
```

## Improvements Added

- Unified current sign convention:
  - Positive current = DISCHARGE
  - Negative current = CHARGE

- Corrected Coulomb counting tests
- Improved EKF stability
- Added realistic simulator
- Added replay-based testing
- Added battery characterization hooks

## Excel Sheet Usage

The original Excel measurement sheets are intended for:

- Battery current validation
- Drive-cycle profile extraction
- Temperature correlation
- OCV curve fitting

The simulator was adjusted to:
- mimic realistic LV battery currents,
- use LTC2943 current polarity,
- generate voltage noise similar to hardware ADC behavior.

If the Excel sheets become available in the repository,
they should replace the synthetic drive cycle inside:

```text
scripts/simulate_cell.py
```

## Build

```bash
make all
make test
```

## Run Simulator

```bash
python3 scripts/simulate_cell.py
```

## References

- https://github.com/kamalkadakara/bms-soc-estimation
- LTC2943 Demo Manual
- TI State of Charge Estimation Application Note
- Munich Motorsport LV BMS firmware
