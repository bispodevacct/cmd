class Resources:
    def __init__(self):
        self.csv = open('data/tables/demands.csv', 'r').readlines()
        self.linesLists = self.splitLines()
        self.resources = self.appendResources()
    
    def splitLines(self, delimiter=','):
        linesLists = []
        for line in self.csv:
            linesLists.append(line.split(delimiter))
        return linesLists
    
    def appendResources(self):
        resources = []
        for i in range(len(self.linesLists)):
            if i != 0:
                resources.append(self.linesLists[i][0])
        return resources
    
    def getResources(self):
        return self.resources