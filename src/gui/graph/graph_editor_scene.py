
from src.gui.graph.background_scene import BackgroundScene

class GraphEditorScene:
    vectos: dict
    nodes: dict
    relationships: dict

    def __init__(self):
        self.vectos = {}
        self.nodes = {}
        self.relationships = {}

        self.scene_width = 64000
        self.scene_height = 64000

        self.init_ui()

    def init_ui(self):
        self.background_scene = BackgroundScene(self.scene_width, self.scene_height)

    def add_vector(self, key, vector):
        self.vectos[key] = vector

    def add_node(self, key,  node):
        self.nodes[key] = node

    def add_relationship(self, key, relationship):
        self.relationships[key] = relationship

    def remove_vector(self, key):
        self.vectos.pop(key)

    def remove_node(self, key):
        self.nodes.pop(key)

    def remove_relationship(self, key):
        self.relationships.pop(key)