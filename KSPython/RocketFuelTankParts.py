"""

This submodule is responsible to house liquid rocket fuel tanks to be used on simulation.

Note: 

* Id Name is the name assigned to the part to be imported and inserted into the code.
* KR12 is divided into two parts, one for engine and one for fuel, both parts must be added if using it.

+------------+-------------------------------------+-----------------+------------------+-----------+
| Id Name    | Name                                | Mass Full [ton] | Mass Empty [ton] | Cost      |
+============+=====================================+=================+==================+===========+
| R4         | R-4 'Dumpling' External Tank        | 0.1238          | 0.0138           | 50        |
+------------+-------------------------------------+-----------------+------------------+-----------+
| R11        | R-11 'Baguette' External Tank       | 0.3038          | 0.03338          | 50        |
+------------+-------------------------------------+-----------------+------------------+-----------+
| R12        | R-12 'Doughnut' External Tank       | 0.3375          | 0.0375           | 147       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| OscarB     | Oscar-B Fuel Tank                   | 0.225           | 0.025            | 70        |
+------------+-------------------------------------+-----------------+------------------+-----------+
| FLT100     | FL-T100 Fuel Tank                   | 0.5625          | 0.0625           | 150       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| FLT200     | FL-T200 Fuel Tank                   | 1.125           | 0.125            | 275       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| FLT400     | FL-T400 Fuel Tank                   | 2.25            | 0.25             | 500       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| FLT800     | FL-T800 Fuel Tank                   | 4.5             | 0.5              | 800       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| X2008      | Rockomax X200-8 Fuel Tank           | 4.5             | 0.5              | 800       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| X20016     | Rockomax X200-16 Fuel Tank          | 9               | 1                | 1550      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| X20032     | Rockomax X200-32 Fuel Tank          | 18              | 2                | 3000      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Jumbo64    | Rockomax Jumbo-64 Fuel Tank         | 36              | 4                | 5750      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| S33600     | Kerbodyne S3-3600 Tank              | 20.25           | 2.25             | 3250      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| S37200     | Kerbodyne S3-7200 Tank              | 40.5            | 4.5              | 6500      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| S314400    | Kerbodyne S3-14400 Tank             | 81              | 9                | 13000     |
+------------+-------------------------------------+-----------------+------------------+-----------+
| KR12_ft    | LFB KR-1x2 "Twin-Boar" Liquid Engine| 42.5            | 10.5             | 17000     |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk2RS      | Mk2 Rocket Fuel Fuselage Short      | 2.29            | 0.29             | 750       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk2R       | Mk2 Rocket Fuel Fuselage            | 4.57            | 0.57             | 1450      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk3RS      | Mk3 Rocket Fuel Fuselage Short      | 14.29           | 1.79             | 2500      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk3R       | Mk3 Rocket Fuel Fuselage            | 28.57           | 3.57             | 5000      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk3RL      | Mk3 Rocket Fuel Fuselage Long       | 57.14           | 7.14             | 10000     |
+------------+-------------------------------------+-----------------+------------------+-----------+
| C7BA       | C7 Brand Adapter - 2.5m to 1.25m    | 4.57            | 0.57             | 800       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| C7BAS      | C7 Adapter Slanted - 2.5m to 1.25m  | 4.57            | 0.57             | 800       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk2125     | Mk2 to 1.25m Adapter Long           | 4.57            | 0.57             | 1050      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk2125L    | Mk2 Bicoupler                       | 2.29            | 0.29             | 860       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk2Bi      | Kerbodyne S3-14400 Tank             | 81              | 9                | 13000     |
+------------+-------------------------------------+-----------------+------------------+-----------+
| A25Mk2     | 2.5m to Mk2 Adapter                 | 4.57            | 0.57             | 800       |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk3Mk2     | Mk3 to Mk2 Adapter                  | 11.43           | 1.43             | 2200      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk325      | Mk3 to 2.5m Adapter                 | 14.29           | 1.79             | 2500      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk325S     | Mk3 to 2.5m Adapter Slanted         | 14.29           | 1.79             | 2500      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| Mk3375     | Mk3 to 3.75m Adapter                | 14.29           | 1.79             | 2500      |
+------------+-------------------------------------+-----------------+------------------+-----------+
| ADTP23     | Kerbodyne ADTP-2-3                  | 16.88           | 1.88             | 1623      |
+------------+-------------------------------------+-----------------+------------------+-----------+

"""

