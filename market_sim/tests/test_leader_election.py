from market_sim.leader_election import simulate_election

def test_election_returns_leader():
    leader_id, vote_counts = simulate_election(num_agents=5)
    assert leader_id in vote_counts
    assert vote_counts[leader_id] == max(vote_counts.values())
