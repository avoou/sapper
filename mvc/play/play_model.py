import itertools
from mvc.play.play_node import Node
from random import randint


class Play_model:
    def __init__(self, size_of_field):
        self.number = size_of_field
        self.number_of_bombs = 3
        self.count_of_flags = self.number_of_bombs
        self.size_of_rect = 30
        self.empty_rect = ' '
        self.win_set = set()
        self.lists_of_head = [Node() for _ in range(self.number)]
        self.len_lists_of_head = len(self.lists_of_head)
        self.val = 0
        self.count_of_open_nodes = 0
        self.required_number_of_open_nodes = (self.number*self.number) - self.number_of_bombs
        self.real_count_of_flags = 0
        self.win = None
        
        for head in self.lists_of_head:
            node = head
            node.value = self.empty_rect
            node.id = self.val
            next_node = Node()
            next_node.value = self.empty_rect
            self.val += 1
            next_node.id = self.val

            for _ in range(1,self.len_lists_of_head):
                node.right_node = next_node
                next_node.left_node = node
                node = next_node
                next_node = Node()
                next_node.value = self.empty_rect
                self.val += 1
                next_node.id = self.val
        
        for k in range(self.len_lists_of_head-1):
            one = self.lists_of_head[k]
            two = self.lists_of_head[k+1]
            #связь первого узла со вторым нижним
            one.down_node = two
            two.up_node = one

            for _ in range(self.len_lists_of_head-1):
                #связь первого узла наискосок вправо вниз со вторым
                one.down_right_node = two.right_node
                two.right_node.up_left_node = one
                #связь второго узла наискосок вправо вверз с первым
                two.up_right_node = one.right_node
                one.right_node.down_left_node = two
                #связь следующих узлов
                one.right_node.down_node = two.right_node
                two.right_node.up_node = one.right_node
                one = one.right_node
                two = two.right_node

        self.list_of_bombs = self.create_bombs(self.number_of_bombs)
        self.obj_surround_bomb_set = set()
        self.bomb_nodes = []

        for x, y in self.list_of_bombs:
            node = self.lists_of_head[x]
            for _ in range(y):
                node = node.right_node
            node.value = 'B'
            self.bomb_nodes.append(node)

        #в сет добавляются узлы которые лежат вокруг бомбы
        for bomb in self.bomb_nodes:
            for node in bomb.get_surround_node():
                if not(node == None or node.value == 'B'):
                    self.obj_surround_bomb_set.add(node)
                   
        #из сэта с узлами вокруг бом берется узел и определяется число бомб вокруг этого узла
        for _ in range(len(self.obj_surround_bomb_set)):
            node = self.obj_surround_bomb_set.pop()
            number_of_bombs = 0
            for surround_node in node.get_surround_node():
                if surround_node != None:
                    if surround_node.value == 'B':
                        number_of_bombs += 1
            node.value = number_of_bombs


    def create_bombs(self, n):
        res = []
        for _ in range(n):
            flag = True
            while flag:
                tuple_of_bombs = tuple([randint(0,self.number-1), randint(0,self.number-1)])
                if not (tuple_of_bombs in res):
                    res.append(tuple_of_bombs)
                    flag = False
        return res


    def win_check(self):
        if self.win_set == set(self.list_of_bombs) and self.count_of_open_nodes == self.required_number_of_open_nodes:
            self.win = True
            raise Exception

    def row(self, id, size_of_field):
        if id % size_of_field == id:
            return (0, id)
        else:
            return(int((id-(id % size_of_field))/size_of_field), id % size_of_field)


    def calc_field(self, id):
        x, y = self.row(id, self.number)
        res = {}
        node = self.lists_of_head[x]

        for _ in range(y):
            node = node.right_node

        if node.open or node.rmb_put:
            return None

        if node.value == 'B':
            res[node.id] = "B"   
            self.win = False
            raise Exception
            
        if isinstance(node.value, int):
            node.open = True
            res[node.id] = node.value
            self.count_of_open_nodes += 1
            self.win_check()
            return res

        nodes = itertools.chain([node], node.get_surround_node()) 
        nodes_for_opening = {}
        queue = []
        run = True

        while run:
            for surround_node in nodes:
                if surround_node != None:
                    if surround_node.rmb_put or surround_node.value == 'B':
                        continue
                    #узел не пустой, с каким либо числом
                    if surround_node.value != self.empty_rect and not surround_node.open:
                        nodes_for_opening[surround_node.id] = surround_node.value
                        surround_node.open = True
                        self.count_of_open_nodes += 1
                        continue
                    elif not surround_node in nodes_for_opening and not surround_node.open:
                        surround_node.open = True
                        nodes_for_opening[surround_node.id] = surround_node.value
                        queue.append(surround_node)
                        self.count_of_open_nodes += 1
            nodes = []
            for node_in_queue in queue:
                for n in node_in_queue.get_surround_node():
                    if n != None and not n.open:
                        if not n.id in nodes_for_opening:
                            nodes.append(n)
            queue = []
            if len(nodes) == 0:
                break
        self.win_check()
        return nodes_for_opening

    def make_flag(self, id):
        x, y = self.row(id, self.number)
        node = self.lists_of_head[x]
        for _ in range(y):
            node = node.right_node
        if not node.open:
            if node.rmb_put:
                self.real_count_of_flags -= 1
                self.win_set.remove((x,y))
                node.rmb_put = False
                self.win_check()
                return True
            elif self.real_count_of_flags < self.count_of_flags:
                self.real_count_of_flags += 1
                self.win_set.add((x, y))
                self.win_check()
                node.rmb_put = True
                return False