from KSPython import RocketFuelTank

R4 = RocketFuelTank("R-4 'Dumpling' External Tank", 0.1238, 0.0138, 50)
R11 = RocketFuelTank("R-11 'Baguette' External Tank", 0.3038, 0.03338, 50)
R12 = RocketFuelTank("R-12 'Doughnut' External Tank", 0.3375, 0.0375, 147)
OscarB = RocketFuelTank("Oscar-B Fuel Tank", 0.225, 0.025, 70)

FLT100 = RocketFuelTank("FL-T100 Fuel Tank", 0.5625, 0.0625, 150)
FLT200 = RocketFuelTank("FL-T200 Fuel Tank", 1.125, 0.125, 275)
FLT400 = RocketFuelTank("FL-T400 Fuel Tank", 2.25, 0.25, 500)
FLT800 = RocketFuelTank("FL-T800 Fuel Tank", 4.5, 0.5, 800)

X2008 = RocketFuelTank("Rockomax X200-8 Fuel Tank", 4.5, 0.5, 800)
X20016 = RocketFuelTank("Rockomax X200-16 Fuel Tank", 9, 1, 1550)
X20032 = RocketFuelTank("Rockomax X200-32 Fuel Tank", 18, 2, 3000)
Jumbo64 = RocketFuelTank("Rockomax Jumbo-64 Fuel Tank", 36, 4, 5750)

S33600 = RocketFuelTank("Kerbodyne S3-3600 Tank", 20.25, 2.25, 3250)
S37200 = RocketFuelTank("Kerbodyne S3-7200 Tank", 40.5, 4.5, 6500)
S314400 = RocketFuelTank("Kerbodyne S3-14400 Tank", 81, 9, 13000)
KR12_ft = RocketFuelTank('LFB KR-1x2 "Twin-Boar" Liquid Fuel Engine', 42.5, 10.5, 17000) # NOTE: To use this, you need to add both the engine part as well as the fuel tank part to stage.

Mk2RS = RocketFuelTank("Mk2 Rocket Fuel Fuselage Short", 2.29, 0.29, 750)
Mk2R = RocketFuelTank("Mk2 Rocket Fuel Fuselage", 4.57, 0.57, 1450)

Mk3RS = RocketFuelTank("Mk3 Rocket Fuel Fuselage Short", 14.29, 1.79, 2500)
Mk3R = RocketFuelTank("Mk3 Rocket Fuel Fuselage", 28.57, 3.57, 5000)
Mk3RL = RocketFuelTank("Mk3 Rocket Fuel Fuselage Long", 57.14, 7.14, 10000)

C7BA = RocketFuelTank("C7 Brand Adapter - 2.5m to 1.25m", 4.57, 0.57, 800)
C7BAS = RocketFuelTank("C7 Brand Adapter Slanted - 2.5m to 1.25m", 4.57, 0.57, 800)
Mk2125 = RocketFuelTank("Mk2 to 1.25m Adapter", 2.29, 0.29, 550)
Mk2125L = RocketFuelTank("Mk2 to 1.25m Adapter Long", 4.57, 0.57, 1050)
Mk2Bi = RocketFuelTank("Mk2 Bicoupler", 2.29, 0.29, 860)
A25Mk2 = RocketFuelTank("2.5m to Mk2 Adapter", 4.57, 0.57, 800)
Mk3Mk2 = RocketFuelTank("Mk3 to Mk2 Adapter", 11.43, 1.43, 2200)
Mk325 = RocketFuelTank("Mk3 to 2.5m Adapter", 14.29, 1.79, 2500)
Mk325S = RocketFuelTank("Mk3 to 2.5m Adapter Slanted", 14.29, 1.79, 2500)
Mk3375 = RocketFuelTank("Mk3 to 3.75m Adapter", 14.29, 1.79, 2500)
ADTP23 = RocketFuelTank("Kerbodyne ADTP-2-3", 16.88, 1.88, 1623)