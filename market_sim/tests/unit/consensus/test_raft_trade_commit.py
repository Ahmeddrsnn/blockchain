from market_sim.blockchain.consensus import RaftCluster

def test_trade_replication():
    cluster = RaftCluster.make_demo_cluster(5)
    # advance to get leader
    for _ in range(15000):
        cluster.tick(1)
        if cluster.leader_id:
            break
    leader = cluster.leader_id
    assert leader

    # Fake trade object (can be any hashable)
    trade_obj = {"trade_id": 99}
    cluster.commit_command(trade_obj)
    for _ in range(1000):
        cluster.tick(1)

    # All logs must contain it at index 0 (first real entry)
    for node in cluster.nodes.values():
        assert node.log and node.log[-1].command == trade_obj
        assert node.commit_index >= 0
