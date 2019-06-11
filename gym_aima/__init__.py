from gym.envs.registration import register

register(
    id='AIMAGridworld-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
