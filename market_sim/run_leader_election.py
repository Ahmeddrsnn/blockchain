from leader_election import simulate_election, visualize_votes

if __name__ == "__main__":
    leader, vote_counts = simulate_election(num_agents=5)
    visualize_votes(vote_counts)
