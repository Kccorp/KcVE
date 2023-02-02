from cpeClass import Cpe


class Cve:
    exploitabilityScore = None
    id = None
    publishedDate = None
    lastModifiedDate = None
    description = None
    version = None
    baseScore = None
    vectorString = None

    source = None
    urlSource = None

    cpeList = []

    def __init__(self, id, publishedDate, lastModifiedDate, description):
        self.id = id
        self.publishedDate = publishedDate
        self.lastModifiedDate = lastModifiedDate
        self.description = description

    def getCvss(self, version, baseScore, vectorString, exploitabilityScore):
        self.version = version
        self.baseScore = baseScore
        self.vectorString = vectorString
        self.exploitabilityScore = exploitabilityScore

    def getSource(self, source, urlSource):
        self.source = source
        self.urlSource = urlSource

    def getCpe(self, cpeList):
        self.cpeList = cpeList

    def showAll(self):
        print("\n\n")
        print("id: " + str(self.id))
        print("publishedDate: " + str(self.publishedDate))
        print("lastModifiedDate: " + str(self.lastModifiedDate))
        print("description: " + str(self.description))
        print("version: " + str(self.version))
        print("baseScore: " + str(self.baseScore))
        print("vectorString: " + str(self.vectorString))
        print("exploitabilityScore: " + str(self.exploitabilityScore))
        print("\nVulnerable CPEs: ")
        for i in range(len(self.cpeList)):
            self.cpeList[i].showAll()
        print("\nsource: " + str(self.source))
        print("urlSource: " + str(self.urlSource))
