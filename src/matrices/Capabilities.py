class Capabilities:
    def __init__(self):
        self.csv = open('data/tables/capabilities.csv', 'r').readlines()
        self.linesList = self.splitLines()
        self.capabilities = self.appendCapabilities()
    
    def splitLines(self, delimiter=','):
        linesList = []
        for line in self.csv:
            linesList.append(line.rstrip('\n').split(delimiter))
        return linesList

    def appendCapabilities(self):
        capabilities = []
        self.linesList.pop(0)
        for line in self.linesList:
            line.pop(0)
            capabilities.append(line)
        return capabilities
    
    def getCapabilities(self):
        return self.capabilities