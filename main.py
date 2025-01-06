import src.matrices.Sources as src
import src.matrices.Targets as tgt
import src.matrices.Resources as rsc
import src.matrices.Costs as cst
import src.matrices.Capabilities as cpb
import src.matrices.Demands as dmd
import src.model.Variables as var
import src.model.Function as fun

sources = src.Sources().getSources()
targets = tgt.Targets().getTargets()
resources = rsc.Resources().getResources()
costs = cst.Costs().getCosts()
capabilities = cpb.Capabilities().getCapabilities()
demands = dmd.Demands().getDemands()
variables = var.Variables().getVariables()
coefficients = fun.Function().getCoefficients()

print(sources)
print(targets)
print(resources)
print(costs)
print(capabilities)
print(demands)
print(variables)
print(coefficients)