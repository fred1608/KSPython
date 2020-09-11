# This script will compare three different ways of setting up a rocket with the same parts to compare

import KSPython as ksp
from KSPython.RocketFuelTankParts import X20032, FLT800
from KSPython.LiquidEngineParts import REI5, LVT30
from KSPython.BoosterParts import RT10

rocket1 = ksp.Rocket('Asparagus')
rocket2 = ksp.Rocket('Direct')
rocket3 = ksp.Rocket('Direct with no fuel connection')
rocket4 = ksp.Rocket('Direct w 4xRT10')
rocket5 = ksp.Rocket('Direct with no fuel connection w 4xRT10')
payload = 2 # Ton


main_stage = ksp.Stage()
asparagus_stage = ksp.Stage()
direct_stage = ksp.Stage()
booster_stage = ksp.Stage()

main_stage.add_parts([X20032, REI5])
asparagus_stage.add_parts([FLT800]*2 + [LVT30]*2)
direct_stage.add_parts([FLT800]*4 + [LVT30]*4)
booster_stage.add_parts([RT10]*4)


rocket1.add_stages([asparagus_stage]*2+[main_stage])
rocket1.schedule_engine(0,1)
rocket1.schedule_engine(0,2)
rocket1.change_payload(payload)
rocket1.generate_report()

rocket2.add_stages([direct_stage]+[main_stage])
rocket2.schedule_engine(0,1)
rocket2.change_payload(payload)
rocket2.generate_report()

rocket3.add_stages([direct_stage]+[main_stage])
rocket3.schedule_engine(0,1)
rocket3.change_payload(payload)
rocket3.rem_fuel_flow(0)
rocket3.generate_report()

# print(rocket3.time_between_stages(0,1))
# print(rocket3.prestage_mass_loss(1))

rocket4.add_stages([booster_stage]+[direct_stage]+[main_stage])
rocket4.schedule_engine(0,1)
rocket4.schedule_engine(0,2)
rocket4.change_payload(payload)
rocket4.generate_report()

# print(rocket4.async_engines)
# print(rocket4.restric_fuel_flow)

rocket5.add_stages([booster_stage]+[direct_stage]+[main_stage])
rocket5.schedule_engine(0,1)
rocket5.schedule_engine(0,2)
rocket5.change_payload(payload)
rocket5.rem_fuel_flow(1)
rocket5.generate_report()

# print(rocket5.async_engines)
# print(rocket5.restric_fuel_flow)
# print(rocket5.time_between_stages(0,2))
# print(rocket5.prestage_mass_loss(2))
