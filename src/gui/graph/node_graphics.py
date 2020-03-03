class Node():
    def __init__(self, scene, title="Undefined Node"):
        self.scene = scene
        self.title = title
        self.grNode = QDMGraphicsNode(self, self.title)