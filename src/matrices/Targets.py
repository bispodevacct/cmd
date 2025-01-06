class Targets:
    def __init__(self):
        self.csv = open('data/tables/costs.csv', 'r').readline().rstrip('\n')
        self.targets = self.appendTargets()
    
    def appendTargets(self):
        targets = []
        columnsList = self.csv.split(',')
        for i in range(len(columnsList)):
            if i != 0:
                targets.append(columnsList[i])
        return targets
    
    def getTargets(self):
        return self.targets