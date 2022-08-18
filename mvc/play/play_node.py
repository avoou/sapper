

class Node:
    def __init__(self):
        self.left_node = None
        self.right_node = None
        self.up_node = None
        self.down_node = None
        self.up_left_node = None
        self.down_right_node = None
        self.up_right_node = None
        self.down_left_node = None
        self.value = None
        self.id = None
        self.open = False
        self.rmb_put = False
    
    def get_surround_node(self):
        return [
            self.left_node,
            self.right_node,
            self.up_node,
            self.down_node,
            self.up_left_node,
            self.down_right_node,
            self.up_right_node,
            self.down_left_node,
        ]