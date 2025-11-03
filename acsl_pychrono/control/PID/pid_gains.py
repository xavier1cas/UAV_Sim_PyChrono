import math
import numpy as np
from numpy import linalg as LA
import scipy
from scipy import linalg
from acsl_pychrono.simulation.flight_params import FlightParams

class PIDGains:
  def __init__(self, flight_params: FlightParams):
    # General vehicle properties
    self.I_matrix_estimated = flight_params.uav_controller.I_matrix_estimated
    self.mass_total_estimated = flight_params.uav_controller.mass_total_estimated
    self.air_density_estimated = flight_params.uav_controller.air_density_estimated
    self.surface_area_estimated = flight_params.uav_controller.surface_area_estimated
    self.drag_coefficient_matrix_estimated = flight_params.uav_controller.drag_coefficient_matrix_estimated

    # Number of states to be integrated by RK4
    self.number_of_states = flight_params.uav_controller.PID_number_of_states
    # Length of the array vector that will be exported 
    self.size_DATA = flight_params.uav_controller.PID_size_DATA
    
    # **Translational** PID parameters 
    self.KP_tran = np.matrix(np.diag(flight_params.uav_controller.PID_KP_tran))
    self.KD_tran = np.matrix(np.diag(flight_params.uav_controller.PID_KD_tran))
    self.KI_tran = np.matrix(np.diag(flight_params.uav_controller.PID_KI_tran))

    # **Rotational** PID parameters
    self.KP_rot = np.matrix(np.diag(flight_params.uav_controller.PID_KP_rot))
    self.KD_rot = np.matrix(np.diag(flight_params.uav_controller.PID_KD_rot))
    self.KI_rot = np.matrix(np.diag(flight_params.uav_controller.PID_KI_rot))
    
    # ----------------------------------------------------------------
    #                   Safety Mechanism Parameters
    # ----------------------------------------------------------------
    self.use_safety_mechanism = flight_params.uav_controller.PID_use_safety_mechanism
    
    # Mu - sphere intersection
    self.sphereEpsilon = flight_params.uav_controller.PID_sphereEpsilon
    self.maximumThrust = flight_params.uav_controller.PID_maximumThrust # [N] 85
    
    # Mu - elliptic cone intersection
    self.EllipticConeEpsilon = flight_params.uav_controller.PID_EllipticConeEpsilon
    self.maximumRollAngle = math.radians(flight_params.uav_controller.PID_maximumRollAngle) # [rad] 25
    self.maximumPitchAngle = math.radians(flight_params.uav_controller.PID_maximumPitchAngle) # [rad] 25
    
    # Mu - plane intersection
    self.planeEpsilon = flight_params.uav_controller.PID_planeEpsilon
    self.alphaPlane = flight_params.uav_controller.PID_alphaPlane # [-] coefficient for setting the 'height' of the bottom plane. Must be >0 and <1.
    
    # For X8-Copter
    # # **Translational** PID parameters 
    # # self.KP_tran = np.matrix(1 * np.diag([5,5,6]))
    # # self.KD_tran = np.matrix(1 * np.diag([8,8,3]))
    # # self.KI_tran = np.matrix(1 * np.diag([1,1,1]))

    # self.KP_tran = np.matrix(1 * np.diag([77,84,35]))
    # self.KD_tran = np.matrix(1 * np.diag([34,29,6]))
    # self.KI_tran = np.matrix(1 * np.diag([129,53,53]))

    # # **Rotational** PID parameters
    # self.KP_rot = np.matrix(1 * np.diag([100,100,50]))
    # self.KD_rot = np.matrix(1 * np.diag([50,50,50]))
    # self.KI_rot = np.matrix(1 * np.diag([20,20,10]))
    
    # # ----------------------------------------------------------------
    # #                   Safety Mechanism Parameters
    # # ----------------------------------------------------------------
    # self.use_safety_mechanism = True
    
    # # Mu - sphere intersection
    # self.sphereEpsilon = 1e-2
    # self.maximumThrust = 85 # [N] 85
    
    # # Mu - elliptic cone intersection
    # self.EllipticConeEpsilon = 1e-2
    # self.maximumRollAngle = math.radians(60) # [rad] 25
    # self.maximumPitchAngle = math.radians(60) # [rad] 25
    
    # # Mu - plane intersection
    # self.planeEpsilon = 1e-2
    # self.alphaPlane = 0.6 # [-] coefficient for setting the 'height' of the bottom plane. Must be >0 and <1.