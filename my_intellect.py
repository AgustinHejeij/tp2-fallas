from intellect.Intellect import Intellect, Callable

class MyIntellect(Intellect):
    def __init__(self):
        super(MyIntellect, self).__init__()
        self._recommended_destinies = []
        self._user_destiny = None

    @Callable
    def set_recommended_destiny(self, recommended_destiny):
        self._recommended_destinies.append(recommended_destiny)

    def get_recommended_destiny(self):
        if len(self._recommended_destinies) == 0:
            return None
        return self._recommended_destinies[0]

    @Callable
    def get_user_destiny(self):
        return self._user_destiny

    def set_user_destiny(self, destiny):
        self._user_destiny = destiny

    def learn_rules(self, rules_file):
        self.learn(Intellect.local_file_uri(rules_file))
