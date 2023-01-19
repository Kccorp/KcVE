class Cpe:
    vendor = None
    product = None
    version = None

    def __init__(self, vendor, product, version):
        self.vendor = vendor
        self.product = product
        self.version = version

    def showAll(self):
        print("vendor: " + str(self.vendor), end=" ")
        print("product: " + str(self.product), end=" ")
        print("version: " + str(self.version))
