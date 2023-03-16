import gym

from typing import Optional, Union
from gym import spaces

import numpy as np

from first_mdp.Gridsearch import GridWorld


class DetAgent():
    """ The Agent class enables to play different policies for a given evironment

    :param env: The environment to learn from (if registered in Gym, can be str)
    :param use_masking: Whether or not to use invalid action masks during evaluation
    :param seed: Seed for the pseudo random generators
    :param policy_type: the type of the initialization policy
    """
    def __init__(self, env: Union[gym.Env, str] = GridWorld(5), masking: bool = True, seed: Optional[int] = None, policy_type: str = 'uniform') -> None:
        self.env = env
        print(self.env)
        self.masking = masking
        self.rng = np.random.default_rng(seed=seed)
        # size of action space
        if isinstance(self.env.action_space, spaces.Discrete):
            num_acts = self.env.action_space.n
            self.all_actions = np.arange(num_acts)
        if isinstance(self.env.observation_space, spaces.MultiDiscrete):
            self.obs_shape = self.env.observation_space.nvec
            state_type = 'MultiDiscrete'
        if isinstance(self.env.observation_space, spaces.Discrete):
            self.obs_shape = self.env.observation_space.n
            state_type = 'Discrete'
        policy_shape = np.append(self.obs_shape, num_acts)

        # Init policy # TODO: Als Funktion auslagern?
        if policy_type == 'uniform':
            self.policy = np.ones(policy_shape)/num_acts
        if policy_type == 'greedy' and state_type == 'MultiDiscrete':
            self.policy = np.zeros(policy_shape)
            for i in range(self.obs_shape[0]):
                for j in range(self.obs_shape[1]):
                    k = np.random.randint(num_acts)
                    self.policy[i, j, k] = 1
        if policy_type == 'greedy' and state_type == 'Discrete':
            self.policy = np.zeros(policy_shape)
            for i in range(self.obs_shape[0]):
                for j in range(self.obs_shape[1]):
                    k = np.random.randint(num_acts)
                    self.policy[i, j, k] = 1
        
    def get_action(self, state: np.ndarray) -> int:
        """samples an action of the environments action space for a given state

        Args:
            state (np.ndarray): gamestate of the environment

        Returns:
            action :single action, randomly generated according to policy
        """
        try:
            assert state.shape == self.obs_shape.shape
        except AssertionError:
            print('State shape of Agent and Algorithm do not match')
            raise
        
        # Update Probabilities
        self._update_action_mask_prob(state)
        # Sample Action
        action = self.rng.choice(self.all_actions, p=self.policy[tuple(state)])
        return action
    
    def _update_action_mask_prob(self, state: np.ndarray):
        """Updates the probabilities of all actions for a given state

        Args:
            state (np.ndarray): gamestate of the environment
        """
        if self.masking:
            # Get all possible actions of state:
            pos_actions = self.env.get_valid_actions(state)
            not_pos_actions = set(self.all_actions) - set(pos_actions)
            # Adjust probability of action to legal probabilities
            state_prob = self.policy[tuple(state)]
            state_prob[list(not_pos_actions)] = 0.0
            state_prob = state_prob/sum(state_prob)
            self.policy[tuple(state)] = state_prob
        
        else:
            self.policy[tuple(state)]


if __name__=="__main__":

    NUM_STEPS = 20
    environment = GridWorld(size=5)
    environment.reset()
    agent = DetAgent(env=environment)
    for _ in range(NUM_STEPS):
            state = environment.state
            action = agent.get_action(state)
            next_state, reward, done, _ = environment.step(action)
            print(f"reward is {reward}, done is {done} and action was {action}")
            environment.render()
            if done==True:
                environment.reset()