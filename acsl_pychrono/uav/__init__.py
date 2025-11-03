# acsl_pychrono/uav/__init__.py
from pathlib import Path
import yaml
from .X8 import X8, X8_Controller_Params
from .X8_TEST import X8_TEST, X8_TEST_Controller_Params
from .QUAD1 import QUAD1, QUAD1_Controller_Params
from .THRUSTSTAND import THRUSTSTAND, THRUSTSTAND_Controller_Params

uav_classes = {
  'X8': (X8, X8_Controller_Params),
  'X8_TEST': (X8_TEST, X8_TEST_Controller_Params),
  'QUAD1': (QUAD1, QUAD1_Controller_Params),
  'THRUSTSTAND': (THRUSTSTAND, THRUSTSTAND_Controller_Params),
}

uav_config_name = {
  'X8': "x8_config.yaml",
  'X8_TEST': "x8_test_config.yaml",
  'QUAD1': "quad1_config.yaml",
  'THRUSTSTAND': "thruststand_config.yaml",
}

def instantiateUAV(uav_type: str):
  if uav_type not in uav_classes:
    raise ValueError(f"Unknown controller type: {uav_type}")
  
  UAV_Class, UAV_Controller_Params_Class = uav_classes[uav_type]
  uav = UAV_Class()
  # Controller parameters depend on the UAV parameters to get estimates
  uav_controller = UAV_Controller_Params_Class(uav)
  
  return uav, uav_controller


def get_uav_config(uav_type: str) :
  if uav_type not in uav_classes:
    raise ValueError(f"Unknown UAV type: {uav_type}")
  
  # Prepend working directory and "/acsl_pychrono/uav/*uav_type*/*config_file_name*"
  config_file_name = uav_config_name[uav_type]
  absolute_path = Path.cwd() / "acsl_pychrono/uav" / uav_type / config_file_name
  
  with open(absolute_path, 'r') as f:
    uav_cfg = yaml.safe_load(f)
      
  return uav_cfg