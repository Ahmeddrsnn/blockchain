from market_sim.blockchain.consensus.consensus_testbed import ConsensusTestbed


def test_testbed_with_raft():
    seen = []
    testbed = ConsensusTestbed(algorithm="raft", quorum_size=3)
    testbed.register_listener(lambda cmd: seen.append(cmd))

    for _ in range(20):
        testbed.tick(100)

    testbed.submit_command("ORDER_1")

    # Allow log to be replicated
    for _ in range(10):
        testbed.tick(100)

    assert "ORDER_1" in seen



def test_testbed_with_paxos():
    seen = []
    testbed = ConsensusTestbed(algorithm="paxos", quorum_size=2)
    testbed.register_listener(lambda cmd: seen.append(cmd))

    testbed.submit_command("ORDER_X")
    assert "ORDER_X" in seen
