"""
Paxos Learner module: receives accepted values from acceptors and learns the final consensus value.
"""

from collections import defaultdict
from typing import Any, Callable


class PaxosLearner:
    def __init__(self, quorum_size: int):
        self.quorum_size = quorum_size
        self.accepted: dict[int, list[Any]] = defaultdict(list)
        self.learned_value: dict[int, Any] = {}
        self.callbacks: list[Callable[[int, Any], None]] = []

    def register_callback(self, cb: Callable[[int, Any], None]):
        """Register a callback triggered when a value is learned."""
        self.callbacks.append(cb)

    def receive_accepted(self, round_id: int, value: Any):
        """Receive an accepted value from an acceptor."""
        if round_id in self.learned_value:
            return  # Already learned

        self.accepted[round_id].append(value)

        counts = defaultdict(int)
        for v in self.accepted[round_id]:
            counts[v] += 1

        for val, count in counts.items():
            if count >= self.quorum_size:
                self.learned_value[round_id] = val
                for cb in self.callbacks:
                    cb(round_id, val)
                break

    def get_learned_value(self, round_id: int) -> Any:
        return self.learned_value.get(round_id)
