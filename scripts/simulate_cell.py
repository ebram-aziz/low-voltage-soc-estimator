
import csv
import math
import random

CAPACITY_AH = 60.0

# Positive current = discharge
# Negative current = charge

R0 = 0.005
R1 = 0.008
C1 = 1500.0

OCV_TABLE = [
3000,3010,3020,3040,3060,3080,3100,3120,3140,3160,
3180,3200,3220,3240,3260,3280,3300,3320,3340,3360,
3380,3400,3420,3440,3460,3480,3500,3510,3520,3530,
3540,3550,3560,3570,3580,3590,3600,3610,3620,3630,
3640,3650,3660,3670,3680,3690,3700,3710,3715,3720,
3725,3730,3735,3740,3745,3750,3755,3760,3765,3770,
3775,3780,3790,3800,3810,3820,3830,3840,3850,3860,
3870,3880,3890,3900,3910,3920,3940,3960,3980,4000,
4020,4040,4060,4080,4090,4100,4110,4120,4130,4140,
4150,4155,4160,4165,4170,4175,4180,4185,4190,4195,
4200
]

def ocv_from_soc(soc):
    soc = max(0.0, min(100.0, soc))
    idx = int(soc)

    if idx >= 100:
        return OCV_TABLE[100]

    frac = soc - idx
    return OCV_TABLE[idx] + frac * (OCV_TABLE[idx+1] - OCV_TABLE[idx])

def generate_profile(duration_s=1800, dt=0.1):
    profile = []
    t = 0.0
    current = 5.0

    while t < duration_s:
        target = random.choice([
            random.uniform(5, 20),
            random.uniform(20, 60),
            random.uniform(-15, -3),
            0.0
        ])

        slew = 10.0 * dt

        if target > current:
            current += slew
        else:
            current -= slew

        profile.append((round(t,2), current))
        t += dt

    return profile

def simulate():
    soc = 90.0
    v_rc = 0.0

    dt = 0.1
    tau = R1 * C1
    alpha = math.exp(-dt/tau)

    records = []

    for t, current in generate_profile():

        delta_soc = (current * dt) / (3600 * CAPACITY_AH) * 100.0
        soc -= delta_soc

        soc = max(0.0, min(100.0, soc))

        v_rc = alpha * v_rc + R1 * (1.0 - alpha) * current

        ocv = ocv_from_soc(soc)

        voltage = ocv - current * R0 * 1000 + v_rc * 1000

        voltage += random.gauss(0, 4)

        records.append([
            round(t,2),
            round(current,3),
            round(voltage,2),
            round(soc,3)
        ])

    return records

records = simulate()

with open("test_vectors.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "time_s",
        "current_a",
        "voltage_mv",
        "true_soc_pct"
    ])

    writer.writerows(records)

print(f"Generated {len(records)} samples")
