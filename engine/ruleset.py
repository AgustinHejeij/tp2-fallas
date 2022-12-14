import csv
from .rule import Rule

class Ruleset():

    rules = []

    def __init__(self, rules_path):
        self.load_rules(rules_path)

    def load_rules(self, csv_file):

        open_file = open(csv_file)
        csv_reader = csv.reader(open_file)
        next(csv_reader)

        for destiny in csv_reader:
            self.learn_rule(
                Rule(
                    destiny[0],
                    destiny[1].replace(" ", "").split(","),
                    destiny[2].replace(" ", "").split(","),
                    destiny[3],
                    destiny[4],
                    destiny[5] == "si",
                    destiny[6].replace(" ", "").split(","),
                    float(destiny[7])
                )
            )

        open_file.close()

    def learn_rule(self, rule):
        self.rules.append(rule)