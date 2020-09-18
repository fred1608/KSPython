"""A collection of classes, functions and methods to aid in Kerbal Space Program design.

"""


from math import log
from collections import defaultdict


class KerbalException(Exception):
    """

    Exception called when there is issues with KSPython implementation.

    """
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
    """Basic Part class for generating new parts.

    Parameters
        ----------
        name - `string`
            The name of the part.
        mass - `float/int`
            The mass of the part.
        cost - `float/int`
            Part cost.


    """
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
    """Liquid fuel tank class for generating new parts.

    Parameters
        ----------
        name - `string`
            The name of the part.
        mass_full - `float/int`
            The mass of the part when it is full.
        mass_empty - `float/int`
            The mass of the part when it is empty.
        cost - `float/int`
            Part cost.
    
    Example
        -------
        >>> Jumbo64 = RocketFuelTank("Rockomax Jumbo-64 Fuel Tank", 36, 4, 5750)

    Note
        ----------
        * Basic parts have already been inserted through RocketFuelTankParts, but new ones can be made by utilising this class.
    """
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
    """Liquid engine class for generating new parts.

    Parameters
        ----------
        name - `string`
            The name of the part.
        mass - `float/int`
            The mass of the part.
        cost - `float/int`
            Part cost.
        thrust_atm - `float/int`
            Atmospheric engine thrust, in kN.
        thrust_vac - `float/int`
            Vacuum engine thrust, in kN.
        isp_atm - `float/int`
            Atmospheric engine ISP, in s.
        isp_vac - `float/int`
            Vacuum engine ISP, in s.
    
    Example
        -------
        >>> REM3 = LiquidEngine('RE-M3 "Mainsail" Liquid Fuel Engine', 6, 13000, 1379.03, 1500, 285, 310)

    Note
        ----------
        * Basic parts have already been inserted through LiquidEngineParts, but new ones can be made by utilizing this class.

    """
    def __init__(self, name, mass, cost, thrust_atm, thrust_vac, isp_atm, isp_vac): 
        super().__init__(name, mass, cost, thrust_atm, thrust_vac, isp_atm, isp_vac)

class SolidEngine(Engine):
    """Liquid engine class for generating new parts.

    Parameters
        ----------
        name - `string`
            The name of the part.
        mass_full - `float/int`
            The mass of the part when it is full.
        mass_empty - `float/int`
            The mass of the part when it is empty.
        cost - `float/int`
            Part cost.
        thrust_atm - `float/int`
            Atmospheric engine thrust, in kN.
        thrust_vac - `float/int`
            Vacuum engine thrust, in kN.
        isp_atm - `float/int`
            Atmospheric engine ISP, in s.
        isp_vac - `float/int`
            Vacuum engine ISP, in s.
    
    Example
        -------
        >>> RT10 = SolidEngine('RT-10 "Hammer" Solid Fuel Booster', 3.56, 0.75, 400, 197.9, 227, 170, 195)

    Note
        ----------
        * Basic parts have already been inserted through BoosterParts, but new ones can be made by utilising this class.
    """

    def __init__(self, name, mass_full, mass_empty, cost, thrust_atm, thrust_vac, isp_atm, isp_vac): 
        super().__init__(name, mass_full, cost, thrust_atm, thrust_vac, isp_atm, isp_vac)
        self.mass_empty = _number_check(mass_empty)

