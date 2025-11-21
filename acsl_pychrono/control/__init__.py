# acsl_pychrono/control/__init__.py
from pathlib import Path
import importlib
import pkgutil

# Discover available controller modules dynamically
_package_path = Path(__file__).parent
_discovered_controllers = {
  m.name: m.name
  for m in pkgutil.iter_modules([str(_package_path)])
  if not m.name.startswith("_")
}

def instantiateController(controller_type: str, ode_input, flight_params, timestep):
  """
  Dynamically import and instantiate the specified controller.
  Only the chosen controller module is loaded.
  """
  if controller_type not in _discovered_controllers:
    raise ValueError(f"Unknown controller type: {controller_type}")

  module_name = _discovered_controllers[controller_type]
  module = importlib.import_module(f".{module_name}", package=__name__)

  # Expected naming convention:
  #   Gains class:   <ControllerType>Gains
  #   Main class:    <ControllerType>
  #   Logger class:  <ControllerType>Logger
  class_prefix = controller_type

  try:
    GainsClass = getattr(module, f"{class_prefix}Gains")
    ControllerClass = getattr(module, f"{class_prefix}")
    LoggerClass = getattr(module, f"{class_prefix}Logger")
  except AttributeError as e:
    raise ImportError(
      f"[ERROR] {controller_type} module missing required class: {e}"
    )

  # Instantiate dynamically
  gains = GainsClass(flight_params)
  controller = ControllerClass(gains, ode_input, flight_params, timestep)
  logger = LoggerClass(gains)

  return gains, controller, logger