import src.matrices.Resources as rsc
import src.matrices.Sources as src
import src.matrices.Targets as tgt

resources = rsc.Resources().getResources()
sources = src.Sources().getSources()
targets = tgt.Targets().getTargets()

class Variables:
    def __init__(self):
        self.variables = self.appendVariables()
    
    def appendVariables(self):
        variables = []
        for resource in resources:
            for source in sources:
                for target in targets:
                    variables.append(f'Quantity of {resource} to be distributed from {source} to {target}.')
        return variables
    
    def getVariables(self):
        return self.variables