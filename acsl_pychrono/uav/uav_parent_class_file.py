import numpy as np
import pychrono as chrono
from abc import ABC, abstractmethod

class UAV_PARENT_CLASS(ABC):
    def __init__(self):
        
        # --- Unchanged parameters (These two are defined here only) ---
        self.air_density = 1.225    # Air density [kg/m^3]
        self.G_acc = 9.80665        # Gravitational acceleration
        # --------------------------------------------------------------
        
        # Get the UAV name from the class name
        self.name = ""
    
        # --- Number of Propellers ---
        self.number_of_propellers = 0
        
        # --- Aerodynamics ---
        self.surface_area = 0.0
        self.drag_coefficient = 0.0
        self.aerodynamic_force_application_point = chrono.ChVectorD(0, 0, 0)
        
        # --- Motor Parameters ---
        self.maximum_motor_thrust = 0.0
        self.minimum_motor_thrust = 0.0
        
        self.propellers_spin_directions = []
        self.motor_efficiency_matrix = None
        self.motor_efficiency_matrix_after_failure = None
        
        # --- Force positions (in each propeller) --- 
        self.motor_force_positions = []
        
        # --- Mass --- 
        self.mass_total = 0.0
        
        # --- Inertia matrix of the system (NED orientation) ---
        # (x-front, y-right, z-down), computed at the center of mass
        self.Inertia_mat_pixhawk = np.eye(3) # (Specific defined in each UAV subclass)
        
        # --- Reference Frames ---
        # Rotation Matrix that represents a fixed rotation of PI/2 rad around the X-Axis
        self.RotMat_X_PI_2_array = np.array([[1,  0,  0],
                                             [0,  0,  1],
                                             [0, -1,  0]])
        
        # Rotation Matrix that represents a fixed rotation of -PI/2 rad around the X-Axis
        self.RotMat_X_PI_2_tran_array = np.transpose(self.RotMat_X_PI_2_array)
    
    def loadFromYAML(self, cfg: dict) -> None:
        """Generic loader for shared parameters."""
        # --- Number of Propellers ---
        self.number_of_propellers = cfg["uav"].get("number_of_propellers", 0)
        
        # --- Aerodynamics ---
        self.surface_area = float(cfg["uav"]["aerodynamics"]["surface_area"])
        self.drag_coefficient = float(cfg["uav"]["aerodynamics"]["drag_coefficient"])
        # point where to apply the aerodynamic force in local frame
        self.aerodynamic_force_application_point = chrono.ChVectorD(*cfg["uav"]["aerodynamic_force_application_point"])
        
        # --- Mass --- 
        self.mass_total = cfg["uav"].get("mass_total", 0.0)
        
        # --- Inertia Matrix ---
        # Inertia matrix of the system: (drone frame + box + propellers), computed at the center of mass
        # Originally expressed in Solidworks coordinate sys (x-front, y-up, z-right)
        # If reference frame transformation is needed, it will be done in each UAV subclass,
        # so that the final inertia matrix is expressed in Pixhawk coordinate sys (x-front, y-right, z-down)
        Lxx = float(cfg["uav"]["inertia"]["Lxx"])
        Lyy = float(cfg["uav"]["inertia"]["Lyy"])
        Lzz = float(cfg["uav"]["inertia"]["Lzz"])
        Lxy = float(cfg["uav"]["inertia"]["Lxy"])
        Lxz = float(cfg["uav"]["inertia"]["Lxz"])
        Lyz = float(cfg["uav"]["inertia"]["Lyz"])
        
        self.inertia_matrix_untransformed = np.array([[Lxx, Lxy, Lxz],
                                                      [Lxy, Lyy, Lyz],
                                                      [Lxz, Lyz, Lzz]])
        
        # --- Motors ---
        self.maximum_motor_thrust = float(cfg["uav"]["motor"]["max_thrust"]) # Maximum thrust [N] per motor
        self.minimum_motor_thrust = float(cfg["uav"]["motor"]["min_thrust"]) # Minimum thrust [N] per motor
        
        self.propellers_spin_directions = cfg["uav"]["motor"]["spin_directions"] # Motors' spin direction
        self.motor_efficiency_matrix = np.matrix(np.diag(cfg["uav"]["motor"]["efficiency_matrix_diag"])) # Motor efficiency coefficients
        self.motor_efficiency_matrix_after_failure = np.matrix(np.diag(cfg["uav"]["motor"]["efficiency_matrix_diag_after_failure"])) # Motor efficiency coefficients after failure
        # Reorder or define coaxial stacking (OPTIONAL)
        self.motor_index_map = cfg["uav"]["motor"]["index_map"]
        
        # --- Force positions (in each propeller) --- 
        self.motor_force_positions = tuple(
            chrono.ChVectorD(*pos) for pos in cfg["uav"]["force_positions"]
        )
        
    @abstractmethod
    def _load_inertia(self) -> None:
        """
        Each subclass must implement this method to build the necessary parameters of the UAV.
        """
        pass
        
    @abstractmethod
    def _compute_mixer_matrix(self, cfg) -> None:
        """
        Each subclass must implement this method to build the necessary parameters of the UAV.
        """
        pass