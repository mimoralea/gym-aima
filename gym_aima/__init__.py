from gym.envs.registration import register


# Classic Gridworld environments
register(
    id='NorvigRussellGridworld-v0',
    # To reproduce must use gamma of 1.0 (no discount)
    entry_point='gym_aima.envs:AIMAEnv',
    # With or without the sink state it will work
    # because they don't use discounting
    kwargs={'noise': 0.2, 'living_rew': -0.04, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    # To reproduce must use gamma of 0.9
    id='AbbeelKleinGridworld-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': 0.0, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)


# Low Noise, With Sink Final State, All living costs
register(
    id='AIMAGridworldLowNoiseNoLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': 0.0, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLowNoiseTinyLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -0.01, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLowNoiseSmallLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -0.04, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLowNoiseMediumLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -0.1, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLowNoiseLargeLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -2, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLowNoiseLargeLivingBonusWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': 2, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)

# Medium Noise, With Sink Final State, All living costs
register(
    id='AIMAGridworldMediumNoiseNoLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': 0.0, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumNoiseTinyLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': -0.01, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumNoiseSmallLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': -0.04, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumNoiseMediumLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': -0.1, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumNoiseLargeLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': -2, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumNoiseLargeLivingBonusWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': 2, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)

# High Noise, With Sink Final State, All living costs
register(
    id='AIMAGridworldHighNoiseNoLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': 0.0, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldHighNoiseTinyLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': -0.01, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldHighNoiseSmallLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': -0.04, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldHighNoiseMediumLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': -0.1, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldHighNoiseLargeLivingCostWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': -2, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldHighNoiseLargeLivingBonusWithSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': 2, 'sink': True},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)

# Low Noise, Without Sink Final State, All living costs
register(
    id='AIMAGridworldLowNoiseNoLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': 0.0, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLowNoiseTinyLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -0.01, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLowNoiseSmallLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -0.04, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLowNoiseMediumLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -0.1, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLowNoiseLargeLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': -2, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldLowNoiseLargeLivingBonusNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.2, 'living_rew': 2, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)

# Medium Noise, Without Sink Final State, All living costs
register(
    id='AIMAGridworldMediumNoiseNoLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': 0.0, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumNoiseTinyLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': -0.01, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumNoiseSmallLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': -0.04, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumNoiseMediumLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': -0.1, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumNoiseLargeLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': -2, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldMediumNoiseLargeLivingBonusNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.5, 'living_rew': 2, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)

# High Noise, Without Sink Final State, All living costs
register(
    id='AIMAGridworldHighNoiseNoLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': 0.0, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldHighNoiseTinyLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': -0.01, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldHighNoiseSmallLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': -0.04, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldHighNoiseMediumLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': -0.1, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldHighNoiseLargeLivingCostNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': -2, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='AIMAGridworldHighNoiseLargeLivingBonusNoSink-v0',
    entry_point='gym_aima.envs:AIMAEnv',
    kwargs={'noise': 0.6666, 'living_rew': 2, 'sink': False},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
