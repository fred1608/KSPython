import KSPython as ksp
from KSPython.RocketFuelTankParts import FLT400, FLT800
from KSPython.LiquidEngineParts import LVT45, LVT30

rocket = ksp.Rocket('Basic Rocket Example')
main_stage = ksp.Stage()
lift_stages = ksp.Stage()

main_stage.add_parts([FLT800, LVT45])
main_stage.add_extra_mass(0.84) # Mk1 Command Pod

lift_stages.add_parts([FLT400]*2 + [LVT30]*2)
lift_stages.add_extra_mass(0.05*2) # FTX-2 Fuel Duct
lift_stages.add_extra_mass(0.05*2) # TT-70 Decoupler

rocket.add_stages([lift_stages]*3 + [main_stage])
rocket.schedule_engine(0,1)
rocket.schedule_engine(0,2)
rocket.schedule_engine(0,3)

rocket.generate_report()