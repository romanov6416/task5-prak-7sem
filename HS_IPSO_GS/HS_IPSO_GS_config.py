from Common.AlgConfig import AlgConfig


class HS_IPSO_GS_Config(AlgConfig):
    def __init__(self):
        AlgConfig.__init__(self)

        # Common algorithm parameters
        self.ps = 100  # population size
        self.k = 200  # iteration number
        self.m1 = 10  # parameter m1
        self.m2 = 20  # parameter m2

        # HS parameters
        self.par = 0.1  # pitching adjusting rating
        self.hmcr = 0.5  # harmony memory considering rate
        self.bw = 0.1  # bandwidth

        # GS parameters
        self.t_max = 100
        self.delta1 = 0.001
        self.delta2 = 0.01
        self.t = 0.99
        self.epsilon = 0.0000001

    def LoadFromXmlNode(self, node):
        AlgConfig.LoadFromXmlNode(self, node)
        try:
            self.ps = int(node.getAttribute("ps"))
            self.k = int(node.getAttribute("k"))
            self.m1 = int(node.getAttribute("m1"))
            self.m2 = int(node.getAttribute("m2"))

            self.par = float(node.getAttribute("par"))
            self.hmcr = float(node.getAttribute("hmcr"))
            self.bw = float(node.getAttribute("bw"))

            self.t_max = int(node.getAttribute("t_max"))
            self.delta1 = float(node.getAttribute("delta1"))
            self.delta2 = float(node.getAttribute("delta2"))
            self.t = float(node.getAttribute("t"))
            self.epsilon = float(node.getAttribute("epsilon"))
        except Exception as e:
            print str(e)
            raise e

