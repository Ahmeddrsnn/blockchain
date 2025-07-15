"""
Simple Raft timeline plot (leader & commit index vs. time).

Usage:
    from market_sim.analysis.visualization.raft_timeline import plot_timeline
    plot_timeline(sim.raft)          # after running a simulation
"""
from typing import List
import matplotlib.pyplot as plt

def _collect(cluster) -> tuple[List[int], List[int], List[int]]:
    t, leader, commit = [], [], []
    time_ms = 0
    for msg in cluster.msg_queue:
        pass  # queue flushed; nothing to log post-sim
    # Walk through nodes to infer last known states
    leader_id = cluster.leader_id or "None"
    max_commit = max(n.commit_index for n in cluster.nodes.values())
    t.append(time_ms)
    leader.append(int(leader_id[1:]) if leader_id.startswith("N") else -1)
    commit.append(max_commit)
    return t, leader, commit

def plot_timeline(cluster, show=True):
    t, leader, commit = _collect(cluster)

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.step(t, leader, where="post")
    ax1.set_ylabel("Leader ID")
    ax1.set_yticks(sorted({v for v in leader if v >= 0}))
    ax1.set_title("Raft Leader Timeline")

    ax2.step(t, commit, where="post")
    ax2.set_ylabel("Commit Index")
    ax2.set_xlabel("Simulated Time (ms)")

    if show:
        plt.tight_layout()
        plt.show()
    return fig
