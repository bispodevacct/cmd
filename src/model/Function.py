import src.matrices.Resources as rsc
import src.matrices.Sources as src
import src.matrices.Targets as tgt
import src.matrices.Costs as cst

resources = rsc.Resources().getResources()
sources = src.Sources().getSources()
targets = tgt.Targets().getTargets()
costs = cst.Costs().getCosts()

class Function:
    def __init__(self):
        self.coefficients = self.appendCoefficients()
    
    def appendCoefficients(self):
        coefficients = []
        for k in range(len(resources)):
            for i in range(len(sources)):
                for j in range(len(targets)):
                    coefficients.append(costs[i][j])
        return coefficients
    
    def getCoefficients(self):
        return self.coefficients