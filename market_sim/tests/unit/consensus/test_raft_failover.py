from market_sim.blockchain.consensus import RaftCluster

def test_leader_failover_and_commit():
    cluster = RaftCluster.make_demo_cluster(5)

    # advance until leader exists
    for _ in range(15000):
        cluster.tick(1)
        if cluster.leader_id:
            break
    old_leader = cluster.leader_id
    assert old_leader

    # crash current leader
    cluster.crash_node(old_leader)

    # let time pass to trigger new election
    for _ in range(15000):
        cluster.tick(1)
        if cluster.leader_id and cluster.leader_id != old_leader:
            break
    new_leader = cluster.leader_id
    assert new_leader and new_leader != old_leader

    # commit after fail-over
    committed = []
    cluster.register_listener(lambda t, i, cmd: committed.append(cmd))
    cluster.commit_command("AFTER-CRASH")

    # give time to replicate
    for _ in range(2000):
        cluster.tick(1)
    assert "AFTER-CRASH" in committed
