import KSPython as ksp
from KSPython.RocketFuelTankParts import X20016, Jumbo64
from KSPython.LiquidEngineParts import REL10, REM3
import matplotlib.pyplot as plt

rocket = ksp.Rocket('Heavy lifter')

final_stage = ksp.Stage()
main_stage = ksp.Stage()
asp_stages = ksp.Stage()


final_stage.add_parts([X20016,REL10])
main_stage.add_parts([Jumbo64,Jumbo64,REM3])
asp_stages.add_parts([Jumbo64,REM3]*2)

rocket.add_stages([asp_stages, asp_stages, asp_stages, main_stage, final_stage])

rocket.schedule_engine(0,1)
rocket.schedule_engine(0,2)
rocket.schedule_engine(0,3)

dVs = []
payloads = range(250)
for mass in payloads:
    rocket.change_payload(mass)
    dVs.append(rocket.adjusted_dV())

plt.plot(payloads, dVs)
plt.xlabel('Payload [ton]')
plt.ylabel('Delta-V [m/s]')
plt.grid()
plt.show()

rocket.change_payload(50)
rocket.generate_report()