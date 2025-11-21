# acsl_pychrono/control/uav_controller_params.py
import numpy as np
import acsl_pychrono.uav as UAV_module
from .uav_parent_class_file import UAV_PARENT_CLASS as UAV

class UAV_Controller_Params:
    def __init__(self, uav: UAV, controller_name: str):
        """
        Generic controller parameter class that loads all UAV-specific
        controller values from YAML configuration.
        """
        
        cfg = UAV_module.get_uav_config(uav.name)
        controller_cfg = cfg["controller"]

        # --- Basic UAV-level estimates ---
        self.mass_total_estimated = getattr(uav, "mass_total", 0)
        self.I_matrix_estimated = np.matrix(uav.Inertia_mat_pixhawk)
        self.surface_area_estimated = getattr(uav, "surface_area", 0)
        self.drag_coefficient_estimated = getattr(uav, "drag_coefficient", 0)
        self.air_density_estimated = getattr(uav, "air_density", 1.225)

        self.drag_coefficient_matrix_estimated = np.matrix(
            np.diag([self.drag_coefficient_estimated,
                     self.drag_coefficient_estimated, 0])
        )

        # --- Derivative Filter Gains ---
        derivative_filter_gains_cfg = controller_cfg.get("derivative_filter_gains", {})
        self.A_phi_ref = np.matrix(derivative_filter_gains_cfg.get("A_phi_ref", np.zeros((1, 1))))
        self.B_phi_ref = np.array(derivative_filter_gains_cfg.get("B_phi_ref", np.zeros((1,))))
        self.C_phi_ref = np.matrix(derivative_filter_gains_cfg.get("C_phi_ref", np.zeros((1, 1))))
        self.D_phi_ref = derivative_filter_gains_cfg.get("D_phi_ref", 0.0)

        self.A_theta_ref = np.matrix(derivative_filter_gains_cfg.get("A_theta_ref", np.zeros((1, 1))))
        self.B_theta_ref = np.array(derivative_filter_gains_cfg.get("B_theta_ref", np.zeros((1,))))
        self.C_theta_ref = np.matrix(derivative_filter_gains_cfg.get("C_theta_ref", np.zeros((1, 1))))
        self.D_theta_ref = derivative_filter_gains_cfg.get("D_theta_ref", 0.0)

        # --- Propeller dynamics ---
        self.K_omega = float(controller_cfg.get("K_omega", 0.0))
        self.K_torque = float(controller_cfg.get("K_torque", 0.0))

        # --- Controller Gains Config file references ---
        gains_cfg = controller_cfg.get("gain_yaml_files", {})
        self.controller_config_filename = gains_cfg.get(controller_name, "")