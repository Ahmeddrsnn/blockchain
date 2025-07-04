class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.is_leader = False

def run_election(nodes):
    """
    Leader election algorithm: Bully algorithm simplified.
    Node with highest ID becomes leader.
    """
    highest_id = max(node.node_id for node in nodes)
    for node in nodes:
        node.is_leader = (node.node_id == highest_id)
    return [node for node in nodes if node.is_leader][0]

if __name__ == "__main__":
    nodes = [Node(i) for i in range(5)]
    leader = run_election(nodes)
    print(f"Leader elected: Node {leader.node_id}")
