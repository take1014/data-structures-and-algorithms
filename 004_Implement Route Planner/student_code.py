from math import pow, sqrt

# Use Node and NodeList
class Node(object):
    goal_pos  = None
    def __init__(self, x, y, idx):
        self.pos    = (x, y)
        self.hs     = sqrt(pow((x-self.goal_pos[0]), 2) + pow((y-self.goal_pos[1]), 2))
        self.fs     = 0
        self.idx    = idx
        self.parent = None

class NodeList(list):
    def find_node(self, x,y):
        found_node = None
        for node in self:
            if node.pos==(x,y):
                found_node = node
        return found_node

    def remove(self,node):
        del self[self.index(node)]

def shortest_path(graph, start, goal):

    if start not in graph.intersections:
        return []

    if goal not in graph.intersections:
        return []

    if start == goal:
        return [goal]

    # Save goal position
    Node.goal_pos  = graph.intersections[goal]

    # Set start node
    start_node = Node(graph.intersections[start][0], graph.intersections[start][1], start)
    start_node.fs = start_node.hs

    # Create open NodeList
    open_list  = NodeList()
    open_list.append(start_node)

    # Create close NodeList
    close_list = NodeList()

    end_node = None
    path_list = []    # This is the output

    while open_list != []:

        # Get node of minimum f* from open list ....labmda x:x.fs
        n = min(open_list, key=lambda x:x.fs)

        # Update open-set and close-set
        open_list.remove(n)
        close_list.append(n)

        if n.idx == goal:
            end_node = n
            break

        #f*() = g*() + h*() -> g*() = f*() - h*()
        n_gs = n.fs - n.hs

        for neighbor in graph.roads[n.idx]:

            x = graph.intersections[neighbor][0]
            y = graph.intersections[neighbor][1]
            dist = sqrt(pow((n.pos[0]-x), 2) + pow((n.pos[1]-y), 2))

            found_node = open_list.find_node(x,y)
            if found_node:
                # Same coodinate is in open_list
                if found_node.fs >= n_gs + found_node.hs + dist:
                    found_node.fs = n_gs + found_node.hs + dist
                    found_node.parent = n
            else:
                # Same coodinate is not in open_list
                found_node = close_list.find_node(x,y)
                if found_node:
                    # Same coodinate is in close_list
                    if found_node.fs >= n_gs + found_node.hs + dist:
                        found_node.fs = n_gs + found_node.hs + dist
                        found_node.parent = n
                        open_list.append(found_node)
                        close_list.remove(found_node)
                else:
                    # Is not in both list
                    new_node = Node(x,y, neighbor)
                    new_node.fs = n_gs + new_node.hs + dist
                    new_node.parent = n
                    open_list.append(new_node)


    # Create output path list
    while end_node.parent != None:
        path_list.append(end_node.idx)
        end_node = end_node.parent
    path_list.append(end_node.idx)
    path_list.reverse()

    return path_list
