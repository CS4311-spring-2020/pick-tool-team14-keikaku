from src.gui.graph.attack_graph_scene import AttackGraphScence

class NodeScene:
    def __init__(self):
        self.nodes = []
        self.relationships = []

        # TODO make the scene size dynamic
        self.scene_width = 64000
        self.scene_height = 64000

        self.init_ui()

    def init_ui(self):
        self.gr_scene = AttackGraphScence(self)
        self.gr_scene.set_gr_scene(self.scene_width, self.scene_height)



    def add_node(self, node):
        self.nodes.append(node)

    def add_relationship(self, relationship):
        self.relationships.append(relationship)

    def remove_node(self, node):
        self.nodes.remove(node)

    def remove_relationship(self, relationship):
        self.relationships.remove(relationship)
