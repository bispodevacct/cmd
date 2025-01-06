class Sources:
    def __init__(self):
        self.csv = open('data/tables/costs.csv', 'r').readlines()
        self.linesLists = self.splitLines()
        self.sources = self.appendSources()
    
    def splitLines(self, delimiter=','):
        linesLists = []
        for line in self.csv:
            linesLists.append(line.split(delimiter))
        return linesLists
    
    def appendSources(self):
        sources = []
        for i in range(len(self.linesLists)):
            if i != 0:
                sources.append(self.linesLists[i][0])
        return sources
    
    def getSources(self):
        return self.sources