class Stage:
    """The stage class incorporates parts and is inserted into a rocket.

    It is one of the basic classes of this project. It is used as a collection of parts, 
    and represents a section of the rocket.

    In the stage, a form of engine and fuel must be present. Other parts can be represented as extra mass and
    extra cost.

    Notes
        -----------
        * Different fuel types or engine types (solid or liquid) cannot be placed on the same stage.
        * Only use one type of solid booster per stage.

    """

    def __init__(self):
        self.parts = []
        self.extra_mass = 0.0
        self.extra_cost = 0.0

    def add_part(self, part):
        """
        Add a part to an stage.

        Parameters
            ----------
            part - `part`
                Part to be added to a stage.

        """
        if not isinstance(part, Part): # compare the Class part and the part being inserted
            raise KerbalException('Only parts can be added to a stage.')
        else:
            self.parts.append(part)
        self._check_for_parts_not_allowed_together()

    def add_parts(self, parts): # Input is a list of parts
        """
        Add parts to an stage.

        Parameters
            ----------
            parts - `list of parts`
                Parts to be added to a stage.

        """

        for part in parts:
            self.add_part(part)

    def list_parts(self):
        """

        Prints all parts present in a stage.

        """
        parts_dict = defaultdict(int)
        for part in self.parts:
            parts_dict[part] +=1
        for part in parts_dict:
            print(f'{part.name}: {parts_dict[part]}')

    # def remove_part(self):
    #     pass

    def add_extra_mass(self, mass):
        """
        Add extra mass to an stage. Used mainly to add other parts that are not engines or fuel tanks.

        Parameters
            ----------
            mass - `int/float`
                Mass to be added [ton].

        """
        self.extra_mass += _number_check(mass)

    def add_extra_cost(self, cost):
        """
        Add extra cost to an stage. Used mainly to add other parts that are not engines or fuel tanks.

        Parameters
            ----------
            cost - `int/float`
                Cost to be added.

        """
        self.extra_cost += _number_check(cost)

    def calculate_full_mass(self):
        """
        Calculate the mass of the stage when it is full.

        Return
            ----------
            mass_sum - `float`
                Total mass of full stage [ton].

        """
        mass_sum = self.extra_mass
        for part in self.parts:
            mass_sum += part.mass
        return mass_sum

    def calculate_cost(self):
        """
        Calculate the full cost of a stage.

        Return
            ----------
            cost_sum - `float`
                Total cost of stage.

        """
        cost_sum = self.extra_cost
        for part in self.parts:
            cost_sum += part.cost
        return cost_sum

    def calculate_empty_mass(self):
        """
        Calculate the mass of the stage when it is empty.

        Return
            ----------
            mass_sum - `float`
                Total mass of empty stage [ton].

        """
        mass_sum = self.extra_mass
        for part in self.parts:
            if hasattr(part, 'mass_empty'):
                mass_sum += part.mass_empty
            else:
                mass_sum += part.mass
        return mass_sum

    def get_engine_performance(self, loc='atm'): # all engines from stage
        """
        Calculate the relative thrust and isp of all engines within this stage.

        Return
            ----------
            thrust - `float`
                Relative thrust for all engines of this stage [kN].
            isp - `float`
                Relative ISP value for all engines of this stage [s]. 

        """
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

    def _check_for_parts_not_allowed_together(self):
        """
        Raises an exception if two parts that are not allowed together are placed in the same stage.

        """
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
        """
        Returns the fuel type being used within the same stage.  

        """
        for part in self.parts:
            if isinstance(part, SolidEngine):
                return 'solid'
            if isinstance(part, RocketFuelTank):
                return 'liquid'


