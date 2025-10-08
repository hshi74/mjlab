import gymnasium as gym

gym.register(
  id="mjlab_velocity_rough_toddlerbot_2xc",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.rough_env_cfg:ToddlerBotRoughEnvCfg",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:ToddlerBotPPORunnerCfg",
  },
)

gym.register(
  id="mjlab_velocity_rough_toddlerbot_2xc_play",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.rough_env_cfg:ToddlerBotRoughEnvCfg_PLAY",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:ToddlerBotPPORunnerCfg",
  },
)


gym.register(
  id="mjlab_velocity_flat_toddlerbot_2xc",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.flat_env_cfg:ToddlerBotFlatEnvCfg",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:ToddlerBotFlatPPORunnerCfg",
  },
)

gym.register(
  id="mjlab_velocity_flat_toddlerbot_2xc_play",
  entry_point="mjlab.envs:ManagerBasedRlEnv",
  disable_env_checker=True,
  kwargs={
    "env_cfg_entry_point": f"{__name__}.flat_env_cfg:ToddlerBotFlatEnvCfg_PLAY",
    "rl_cfg_entry_point": f"{__name__}.rl_cfg:ToddlerBotFlatPPORunnerCfg",
  },
)
