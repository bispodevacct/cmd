class Costs:
    def __init__(self):
        self.csv = open('data/tables/costs.csv', 'r').readlines()
        self.linesLists = self.splitLines()
        self.costs = self.appendCosts()
    
    def splitLines(self, delimiter=','):
        linesLists = []
        for line in self.csv:
            linesLists.append(line.rstrip('\n').split(delimiter))
        return linesLists
    
    def appendCosts(self):
        costs = []
        self.linesLists.pop(0)
        for line in self.linesLists:
            line.pop(0)
            costs.append(line)
        return costs
    
    def getCosts(self):
        return self.costs