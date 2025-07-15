"""
Consensus Testbed: Abstracts consensus implementations (Raft, Paxos) under a unified interface
to compare performance, agreement, and fault tolerance.
"""

from typing import Any, Callable, Optional
from market_sim.blockchain.consensus import RaftCluster
from market_sim.blockchain.consensus.paxos_learner import PaxosLearner
import uuid


class ConsensusTestbed:
    def __init__(self, algorithm: str = "raft", quorum_size: int = 3):
        self.algorithm = algorithm.lower()
        self.callbacks: list[Callable[[Any], None]] = []

        if self.algorithm == "raft":
            self.backend = RaftCluster.make_demo_cluster(quorum_size)
            self.backend.register_listener(self._on_raft_commit)
        elif self.algorithm == "paxos":
            self.backend = PaxosLearner(quorum_size)
            self.backend.register_callback(self._on_paxos_learned)
        else:
            raise ValueError("Unsupported consensus algorithm")

    def register_listener(self, cb: Callable[[Any], None]):
        self.callbacks.append(cb)

    def submit_command(self, command: Any):
        if self.algorithm == "raft":
            self.backend.commit_command(command)
        elif self.algorithm == "paxos":
            # Simulate a round of accepted messages to Paxos learner
            round_id = uuid.uuid4().int % 10000
            for _ in range(self.backend.quorum_size):
                self.backend.receive_accepted(round_id, command)

    def tick(self, ms: int = 100):
        if self.algorithm == "raft":
            self.backend.tick(ms)

    def _on_raft_commit(self, term: int, index: int, command: Any):
        for cb in self.callbacks:
            cb(command)

    def _on_paxos_learned(self, round_id: int, value: Any):
        for cb in self.callbacks:
            cb(value)
