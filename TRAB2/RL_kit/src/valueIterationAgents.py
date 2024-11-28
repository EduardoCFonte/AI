# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util
from learningAgents import ValueEstimationAgent

import mdp, util
from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        A ValueIterationAgent solves a Markov Decision Process (MDP)
        using the value iteration algorithm for a specified number of
        iterations and discount factor.
    """
    def __init__(self, mdp, discount=0.9, iterations=100):
        """
        Initializes the agent and performs value iteration.

        Args:
            mdp: The Markov decision process to solve.
            discount: Discount factor for future rewards (gamma).
            iterations: Number of iterations to run value iteration.
        """
        self.mdp = mdp
        self.discount_factor = discount
        self.iteration_limit = iterations
        self.state_values = util.Counter()  # Default value is 0 for all states.

        # Perform Value Iteration
        for iteration in range(self.iteration_limit):
            updated_values = util.Counter()

            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    updated_values[state] = 0  # Terminal states have zero value.
                else:
                    possible_actions = self.mdp.getPossibleActions(state)
                    updated_values[state] = max(
                        self.computeQValueFromValues(state, action) for action in possible_actions
                    )

            self.state_values = updated_values  # Update state values.

    def getValue(self, state):
        """
        Retrieves the value of a given state.

        Args:
            state: The state for which to retrieve the value.

        Returns:
            The computed value of the state.
        """
        return self.state_values[state]

    def computeQValueFromValues(self, state, action):
        """
        Calculates the Q-value for a given state-action pair.

        Args:
            state: The current state.
            action: The action being evaluated.

        Returns:
            The Q-value of the state-action pair.
        """
        q_value = 0
        transitions = self.mdp.getTransitionStatesAndProbs(state, action)

        for next_state, transition_probability in transitions:
            reward = self.mdp.getReward(state, action, next_state)
            q_value += transition_probability * (
                reward + self.discount_factor * self.state_values[next_state]
            )

        return q_value

    def computeActionFromValues(self, state):
        """
        Determines the best action for a given state based on current values.

        Args:
            state: The state for which to determine the best action.

        Returns:
            The optimal action for the given state, or None if terminal.
        """
        if self.mdp.isTerminal(state):
            return None

        actions = self.mdp.getPossibleActions(state)
        return max(actions, key=lambda action: self.computeQValueFromValues(state, action))

    def getPolicy(self, state):
        """
        Returns the best policy (action) for a given state.
        """
        return self.computeActionFromValues(state)

    def getAction(self, state):
        """
        Returns the action dictated by the policy for the state.
        """
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        """
        Returns the Q-value for a specific state-action pair.
        """
        return self.computeQValueFromValues(state, action)
