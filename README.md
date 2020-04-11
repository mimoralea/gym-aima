# gym-aima

Package implementing the Gridworld environment that appears in
Russell & Norvig's book. It registers environments to
reproduce the results of the book and also the results
in Berkeley's AI lectures by Abbeel & Klein.

## Installation

```bash
git clone https://github.com/mimoralea/gym-aima.git
cd gym-aima
pip install .
```

or:

```bash
pip install git+https://github.com/mimoralea/gym-aima#egg=gym-aima
```

## Use

```python
import gym, gym_aima, numpy as np
def value_iteration(P, gamma=0.99, theta = 1e-10):
    V = np.zeros(len(P), dtype=np.float64)
    while True:
        Q = np.zeros((len(P), len(P[0])), dtype=np.float64)
        for s in range(len(P)):
            for a in range(len(P[s])):
                for prob, new_state, reward, done in P[s][a]:
                    Q[s][a] += prob * (reward + gamma * V[new_state] * (not done))
        if np.max(np.abs(V - np.max(Q, axis=1))) < theta:
            break
        V = np.max(Q, axis=1)
    pi = lambda s : {s:a for s, a in enumerate(np.argmax(Q, axis=1))}[s]
    return V, pi
    
def print_policy(pi, P):
    arrs = {k:v for k,v in enumerate(('<', 'v', '>', '^'))}
    for key, value in pi.items():
        print("| ", end="")
        if P[key][0][0][0] == 1.0:
            print("    ", end=" ")
        else:
            print(str(key).zfill(2), arrs[value], end=" ")
        if (key + 1) % 4 == 0: print("|")
        
# reproduce Russell & Norvig
env = gym.make('RussellNorvigGridworld-v0')
V_best_v, pi_best_v = value_iteration(env.env.P, gamma=1.0)
print(V_best_v)
print_policy(pi_best_v, env.env.P)


# reproduce Abbeel & Klein
env = gym.make('AbbeelKleinGridworld-v0')
V_best_v, pi_best_v = value_iteration(env.env.P, gamma=0.9)
print(V_best_v)
print_policy(pi_best_v, env.env.P)
```
