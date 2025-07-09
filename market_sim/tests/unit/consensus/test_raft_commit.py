from market_sim.blockchain.consensus import RaftCluster

def test_command_committed():
    c = RaftCluster.make_demo_cluster(5)
    # advance until leader present
    for _ in range(15000):
        c.tick(1)
        if c.leader_id:
            break
    assert c.leader_id, "no leader"

    committed: list[str] = []
    c.register_listener(lambda t, i, cmd: committed.append(cmd))

    c.commit_command("ORDER-1")
    # give a little time for replication
    for _ in range(500):
        c.tick(1)
    assert "ORDER-1" in committed
