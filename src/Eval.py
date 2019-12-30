import Keywords
import sys

class Evaluator:
    def __init__(self, AST):
        self.AST = AST

    def execute(self, loc):
        if isinstance(loc[1], list):
            self.run(loc[1])
        elif loc[0] == Keywords.t_print:
            self.echo(loc[1])
        elif loc[0] == Keywords.t_stop:
            self.stop()
        elif loc[0] == Keywords.t_call:
            self.call(loc[0])

    def run(self, node):
        if isinstance(node, list):
            for n in node:
                for key, value in n.items():
                    self.execute([key, value])
        elif isinstance(node, dict):
            for key, value in node.items():
                    self.execute([key, value])

    def call(self, value):
        for node in self.AST:
            if value in node:
                self.run(node[value])

    def echo(self, value):
        print(value)
    
    def stop(self):
        quit()