import numpy as np

class UAV:
    def __init__(self):

        self.G_acc = 9.80665 # Gravitational acceleration
        self.air_density = 1.225 # Air density [kg/m^3]
        
        # Rotation Matrix that represents a fixed rotation of PI/2 rad around the X-Axis
        self.RotMat_X_PI_2_array = np.array([[1,  0,  0],
                                             [0,  0,  1],
                                             [0, -1,  0]])
        
        # Rotation Matrix that represents a fixed rotation of -PI/2 rad around the X-Axis
        self.RotMat_X_PI_2_tran_array = np.transpose(self.RotMat_X_PI_2_array)
        
        # This properties must be overwritten in the child classes that inherit from UAV class
        self.number_of_propellers       = None  # Number of propellers
        self.Inertia_mat_pixhawk        = None  # Inertia matrix of the system: (drone frame + box + propellers) espressed in Pixhawk coordinate sys (x-front, y-right, z-down), computed at the center of mass
        self.surface_area               = None  # Surface area of the drone to account for drag [m^2]
        self.drag_coefficient           = None  # Drag coefficient (equal to that of a plate) [-]
        self.U_mat_inv                  = None  # Moore-Penrose pseudo-inverse of X8copter mixer matrix
        self.maximum_motor_thrust       = None  # [N] Maximum thrust that can be produced by a SINGLE motor
        self.minimum_motor_thrust       = None  # [N] Minimum thrust that can be produced by a SINGLE motor
        self.motor_efficiency_matrix    = None  # Motor efficiency coefficients for simulating motor failure
        self.motor_force_positions      = None  # Position of each motor where the thrust force is applied, expressed in local frame
        self.aerodynamic_force_application_point = None # Point where the aerodynamic force is applied, expressed in local frame
        # Motors' rotation direction
        # Define spin direction of each motor: +1 for CCW, -1 for CW
        self.propellers_spin_directions = None
        