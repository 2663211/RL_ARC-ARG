class RandomAgent:

    def select_action(self, action_space):
        return action_space.sample()