
LV BMS — SOC Estimator
Author: Ebram Aziz

This project combines:

- Original LTC2943 firmware
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
