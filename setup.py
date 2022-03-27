from setuptools import setup

setup(
    name='gym_aima',
    version='0.0.2',
    description='Gym Gridworld environment of the Artificial Intelligence a Modern Approach',
    url='https://github.com/mimoralea/gym-aima',
    author='Miguel Morales',
    author_email='mimoralea@gmail.com',
    packages=['gym_aima', 'gym_aima.envs'],
    license='MIT License',
    install_requires=['gym'],
)
