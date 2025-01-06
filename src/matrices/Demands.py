class Demands:
    def __init__(self):
        self.csv = open('data/tables/demands.csv', 'r').readlines()
        self.linesLists = self.splitLines()
        self.demands = self.appendDemands()
    
    def splitLines(self, delimiter=','):
        linesLists = []
        for line in self.csv:
            linesLists.append(line.rstrip('\n').split(delimiter))
        return linesLists
    
    def appendDemands(self):
        demands = []
        self.linesLists.pop(0)
        for line in self.linesLists:
            line.pop(0)
            demands.append(line)
        return demands
    
    def getDemands(self):
        return self.demands