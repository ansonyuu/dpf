import pandas as pd

# Assuming you have an Excel file named 'data.xlsx' and you're working with 'Sheet1'
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Equivalent to Range("A20:DA30000").Select and Selection.ClearContents in VBA
df.loc[19:29999, 'A':'DA'] = ''

# Comments in Python start with #
# 16 Feb 2022 RADPFV5.16FIB standardised Fast Ion Beam version, rationalised with all radiation data outputted as (plasma self-absorption) AB corrected
# ... (other comments omitted for brevity)

# Variables in Python
backhowmanyrows = 0
ENDFLAG, DFLAG, DVFLAG, NTN, NBN, NN, VRMAX, peakvs, peakvp, tc5 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 1

import math
import pandas as pd

# Quick Device Choice
device = df.iat[3, 14]
if device == 0:
    pass
elif device == 1:
    df.iat[2, 1] = "UNUICTPPFF"
    L0 = 110
    C0 = 30
    RADB = 3.2
    RADA = 0.95
    Z0 = 16
    R0 = 12
    V0 = 15
    P0 = 3.5
    MW = 4
    ZN = 1
    dissociatenumber = 2
    massf = 0.08
    CURRF = 0.7
    massfr = 0.16
    currfr = 0.7
    df.iat[4, 0] = L0
    df.iat[4, 1] = C0
    df.iat[4, 2] = RADB
    df.iat[4, 3] = RADA
    df.iat[4, 4] = Z0
    df.iat[4, 5] = R0
    df.iat[6, 0] = massf
    df.iat[6, 1] = CURRF
    df.iat[6, 2] = massfr
    df.iat[6, 3] = currfr
    df.iat[8, 0] = V0
    df.iat[8, 1] = P0
    df.iat[8, 2] = MW
    df.iat[8, 3] = ZN
    df.iat[8, 4] = dissociatenumber
elif device == 2:
    # Similar assignments as in device == 1
    pass
elif device == 3:
    # Similar assignments as in device == 1
    pass

# Input, from EXCEL Sheet, Machine Parameters, in convenient units; fen=ratio beam KE/pinch inductive energy (for FIB calc)
L0 = df.iat[4, 0]
C0 = df.iat[4, 1]
RADB = df.iat[4, 2]
RADA = df.iat[4, 3]
Z0 = df.iat[4, 4]
R0 = df.iat[4, 5]

# Is anode tapered?
TAPER = df.iat[6, 7]

# Input, from EXCEL Sheet, Machine Operational parameters, in convenient units
V0 = df.iat[8, 0]
P0 = df.iat[8, 1]
MW = df.iat[8, 2]
ZN = df.iat[8, 3]
dissociatenumber = df.iat[8, 4]
fen = df.iat[12, 12]
radratiolimit = df.iat[12, 9]
rctimelimit = df.iat[12, 10]

# Input, from EXCEL Sheet, Model Parameters
massf = df.iat[6, 0]
CURRF = df.iat[6, 1]
massfr = df.iat[6, 2]
currfr = df.iat[6, 3]
R0 = R0 / 1000

# Input some constants in SI units
Mu = 1.257 * 10 ** -6
Pi = 3.142
bc = 1.38 * 10 ** -23
mi = 1.67 * 10 ** -27
MUK = Mu / (8 * Pi * Pi * bc)
CON11 = 1.6 * 10 ** -20
CON12 = 9.999999 * 10 ** -21
CON2 = 4.6 * 10 ** -31
UGCONS = 8.310001 * 10 ** 3
FRF = 0.3
fe = 1 / 3
FLAG = 0

# reset EINP, energy dissipated by dynamic resistance effect, which is 0.5 (Ldot) I^2, considering current taking part in the motion
EINP = 0

# If operating in Deuterium, set value of G
if ZN == 1 or ZN == 2:
    g = 1.66667
else:
    # If Ne or argon or Xenon, Kr or N2, set approx initial values of G
    g = 1.3

G1 = 2 / (g + 1)
G2 = (g - 1) / g
GCAP = (g + 1) / (g - 1)

# Calculate ambient number density and some ratios
N0 = 2.69 * (10 ** 25) * P0 / 760
C = RADB / RADA
f = Z0 / RADA

# Convert to SI units
C0 = C0 * 10 ** -6
L0 = L0 * 10 ** -9
RADB = RADB * 0.01
RADA = RADA * 0.01
Z0 = Z0 * 10 ** -2
V0 = V0 * 1000
RHO = P0 * 2.33 * (10 ** -4) * MW / 4
TM = 0

#part about tapering

import pandas as pd
import numpy as np

# Assuming we have an Excel file named 'data.xlsx' and we're working with 'Sheet1'
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Example of setting values in DataFrame
df.at[10, 0] = RHO
df.at[10, 1] = I0
df.at[10, 2] = T0
df.at[10, 3] = TA

# Example of getting values from DataFrame
L0 = df.at[4, 0]
C0 = df.at[4, 1]
RADB = df.at[4, 2]
RADA = df.at[4, 3]
Z0 = df.at[4, 4]
R0 = df.at[4, 5]

# If conditions
if P0 > 20:
    print("WARNING! In real experiments, Pressure above 20 torr will not produce focussing")
    print("ACTION RECOMMENDED: REDUCE FILL PRESSURE below 20 torr")

# And so on...

# Save changes to the same Excel file
df.to_excel('data.xlsx', sheet_name='Sheet1', index=False)