# J26-CSNE-310 — Adaptive Cyber-Physical Edge System for Fair Active Power Curtailment in Solar Grids

## Team

| Component | Owner | Folder |
|---|---|---|
| 1 — Embedded & Hardware | Sandes O M S | `components/embedded/` |
| 2 — Network & Security | Wimalasena D C B V D S | `components/network/` |
| 3 — Edge Intelligence | Wanniarachchi C P | `components/edge/` |
| 4 — Cloud Analytics | Somachandra K P D M | `components/cloud/` |

## Repo Structure

```
j26-csne-310-rp/
├── components/
│   ├── embedded/     # Component 1
│   ├── network/      # Component 2
│   ├── edge/         # Component 3
│   └── cloud/        # Component 4
│       each has: src/, tests/, requirements.txt, README.md
│       (edge/ also has notebooks/ and data/)
├── shared/            # common constants + MQTT data models
├── docs/              # proposal, TAF, module policy PDFs
├── scripts/
├── .gitignore
├── requirements-dev.txt   # pytest, black, ruff
└── README.md
```

Your component folder is your kingdom — do what you want in there. `shared/` is common ground: never delete or rename what's already in it, and tell the team before adding to it. Don't touch someone else's component folder without asking first.

## First-Time Setup

```powershell
git clone https://github.com/wanniarachchichaluka/j26-csne-310-rp.git
cd j26-csne-310-rp\components\edge   # swap "edge" for your own component

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r ..\..\requirements-dev.txt   # optional: pytest, black, ruff
```

## Using `shared/`

```python
from shared.constants import VOLTAGE_LIMITS, QOS_LEVELS
from shared.models import SolarData, GridData
```

This only resolves if the repo root is on the Python path. Run your own scripts as modules **from the repo root**:

```powershell
python -m components.edge.src.main
```

`python components\edge\src\main.py` will NOT find `shared` — running a script directly only puts its own folder on the path, not the root. In a notebook, add this to the first cell instead:

```python
import sys
sys.path.insert(0, r"C:\Users\user\Desktop\j26-csne-310-rp")  # adjust if your clone lives elsewhere
from shared.constants import VOLTAGE_LIMITS
```

## Git Workflow

**Never commit to `main`. Always work on a feature branch.**

### Branches

| Type | Format | Example |
|---|---|---|
| Feature | `feature/component-description` | `feature/edge-pv-forecast` |
| Fix | `fix/component-description` | `fix/edge-voltage-calculation` |
| Hotfix | `hotfix/description` | `hotfix/critical-bug` |

### Daily loop

```powershell
# start
git checkout main
git pull origin main
git checkout -b feature/edge-your-task

# during work
git add components/edge/
git commit -m "feat(edge): add XGBoost model for hosting capacity"
git push origin feature/edge-your-task

# before opening a PR
git checkout main
git pull origin main
git checkout feature/edge-your-task
git rebase main
git push origin feature/edge-your-task --force-with-lease
```

### Commit messages

Format: `type(scope): brief description`. Scope is your component: `embedded`, `network`, `edge`, `cloud`, or `shared`.

| Type | Use |
|---|---|
| feat | new feature |
| fix | bug fix |
| refactor | code change, no behavior change |
| docs | documentation |
| test | tests |
| chore | maintenance |

```powershell
# good
git commit -m "feat(edge): implement Random Forest for hosting capacity"
git commit -m "fix(edge): correct voltage conversion factor"

# bad
git commit -m "fixed stuff"
```

### Merge conflicts

```
<<<<<<< HEAD
your changes
=======
their changes
>>>>>>> main
```
Resolve, remove the markers, then:
```powershell
git add <file>
git rebase --continue
```

### Opening a PR

Open when: your tests pass, your branch is rebased on the latest `main`, there are no conflicts, and your commits follow the convention above. Title it `[Component N] short description` and get a review before merging. Turn on branch protection for `main` in the GitHub repo settings so this is enforced, not just agreed on.

## Never Commit

```
.venv/, venv/, env/
__pycache__/, *.pyc
.vscode/, .idea/
.env, *.pem, *.key, secrets.json
```
All covered in `.gitignore`. If you hit something new that shouldn't be tracked, add it there and mention it in the team chat rather than working around it locally.
