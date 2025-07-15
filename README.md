# Investment

Code related to the investment section of the website.

See **[market_sim](market_sim/README.md)** for the full market‑simulation framework.

---

## Quick usage

```bash
# Example database test run
python3 test_db_operations.py
```

---

## Distributed Consensus (Raft)  🆕

> **Why?** Exchanges must stay consistent even if servers crash.  
> We embed a pure‑Python **Raft** implementation that elects a leader, replicates
> trades, and re‑elects instantly on failure.

| Feature | Details |
|---------|---------|
| Module  | `market_sim/blockchain/consensus` |
| Capabilities | Leader election < 300 ms¹, log replication, crash/restart fail‑over, commit callbacks |
| Extras  | Timeline visualiser (`raft_timeline.py`) |
| Tests   | `market_sim/tests/unit/consensus/` (4 green tests) |

Run the consensus test‑suite:

```bash
pytest market_sim/tests/unit/consensus/
```

Generate a leader/commit timeline after any simulation:

```python
from market_sim.analysis.visualization.raft_timeline import plot_timeline
plot_timeline(sim.raft)
```

<sub>¹ Simulated milliseconds in bundled unit tests.</sub>

---

## Market Dynamics and Trading Simulation

A framework for simulating, analysing, and learning about financial markets,
trading strategies, and blockchain integration. **Currently v0.**

---

## License

This project is licensed under the MIT License – see the
[LICENSE](LICENSE) file for details.

**Why MIT?**

* Encourages wide adoption & collaboration  
* Allows commercial and academic use  
* Keeps compliance simple  
* Protects contributors from liability  
* Compatible with most other open‑source projects  

---

_Project log re‑initialised on 2025‑01‑19._
