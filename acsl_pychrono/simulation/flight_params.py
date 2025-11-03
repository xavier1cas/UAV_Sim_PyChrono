from acsl_pychrono.uav.uav import UAV

# Flight parameters class to hold UAV and controller parameters
# This class acts as a container for passing UAV and controller parameters to the simulation and controller
class FlightParams:
  def __init__(self, uav: UAV, uav_controller):

    self.uav = uav
    self.uav_controller = uav_controller
    
    # Time after the start of simulation at which the controller is switched ON
    self.controller_start_time = 0.1 #uav_cfg["controller"]["controller_start_time"]