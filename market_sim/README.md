# Market Dynamics and Trading Simulation Framework

Implements a framework for simulating, analysing, and learning about financial
markets, trading strategies, and blockchain integration.

**Version v0**

---

## Project Structure
```
market_sim/
├── core/               # Data & utility layer
│   ├── data/
│   ├── models/
│   └── utils/
├── market/             # Exchange, agents, mechanisms, dynamics
├── strategies/         # Traditional, HFT, ML strategies
├── simulation/         # Engine, scenarios, results
├── blockchain/         # Blockchain & consensus
│   ├── ethereum/
│   ├── consensus/      # ← Raft implementation lives here
│   └── contracts/
├── analysis/           # Metrics · visualisation · reports
├── api/                # REST / WebSocket
├── ui/                 # Web • CLI • Desktop
└── tests/              # Unit · integration · performance
```

---

## Feature Highlights

### Market Simulation
* Real‑time engine with configurable parameters  
* Multiple asset types & order‑book management  
* Agent framework with pluggable strategies  

### Trading Mechanisms
* Stock, options, warrants, margin, short‑selling  
* Custom mechanism skeletons for future work  

### High‑Frequency Trading
* Ultra‑low‑latency matching engine  
* Market‑making & statistical‑arbitrage examples  

### Blockchain Integration
* Ethereum smart‑contract hooks  
* **Raft consensus module** (`blockchain/consensus/`)  
  * Leader election, log replication, crash fail‑over  
  * Trades are committed through Raft; consensus timeline visualisable  
* Cross‑chain trading & DeFi strategy stubs  

> **Try it**

```bash
# Run the consensus test‑suite
pytest market_sim/tests/unit/consensus/

# Visualise leader & commit timeline (after a quick 1‑second sim)
python - <<'PY'
from datetime import datetime, timedelta
from market_sim.simulation.engine.simulation_engine import MarketSimulation
from market_sim.analysis.visualization.raft_timeline import plot_timeline

sim = MarketSimulation(datetime.utcnow(),
                       datetime.utcnow() + timedelta(seconds=1))
sim.run()
plot_timeline(sim.raft)           # opens a Matplotlib window
PY
```

### Learning Environment
* Interactive scenarios & tutorials (work‑in‑progress)  
* Back‑testing harness with risk/performance metrics  

---

## Getting Started

```bash
# 1  Install dependencies
pip install -r requirements.txt

# 2  Run all tests
pytest

# 3  (Optionally) run coverage
pytest --cov=market_sim
```

---

## License

MIT – see the [LICENSE](../LICENSE) file.
