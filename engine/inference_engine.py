from .ruleset import Ruleset

class InferenceEngine():

    knowledge_base = None

    def __init__(self):
        pass

    def learn(self, rules_path):
        self.knowledge_base = Ruleset(rules_path)

    def get_most_alike_destiny(self, user_ideal_destiny):
        destiny_selected = None
        max_hit = 0
        hitted_map = {}

        for destiny in self.knowledge_base.rules:
            count_field = destiny.get_similarity(user_ideal_destiny)
            if max_hit <= count_field:
                max_hit = count_field
                hitted_map[max_hit] = destiny._name

        destiny_selected = None

        if max_hit >= 4:
            destiny_selected = hitted_map[max_hit]
        destiny_data = {"name": ""}

        if destiny_selected != None:
            destiny_data = {"name": destiny_selected}

        return destiny_data
