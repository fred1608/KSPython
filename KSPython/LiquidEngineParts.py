"""

This submodule is responsible to house liquid rocket engines to be used on simulation.

Note: 

* Id Name is the name assigned to the part to be imported and inserted into the code.
* LVN 'Nerv' Engine is not-supported, as the calculation currently does not differentiate between oxidizer and liquid fuel.
* KR12 is divided into two parts, one for engine and one for fuel, both parts must be added if using it.

+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| Id Name    | Name                                | Mass [ton] | Cost      | Thrust atm | Thrust vac | ISP atm | ISP vac |
+============+=====================================+============+===========+============+============+=========+=========+
| LV1R       | LV-1R "Spider" Liquid Fuel Engine   | 0.02       | 120       | 1.79       | 2          | 260     | 290     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| E2477      | 24-77 "Twitch" Liquid Fuel Engine   | 0.02       | 230       | 15.17      | 16         | 275     | 290     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| Mk55       | Mk-55 "Thud" Liquid Fuel Engine     | 0.9        | 820       | 108.2      | 120        | 275     | 305     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| LV1        | LV-1 "Ant" Liquid Fuel Engine       | 0.02       | 110       | 0.51       | 2          | 80      | 315     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| E487S      | 48-7S "Spark" Liquid Fuel Engine    | 0.13       | 240       | 16.56      | 20         | 265     | 320     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| LV909      | LV-909 "Terrier" Liquid Fuel Engine | 0.5        | 390       | 14.78      | 60         | 85      | 345     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| LVT30      | LV-T30 "Reliant" Liquid Fuel Engine | 1.25       | 1100      | 205.16     | 240        | 265     | 310     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| LVT45      | LV-T45 "Swivel" Liquid Fuel Engine  | 1.5        | 1200      | 167.97     | 215        | 250     | 320     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| S3KS25     | S3 KS-25 "Vector" Liquid Fuel Engine| 4          | 18000     | 936.51     | 1000       | 295     | 315     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| T1         | T-1 Toroidal Aerospike "Dart"       | 1          | 3850      | 153.53     | 180        | 290     | 340     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| REL10      | RE-L10 "Poodle" Liquid Fuel Engine  | 1.75       | 1300      | 64.29      | 250        | 90      | 350     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| REI5       | RE-I5 "Skipper" Liquid Fuel Engine  | 3          | 5300      | 568.75     | 650        | 280     | 320     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| REM3       | RE-M3 "Mainsail" Liquid Fuel Engine | 6          | 13000     | 1379.03    | 1500       | 285     | 310     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| KR12_e     | LFB KR-1x2 "Twin-Boar" Liquid Engine| 0          | 0         | 1866.67    | 2000       | 280     | 300     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| KR2L       | Kerbodyne KR-2L+ "Rhino"            | 9          | 25000     | 1205.88    | 2000       | 205     | 340     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| S3KS254    | S3 KS-25x4 "Mammoth" Liquid Engine  | 15         | 39000     | 3746.03    | 4000       | 295     | 315     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+
| CR7        | CR-7 R.A.P.I.E.R. Engine            | 2          | 6000      | 162.3      | 180        | 275     | 305     |
+------------+-------------------------------------+------------+-----------+------------+------------+---------+---------+


"""

from KSPython import LiquidEngine

LV1R = LiquidEngine('LV-1R "Spider" Liquid Fuel Engine', 0.02, 120, 1.79, 2, 260, 290)
E2477 = LiquidEngine('24-77 "Twitch" Liquid Fuel Engine', 0.08, 230, 15.17, 16, 275, 290)
Mk55 = LiquidEngine('Mk-55 "Thud" Liquid Fuel Engine', 0.9, 820, 108.2, 120, 275, 305)
# O10 mono engine would be here, not yet supported

LV1 = LiquidEngine('LV-1 "Ant" Liquid Fuel Engine', 0.02, 110, 0.51, 2, 80, 315)
E487S = LiquidEngine('48-7S "Spark" Liquid Fuel Engine', 0.13, 240, 16.56, 20, 265, 320)

LV909 = LiquidEngine('LV-909 "Terrier" Liquid Fuel Engine', 0.5, 390, 14.78, 60, 85, 345)
LVT30 = LiquidEngine('LV-T30 "Reliant" Liquid Fuel Engine', 1.25, 1100, 205.16, 240, 265, 310)
LVT45 = LiquidEngine('LV-T45 "Swivel" Liquid Fuel Engine', 1.5, 1200, 167.97, 215, 250, 320)

S3KS25 = LiquidEngine('S3 KS-25 "Vector" Liquid Fuel Engine', 4, 18000, 936.51, 1000, 295, 315)
T1 = LiquidEngine('T-1 Toroidal Aerospike "Dart" Liquid Fuel Engine', 1, 3850, 153.53, 180, 290, 340)
LVN = LiquidEngine('LV-N "Nerv" Atomic Rocket Motor', 3, 10000, 13.88, 60, 185, 800) # NOTE: Nerv only uses liquid fuel, there is currently no distinction between fuel types in the library, so caution is advised when using this engine

REL10 = LiquidEngine('RE-L10 "Poodle" Liquid Fuel Engine', 1.75, 1300, 64.29, 250, 90, 350)
REI5 = LiquidEngine('RE-I5 "Skipper" Liquid Fuel Engine', 3, 5300, 568.75, 650, 280, 320)
REM3 = LiquidEngine('RE-M3 "Mainsail" Liquid Fuel Engine', 6, 13000, 1379.03, 1500, 285, 310)
KR12_e = LiquidEngine('LFB KR-1x2 "Twin-Boar" Liquid Fuel Engine', 0, 0, 1866.67, 2000, 280, 300)# NOTE: To use this, you need to add both the engine part as well as the fuel tank part to stage.

KR2L = LiquidEngine('Kerbodyne KR-2L+ "Rhino" Liquid Fuel Engine', 9, 25000, 1205.88, 2000, 205, 340)
S3KS254 = LiquidEngine('S3 KS-25x4 "Mammoth" Liquid Fuel Engine', 15, 39000, 3746.03, 4000, 295, 315)

CR7 = LiquidEngine('CR-7 R.A.P.I.E.R. Engine', 2, 6000, 162.3, 180, 275, 305) # NOTE: Currently there's no simulation of jet engines, this will only simulate Rocket behavior