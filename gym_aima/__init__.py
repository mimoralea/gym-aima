from gym.envs.registration import register

register(
    id='AIMAGridworldNoLivingPenalty-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldTinyLivingPenalty-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -0.01},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldSmallLivingPenalty-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -0.04},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumLivingPenalty-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -0.1},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLargeLivingPenalty-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -2},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLargeLivingBonus-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': 2},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
