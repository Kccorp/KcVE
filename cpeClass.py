class Cpe:
    vendor = None
    product = None
    version = None
    minVersion = None
    maxVersion = None

    def __init__(self, vendor, product, version):
        self.vendor = vendor
        self.product = product
        self.version = version

    def getMinVersion(self, minVersion):
        self.minVersion = minVersion

    def getMaxVersion(self, maxVersion):
        self.maxVersion = maxVersion

    def showAll(self):
        print("vendor: " + str(self.vendor), end=" ")
        print("product: " + str(self.product), end=" ")
        print("version: " + str(self.version))
        if self.minVersion is not None:
            print("minVersion: " + str(self.minVersion), end=" ")
        if self.maxVersion is not None:
            print("maxVersion: " + str(self.maxVersion))
