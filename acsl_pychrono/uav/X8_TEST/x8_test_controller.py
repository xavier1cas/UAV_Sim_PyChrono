from acsl_pychrono.uav.X8_TEST import X8_TEST
import numpy as np
import acsl_pychrono.uav as UAV_module

class X8_TEST_Controller_Params:
  def __init__(self, uav: X8_TEST):
    
    # UAV specific parameters
    cfg = UAV_module.get_uav_config("X8_TEST") # Config Dictionary
        
    self.mass_total_estimated = cfg["controller"]["mass_total_estimated"] # [kg]
    
    # Estimated quantities computed from the actual values provided by the UAV class
    self.I_matrix_estimated = np.matrix(uav.Inertia_mat_pixhawk)
    self.surface_area_estimated = uav.surface_area
    self.drag_coefficient_estimated = uav.drag_coefficient
    self.air_density_estimated = uav.air_density
    
    self.drag_coefficient_matrix_estimated = np.matrix(np.diag([self.drag_coefficient_estimated,self.drag_coefficient_estimated,0]))

    # Roll filters gains (from matlab)
    self.A_phi_ref = np.matrix(cfg["controller"]["gains"]["A_phi_ref"])
    self.B_phi_ref = np.array(cfg["controller"]["gains"]["B_phi_ref"])
    self.C_phi_ref = np.matrix(cfg["controller"]["gains"]["C_phi_ref"])
    self.D_phi_ref = cfg["controller"]["gains"]["D_phi_ref"]
    # Pitch filters gains (from matlab)
    self.A_theta_ref = np.matrix(cfg["controller"]["gains"]["A_theta_ref"])
    self.B_theta_ref = np.array(cfg["controller"]["gains"]["B_theta_ref"])
    self.C_theta_ref = np.matrix(cfg["controller"]["gains"]["C_theta_ref"])
    self.D_theta_ref = cfg["controller"]["gains"]["D_theta_ref"]
    
    self.K_omega = cfg["controller"]["K_omega"] # Propellers'thrust to square of the angular velocity
    self.K_torque = cfg["controller"]["K_torque"] # Propellers'torque to square of the angular velocity
    
    self.PID_config_file = cfg["controller"]["PID"]["config_file"]
    self.MRAC_config_file = cfg["controller"]["MRAC"]["config_file"]
    self.TwoLayerMRAC_config_file = cfg["controller"]["TwoLayerMRAC"]["config_file"]