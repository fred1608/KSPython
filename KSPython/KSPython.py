# NOTES:


from math import log
from collections import defaultdict

# __all__ = ['Part', 'BasicTank', 'RocketFuelTank', 'Engine', 'LiquidEngine', 'SolidEngine', 'Stage', 'Rocket']

class KerbalException(Exception):
    def __init__(self, message):
        super().__init__('Whops, accidental lithobrake: ' + message)

def _number_check(num):
    try:
        num = float(num)
    except ValueError:
        raise KerbalException(f'Variable: {num} is not a number!')
    else:
        return num

def _loc_check(loc):
    if loc != 'atm' and loc != 'vac':
        raise KerbalException(f"loc can only be 'atm' or 'vac', and not {loc}.")

class Part:
    def __init__(self, name, mass, cost):
        self.name = name
        self.mass = _number_check(mass)
        self.cost = _number_check(cost)

# Should only be used with rocket fuel tanks. Airplanes and space planes are not yet supported.
class BasicTank(Part):
    def __init__(self, name, mass_full, mass_empty, cost): 
        super().__init__(name, mass_full, cost)
        self.mass_empty = _number_check(mass_empty)

class RocketFuelTank(BasicTank):
    def __init__(self, name, mass_full, mass_empty, cost):
        super().__init__(name, mass_full, mass_empty, cost)

# Xenon will be implemented at a latter time
class XenonTank(BasicTank):
    def __init__(self, name, mass_full, mass_empty, cost):
        super().__init__(name, mass_full, mass_empty, cost)
        raise KerbalException('Not yet implemented')

class Engine(Part):
    def __init__(self, name, mass, cost, thrust_atm, thrust_vac, isp_atm, isp_vac):
        super().__init__(name, mass, cost)
        self.thrust_atm = _number_check(thrust_atm)
        self.thrust_vac = _number_check(thrust_vac)
        self.isp_atm = _number_check(isp_atm)
        self.isp_vac = _number_check(isp_vac)

class LiquidEngine(Engine):
    def __init__(self, name, mass, cost, thrust_atm, thrust_vac, isp_atm, isp_vac): 
        super().__init__(name, mass, cost, thrust_atm, thrust_vac, isp_atm, isp_vac)

class SolidEngine(Engine):
    def __init__(self, name, mass_full, mass_empty, cost, thrust_atm, thrust_vac, isp_atm, isp_vac): 
        super().__init__(name, mass_full, cost, thrust_atm, thrust_vac, isp_atm, isp_vac)
        self.mass_empty = _number_check(mass_empty)

class Stage:
    def __init__(self):
        self.parts = []
        self.extra_mass = 0.0
        self.extra_cost = 0.0

    def add_part(self, part):
        if not isinstance(part, Part): # compare the Class part and the part being inserted
            raise KerbalException('Only parts can be added to a stage.')
        else:
            self.parts.append(part)
        self.check_for_parts_not_allowed_together()

    def add_parts(self, parts): # Input is a list of parts
        for part in parts:
            self.add_part(part)

    def list_parts(self):
        for part in self.parts:
            print(part.name)

    def remove_part(self):
        pass

    def add_extra_mass(self, mass):
        self.extra_mass += _number_check(mass)

    def add_extra_cost(self, cost):
        self.extra_cost += _number_check(cost)

    def calculate_full_mass(self):
        mass_sum = self.extra_mass
        for part in self.parts:
            mass_sum += part.mass
        return mass_sum

    def calculate_cost(self):
        cost_sum = self.extra_cost
        for part in self.parts:
            cost_sum += part.cost
        return cost_sum

    def calculate_empty_mass(self):
        mass_sum = self.extra_mass
        for part in self.parts:
            if hasattr(part, 'mass_empty'):
                mass_sum += part.mass_empty
            else:
                mass_sum += part.mass
        return mass_sum

    def get_engine_performance(self, loc='atm'): # all engines from stage
        _loc_check(loc)
        relative_isp_list = []
        thrust_list = []
        for part in self.parts:
            if isinstance(part, Engine): 
                if loc is 'atm':
                    thrust_list.append(part.thrust_atm)
                    relative_isp_list.append(part.thrust_atm/part.isp_atm)
                elif loc is 'vac':
                    thrust_list.append(part.thrust_vac)
                    relative_isp_list.append(part.thrust_vac/part.isp_vac)
        thrust = sum(thrust_list)
        isp = thrust / sum(relative_isp_list)
        return thrust, isp

    def check_for_parts_not_allowed_together(self):
        fuels = {'liquid': False, 'solid': False}
        engines = {'liquid': False, 'solid': False}
        for part in self.parts:
            if isinstance(part, SolidEngine):
                fuels['solid'] = True
                engines['solid'] = True
            if isinstance(part, RocketFuelTank):
                fuels['liquid'] = True
            if isinstance(part, LiquidEngine):
                engines['liquid']
        if fuels['liquid'] and fuels['solid']:
            raise KerbalException('Cannot have liquid and solid fuels in the same stage.')
        if engines['liquid'] and engines['solid']:
            raise KerbalException('Cannot have liquid and solid engines in the same stage.')

    def get_fuel_type(self):
        for part in self.parts:
            if isinstance(part, SolidEngine):
                return 'solid'
            if isinstance(part, RocketFuelTank):
                return 'liquid'


