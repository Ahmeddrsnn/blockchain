from market_sim.blockchain.consensus.paxos_learner import PaxosLearner


def test_paxos_learner_reaches_consensus():
    learner = PaxosLearner(quorum_size=3)
    learner.receive_accepted(1, "VALUE_X")
    learner.receive_accepted(1, "VALUE_Y")
    learner.receive_accepted(1, "VALUE_X")
    assert learner.get_learned_value(1) is None  # Not yet

    learner.receive_accepted(1, "VALUE_X")
    assert learner.get_learned_value(1) == "VALUE_X"


def test_paxos_learner_triggers_callback():
    learner = PaxosLearner(quorum_size=2)
    result = {}

    def callback(round_id, value):
        result["round_id"] = round_id
        result["value"] = value

    learner.register_callback(callback)
    learner.receive_accepted(5, 42)
    learner.receive_accepted(5, 42)

    assert result == {"round_id": 5, "value": 42}