class Rocket:
    """Rocket class, it is where most of the calculations occur, it also receives stages as inputs.

    The rocket activates each stage in the order that they have been inserted, burning its fuel, turning its engine on and discarding older stages.

    It is possible to have engines fire before their stage by using *schedule_engine* method. Fuel will not be consumed by
    the later stages, and will only be used by the one being fired (assuming they share a type and it is possible to do so).

    If this is not the intended operation, fuel flow can also be restricted. 

    Parameter
        ----------
        name (optional) - `string`
            Name of the rocket.

    """
    def __init__(self,name = None):
        self.stages = []
        self.name = name
        self.payload = 0 # simulated rocket payload in Tons
        self.async_engines = defaultdict(list) # this dictionary links engines that fire before their stage {stage_fire:[stages_present]} 
        self.restric_fuel_flow = [] # this list contains all stages that have restricted fuel flow in between the stage number intered and the next stage

    def add_stage(self, stage):
        """
        Add a stage to an rocket.

        Stages must be added in order, from first (ascension) to last 

        Parameters
            ----------
            stage - `stage`
                Stage to be added to the rocket.

        """
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
        """
        Add stages to an rocket.

        Stages must be added in order, from first (ascension) to last 

        Parameters
            ----------
            stages - `list of stages`
                Stages to be added to the rocket.

        """
        for stage in stages:
            self.add_stage(stage)

    def num_stages(self):
        """
        Number of stages in a rocket.

        Return
            ----------
            num_stage - `int`
                Number of stages in a rocket.

        """
        return len(self.stages)

    def change_payload(self, payload):
        """
        Adds a payload (or change its value, in case this method was used before) that will be carried by the rocket.

        Parameters
            ----------
            payload - `int/float`
                Payload to be added to a rocket [ton].

        """
        self.payload = _number_check(payload)

    # 
    # stage_max limits this function to be performed only to stages smaller or equal than it
    def performance_engines_firing(self, stage_num, stage_max = None, loc = 'atm'):
        """
        This method gets engine performance from all engines that are firing together in more complex stagings, at the time of stage_num.
        
        It can also be restricted to return only values up to a limit stage, defined by stage_max. This is useful when calculating fuel flow with fuel restrictions. 

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            stage_max - `int`
                Maximum stage to which results will be brought (including stage_max).
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            thrust_list - `list of thrusts`
                List the thrust of the engines [kN]. 
            isp_list - `list of ISPs`
                List the ISP of the engines [s].             

        """
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

    def engine_burn_time(self, stage_num, loc = 'atm'): # note: burn time is from stage start to stage end. I
        """
        This method calculates the total time an stage will spend burning at maximum thrust.

        Note that if an engine was started before its stage, and it wasn't able to receive fuel from other stages,
        the fuel lost before it started will be considered in decreasing total burn time.

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            burn_time - `float`
                Total burn time [kN].             

        """
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
        """
        This method returns the total cumulative time between the start of two stages. 

        Parameters
            ----------
            stage_ini - `int`
                Initial stage.
            stage_end - `int`
                Final stage.
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            total_time - `float`
                Total time between stages [s].             

        """

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
        """
        Calculates the relative ISP of all engines firing at a given stage. 

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            isp - `float`
                Relative ISP of engines [s].             

        """
        _loc_check(loc)
        thrust_list, isp_list = self.performance_engines_firing(stage_num, loc = loc)
        total_thrust = sum(thrust_list)
        relative_thurst = sum([thrust_list[i]/isp_list[i] for i in range(len(isp_list))])
        isp = total_thrust / relative_thurst
        return isp

    # the thurst and isp of a group of rockets that are firing together and share common fuel
    def calculate_group_performance(self, stage_num, loc='atm'):
        """
        Calculates the total thrust and relative ISP of all engines firing at a given stage that share common fuel. 

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            total_thrust - `float`
                Total thrust of engines [kN]. 
            isp - `float`
                Relative ISP of engines [s].             

        """
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
        """
        Schedule engines to fire before their normal stage. 

        Parameters
            ----------
            stage_fire - `int`
                Stage to fire engines.
            stage_present - `int`
                Stage which is to fire their engines.           

        """
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

    def rem_fuel_flow(self, stage_num):
        """
        Restrict the fuel flow in the rocket between the assigned stage and next one.

        In normal operation, fuel will always be passed from smaller stages to the upper ones automatically when applicable.
        Using this will prevent the rocket from moving fuel upstage. Setting this is not required when fuel flow is impossible,
        for example when using solid rocket boosters.

        Parameters
            ----------
            stage_num - `int`
                Stage where the operation will be executed.


        """ 
        stage_num = int(stage_num)
        if not stage_num in self.restric_fuel_flow:
            self.restric_fuel_flow.append(stage_num)
            self.restric_fuel_flow.sort() # list must always be sorted to avoid issues with calculate_group_isp algorithm

    def find_when_engine_fired(self,stage_num):
        """
        If the stage being analyzed has been scheduled to fire, return when. Else it returns itself.

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.

        Return
            ----------
            stage_fire - `int`
                Stage where engines fire.            

        """
        stage_fire = stage_num # default is to fire at own stage
        for key in list(self.async_engines):
            if stage_num in self.async_engines[key]:
                stage_fire = key
                return stage_fire
        return stage_fire

    def check_mass_lost(self, stage_num, mass_loss):
        """
        Verifies how much fuel mass a stage has, and if it is greater than a test value at any given stage.

        Raises exception if test fails.  

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            mass_loss - `float`
                Mass to be verified if greater than fuel mass.

        """
        fuel_mass = self.stages[stage_num].calculate_full_mass() - self.stages[stage_num].calculate_empty_mass()
        if mass_loss > fuel_mass:
            raise KerbalException(f"Stage {stage_num} has lost more mass then it has before staging.")

    # when there is fuel restriction, it is necessary to remove all mass lost from firing before the restriction
    # this will decrease the fuel tank and compensate for the lost fuel.
    def prestage_mass_loss(self, stage_num, loc = 'atm'):
        """
        Calculates how much mass an stage has lost before the rocket staged into it.

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            mass_loss - `float`
                Total mass lost by the stage [ton].              

        """
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
        """
        Calculates how much mass the whole rocket has lost in stages above the stage being analyzed when at the stage's start.

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            total_mass_lost - `float`
                Total mass lost by the rocket [ton].             

        """
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
        """
        Calculates how much mass the whole rocket has lost in stages above the stage being analyzed at the stage's end.

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            total_mass_lost - `float`
                Total mass lost by the rocket [ton].             

        """
        _loc_check(loc)
        if stage_num >= self.num_stages():
            return 0.0 # can't have anything after last stage
        return self.total_prestage_mass_loss(stage_num+1, loc = loc)

    # mass above stage_num
    def calculate_upper_mass(self,stage_num):
        """
        Total mass of the rocket above the stage being analyzed (without including it). 

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            upper_mass - `float`
                Upper mass of the rocket [ton].
        """ 
        upper_mass = sum([stage.calculate_full_mass() for stage in self.stages[(stage_num+1):]]) + self.payload
        return upper_mass

    def calculate_stage_dV(self, stage_num,loc='atm'):
        """
        Calculates the delta-V present in a single stage. 

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            dV - `float`
                Delta V of the stage [m/s].            

        """
        _loc_check(loc)
        upper_mass = self.calculate_upper_mass(stage_num)
        total_mass = self.stages[stage_num].calculate_full_mass() + upper_mass - self.total_prestage_mass_loss(stage_num, loc = loc)
        empty_mass = self.stages[stage_num].calculate_empty_mass() + upper_mass - self.total_poststage_mass_loss(stage_num, loc = loc)

        isp = self.calculate_isp(stage_num, loc = loc)
        dV = log(total_mass/empty_mass)*isp*9.81
        return dV

    def calculate_dV(self,loc='atm'):
        """
        Calculates the delta-V present in the rocket. 

        Parameters
            ----------
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            dV - `float`
                Delta V of the rocket [m/s].            

        """
        _loc_check(loc)
        dV = 0
        for i,stage in enumerate(self.stages):
            dV += self.calculate_stage_dV(i,loc = loc)
        return dV

    def adjusted_dV(self, dV_out=2500): # dV_out - delta V to exit atmosphere, 2500 is kerbins
        """
        Calculates the true delta-V present in the rocket, by adjusting for the total required for leaving atmosphere. 

        Parameters
            ----------
            dV_out - `int/float`
                Delta-V required to leave the atmosphere of a given body [m/s]. 
                    * 2500 - Kerbin 

        Return
            ----------
            dV - `float`
                Delta V of the rocket [m/s].            

        """
        dV_atm = self.calculate_dV(loc = 'atm')
        dV_vac = self.calculate_dV(loc = 'vac')
        dV_adj = ((dV_atm - dV_out)/dV_atm)*dV_vac + dV_out
        return dV_adj

    def calculate_total_mass(self):
        """
        Total mass of the rocket full.

        Return
            ----------
            total_mass - `float`
                Total mass of the rocket [ton].            

        """
        total_mass = 0
        for stage in self.stages:
            total_mass += stage.calculate_full_mass()
        return total_mass + self.payload

    def calculate_total_cost(self):
        """
        Total cost of the rocket.

        Return
            ----------
            total_cost - `float`
                Total cost of the rocket.            

        """
        total_cost = 0
        for stage in self.stages:
            total_cost += stage.calculate_cost()
        return total_cost

    def calculate_thrust(self, stage_num, loc='atm'):
        """
        Calculates the total thrust of all engines firing at a given stage. 

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            thrust - `float`
                Total thrust of engines [kN].            

        """
        _loc_check(loc)
        thrust_list, _ = self.performance_engines_firing(stage_num, loc = loc)
        thrust = sum(thrust_list)
        return thrust

    def calculate_twr(self, stage_num,g=9.81,loc='atm'):
        """
        Calculates the thrust to weight ratio of the rocket for a given stage. 

        Parameters
            ----------
            stage_num - `int`
                Stage to be analyzed.
            g - `float`
                Gravity (default for Kerbin).
            loc - `{'atm', 'vac'}`
                Location where the method will be performed.

        Return
            ----------
            twr - `float`
                Thrust to weight ratio.         

        """
        _loc_check(loc)
        upper_mass = self.calculate_upper_mass(stage_num)
        total_mass = self.stages[stage_num].calculate_full_mass() + upper_mass - self.total_prestage_mass_loss(stage_num, loc = loc)
        thrust = self.calculate_thrust(stage_num, loc=loc)
        twr = thrust/(g*total_mass)
        return twr

    def generate_report(self, g=9.81):
        """
        Print a report with the most important informations of a rocket. 

        Parameters
            ----------
            g - `float`
                Gravity (default for Kerbin).             

        """
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