class Rocket:
    def __init__(self,name = None):
        self.stages = []
        self.name = name
        self.payload = 0 # simulated rocket payload in Tons
        self.async_engines = defaultdict(list) # this dictionary links engines that fire before their stage {stage_fire:[stages_present]} 
        self.restric_fuel_flow = [] # this list contains all stages that have restricted fuel flow in between the stage number intered and the next stage

    # Stages must be added in order, from first (ascension) to last 
    def add_stage(self, stage):
        if not isinstance(stage, Stage): # compare the Class part and the part being inserted
            raise KerbalException('Only stages can be added to a rocket.')
        else:
            self.stages.append(stage)
            # If I implement Xenon, this part will have to be changed.
            if stage.get_fuel_type() is 'solid': # if it is a solid rocket engine, it removes fuel flow with both stage after and before
                num_stages = self.num_stages()
                self.rem_fuel_flow(num_stages-1)
                if num_stages > 1:
                    self.rem_fuel_flow(num_stages-2)

    def add_stages(self, stages):
        for stage in stages:
            self.add_stage(stage)

    def num_stages(self):
        return len(self.stages)

    def change_payload(self, payload):
        self.payload = _number_check(payload)

    # This gets engine peformance from all engines that are firing in more complex stagings
    # stage_max limits this function to be performed only to stages smaller or equal than it
    def performance_engines_firing(self, stage_num, stage_max = None, loc = 'atm'):
        _loc_check(loc)
        current_thrust, current_isp = self.stages[stage_num].get_engine_performance(loc = loc)
        thrust_list = [current_thrust]
        isp_list = [current_isp]
        for i in range(stage_num+1):
            stages_present = self.async_engines.get(i)
            if stages_present != None:
                for stage_present in stages_present:
                    if stage_max is None:
                        if stage_present > stage_num:
                            thrust, isp = self.stages[stage_present].get_engine_performance(loc = loc)
                            thrust_list.append(thrust)
                            isp_list.append(isp)
                    else:
                        if stage_present > stage_num and stage_present <=stage_max:
                            thrust, isp = self.stages[stage_present].get_engine_performance(loc = loc)
                            thrust_list.append(thrust)
                            isp_list.append(isp)
        return thrust_list, isp_list

    def engine_burn_time(self, stage_num, loc = 'atm'): # note: burn time is from stage start to stage end. If engine was started before stage start, it will be discarded.
        _loc_check(loc)
        thrust, isp = self.calculate_group_performance(stage_num, loc=loc)
        mass_flow = thrust / (isp*9.81)
        mass_full = self.stages[stage_num].calculate_full_mass() - self.prestage_mass_loss(stage_num, loc = loc)
        mass_empty = self.stages[stage_num].calculate_empty_mass() 
        if mass_full<mass_empty:
            raise KerbalException(f'Stage: {stage_num} lost all its fuel before being staged! This is not supported.')
        burn_time = (mass_full - mass_empty) / mass_flow 
        return burn_time # seconds

    def time_between_stages(self, stage_ini, stage_end, loc = 'atm'): # time until start of stage_end, does not include it
        _loc_check(loc)
        if stage_ini  == stage_end:
            return 0.0
        elif stage_ini>stage_end:
            raise KerbalException('Stage_ini must be smaller than, or equal to stage_end.')
        else:
            iter_stage = range(stage_ini, stage_end) 
        total_time = 0.0
        for stage_num in iter_stage:
            total_time += self.engine_burn_time(stage_num, loc=loc)
        return total_time

    # isp of all engines firing at a given moment to general delta V calculation
    def calculate_isp(self, stage_num, loc = 'atm'):
        _loc_check(loc)
        thrust_list, isp_list = self.performance_engines_firing(stage_num, loc = loc)
        total_thrust = sum(thrust_list)
        relative_thurst = sum([thrust_list[i]/isp_list[i] for i in range(len(isp_list))])
        isp = total_thrust / relative_thurst
        return isp

    # the thurst and isp of a group of rockets that are firing together and share common fuel
    def calculate_group_performance(self, stage_num, loc='atm'):
        _loc_check(loc)
        stage_max = None
        for val in self.restric_fuel_flow:
            if val >= stage_num: # finds stage with fuel restriction closer to stage_num
                stage_max = val
                break
        thrust_list, isp_list = self.performance_engines_firing(stage_num, stage_max = stage_max, loc = loc)
        total_thrust = sum(thrust_list)
        relative_thurst = sum([thrust_list[i]/isp_list[i] for i in range(len(isp_list))])
        isp = total_thrust / relative_thurst
        return total_thrust, isp

    # Engines normally fire at their stage. This allows them to be fired before.
    def schedule_engine(self,stage_fire, stage_present):
        try:
            stage_fire = int(stage_fire)
            stage_present = int(stage_present)
        except ValueError:
            raise KerbalException("Values for stages can only be integers.")

        if stage_fire >= stage_present:
            raise KerbalException("Engines can only be scheduled to fire before their stage.")
        current_keys = list(self.async_engines)
        for key in current_keys:
            if stage_present in self.async_engines[key]:
                raise KerbalException(f"A stage can only be scheduled to fire once.")
        self.async_engines[stage_fire].append(stage_present)

    # In normal operation, fuel will always be passed from smaller stages to the next (automatic fuel flow). 
    # This allows to restric it. In some cases, where there are more then on type of fuel
    # (like solid engines firing together with liquid), this will be performed automatically.
    def rem_fuel_flow(self, stage_num): 
        stage_num = int(stage_num)
        if not stage_num in self.restric_fuel_flow:
            self.restric_fuel_flow.append(stage_num)
            self.restric_fuel_flow.sort() # list must always be sorted to avoid issues with calculate_group_isp algorithm

    def find_when_engine_fired(self,stage_num):
        stage_fire = stage_num # default is to fire at own stage
        for key in list(self.async_engines):
            if stage_num in self.async_engines[key]:
                stage_fire = key
                return stage_fire
        return stage_fire

    def check_mass_lost(self, stage_num, mass_loss):
        fuel_mass = self.stages[stage_num].calculate_full_mass() - self.stages[stage_num].calculate_empty_mass()
        if mass_loss > fuel_mass:
            raise KerbalException(f"Stage {stage_num} has lost more mass then it has before staging.")

    # when there is fuel restriction, it is necessary to remove all mass lost from firing before the restriction
    # this will decrease the fuel tank and compensate for the lost fuel.
    def prestage_mass_loss(self, stage_num, loc = 'atm'):
        _loc_check(loc)
        if not (stage_num-1) in self.restric_fuel_flow:
            return 0 # there is no mass lost if there hasn't been a restriction right before it.
        stage_engine_fired = self.find_when_engine_fired(stage_num)
        time_engine_firing = self.time_between_stages(stage_engine_fired, stage_num, loc = loc)
        thurst, isp = self.calculate_group_performance(stage_num, loc = loc)
        mass_flow = thurst/(isp*9.81)
        mass_loss = mass_flow * time_engine_firing
        self.check_mass_lost(stage_num, mass_loss)
        return mass_loss

    # return all mass lost in all stages after stage_num at current stage_num time 
    def total_prestage_mass_loss(self,stage_num, loc = 'atm'):
        _loc_check(loc)
        total_mass_lost = 0.0
        for check_stage in range(stage_num, self.num_stages()):
            if (check_stage-1) in self.restric_fuel_flow:
                stage_engine_fired = self.find_when_engine_fired(check_stage)
                if stage_engine_fired < stage_num:
                    time_engine_firing = self.time_between_stages(stage_engine_fired, stage_num, loc = loc)
                    thurst, isp = self.calculate_group_performance(check_stage, loc = loc)
                    mass_flow = thurst/(isp*9.81)
                    mass_loss = mass_flow * time_engine_firing
                    self.check_mass_lost(check_stage, mass_loss)
                    total_mass_lost += mass_loss
        return total_mass_lost

    # rocket mass lost at the end of an stage is equivalent to the mass lost at the start of the next
    def total_poststage_mass_loss(self, stage_num, loc = 'atm'):
        _loc_check(loc)
        if stage_num >= self.num_stages():
            return 0.0 # can't have anything after last stage
        return self.total_prestage_mass_loss(stage_num+1, loc = loc)

    # mass above stage_num
    def calculate_upper_mass(self,stage_num): 
        upper_mass = sum([stage.calculate_full_mass() for stage in self.stages[(stage_num+1):]]) + self.payload
        return upper_mass

    def calculate_stage_dV(self, stage_num,loc='atm'):
        _loc_check(loc)
        upper_mass = self.calculate_upper_mass(stage_num)
        total_mass = self.stages[stage_num].calculate_full_mass() + upper_mass - self.total_prestage_mass_loss(stage_num, loc = loc)
        empty_mass = self.stages[stage_num].calculate_empty_mass() + upper_mass - self.total_poststage_mass_loss(stage_num, loc = loc)

        isp = self.calculate_isp(stage_num, loc = loc)
        dV = log(total_mass/empty_mass)*isp*9.81
        return dV

    def calculate_dV(self,loc='atm'):
        _loc_check(loc)
        dV = 0
        for i,stage in enumerate(self.stages):
            dV += self.calculate_stage_dV(i,loc = loc)
        return dV

    def adjusted_dV(self, dV_out=2500): # dV_out - delta V to exit atmosphere, 2500 is kerbins
        dV_atm = self.calculate_dV(loc = 'atm')
        dV_vac = self.calculate_dV(loc = 'vac')
        dV_adj = ((dV_atm - dV_out)/dV_atm)*dV_vac + dV_out
        return dV_adj

    def calculate_total_mass(self):
        total_mass = 0
        for stage in self.stages:
            total_mass += stage.calculate_full_mass()
        return total_mass + self.payload

    def calculate_total_cost(self):
        total_cost = 0
        for stage in self.stages:
            total_cost += stage.calculate_cost()
        return total_cost

    def calculate_thrust(self, stage_num, loc='atm'):
        _loc_check(loc)
        thrust_list, _ = self.performance_engines_firing(stage_num, loc = loc)
        thrust = sum(thrust_list)
        return thrust

    def calculate_twr(self, stage_num,g=9.81,loc='atm'):
        _loc_check(loc)
        upper_mass = self.calculate_upper_mass(stage_num)
        total_mass = self.stages[stage_num].calculate_full_mass() + upper_mass - self.total_prestage_mass_loss(stage_num, loc = loc)
        thrust = self.calculate_thrust(stage_num, loc=loc)
        twr = thrust/(g*total_mass)
        return twr

    def generate_report(self, g=9.81):
        print('')
        print('--------------------------------------------')
        print('ROCKET REPORT')
        print('--------------------------------------------')
        if not self.name is None:
            print(f'Name: {self.name}')
        print(f'Mass: {round(self.calculate_total_mass(),3)} Ton')
        print(f'Cost: {self.calculate_total_cost()}')
        if self.payload > 0:
            print(f'Payload: {self.payload} Ton')
        print(f'True Delta-V: {round(self.adjusted_dV(),2)} m/s')
        print('Total vaccum dV: {} m/s'.format(round(self.calculate_dV(loc='vac'),2)))
        print('Total atmospheric dV: {} m/s'.format(round(self.calculate_dV(loc = 'atm'),2)))
        print('')
        print('--------------------------------------------')
        print('STAGES')
        print('--------------------------------------------')
        for i,stage in enumerate(self.stages):
            print(f'Stage: {i}')
            print('Delta-V: {} atm - {} vac [m/s]'.format(round(self.calculate_stage_dV(i, loc='atm'),2), round(self.calculate_stage_dV(i, loc='vac'),2)))
            print('TWR: {} atm - {} vac'.format(round(self.calculate_twr(i,g=g, loc='atm'),2), round(self.calculate_twr(i,g=g, loc='vac'),2)))
            print('Engine burn time: {} atm - {} vac [s]'.format(round(self.engine_burn_time(i, loc='atm'),2), round(self.engine_burn_time(i, loc='vac'),2)))
            print('')
        print('--------------------------------------------')
        print('NOTES')
        print('--------------------------------------------')
        print('True delta-V is the total dV adjusted')
        print('for when the craft leaves Kerbin.')
        print(f'TWR calculation used g = {g} m/s².')
        print('Engine burn time measured at full power.')
        print('--------------------------------------------')
        print('')


