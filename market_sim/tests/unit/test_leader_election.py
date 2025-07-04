import unittest
from market_sim.blockchain.consensus.leader_election import Node, run_election

class TestLeaderElection(unittest.TestCase):
    def test_election(self):
        nodes = [Node(1), Node(3), Node(2)]
        leader = run_election(nodes)
        self.assertEqual(leader.node_id, 3)
        self.assertTrue(leader.is_leader)
        # only one leader
        self.assertEqual(sum([n.is_leader for n in nodes]), 1)

if __name__ == "__main__":
    unittest.main()
