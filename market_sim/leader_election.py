import random
from collections import Counter
import matplotlib.pyplot as plt
class Agent:
    def __init__(self, agent_id):
        self.id = agent_id

    def vote(self, agents):
        # Kendi dahil rastgele bir ajan için oy verir
        return random.choice(agents).id

def simulate_election(num_agents=5):
    agents = [Agent(i) for i in range(num_agents)]
    votes = [agent.vote(agents) for agent in agents]

    result = Counter(votes)
    leader_id, count = result.most_common(1)[0]

    print("Oylar:", result)
    print("Kazanan lider:", leader_id, f"({count} oy)")
    return leader_id, result



def visualize_votes(vote_counts):
    agent_ids = list(vote_counts.keys())
    votes = list(vote_counts.values())

    plt.bar(agent_ids, votes)
    plt.xlabel("Ajan ID")
    plt.ylabel("Aldığı Oy Sayısı")
    plt.title("Lider Seçimi Oy Dağılımı")
    plt.tight_layout()
    plt.show()

