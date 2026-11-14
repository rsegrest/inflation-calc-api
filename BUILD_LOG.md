# BUILD LOG — inflation-calc-api

Flask API serving US CPI figures (BLS, 1913 → present) and inflation arithmetic.
Deployed on Vercel: **https://inflation-calc-api.vercel.app** (project
`rick-segrests-projects/inflation-calc-api`). Consumed by `inflation-calc-gui`.

## How it deploys

- Git-integration production deploy on push to `main` (no `vercel.json`; Vercel's
  zero-config Python/Flask detection finds the WSGI `app` in `src/app.py`).
- Runtime pinned by `.python-version`; dependencies come from `pyproject.toml`
  (Vercel installs with `uv sync`). `requirements.txt` is used by Docker/Heroku.
- Local run: `PYTHONPATH=./src python src/app.py` (port 5000).
- Tests: `./runtest.sh` (pytest, `PYTHONPATH=./src`).

## Timeline

| Date | Change |
| --- | --- |
| 2026-02 | Vercel migration; `.python-version` added, Python bumped to 3.13 |
| 2026-07-26 | API wired to the GUI (`/cpi-data` consumed by the front end) |
| 2026-08-12 | Last green production deploy (`aea95a4`, July 2026 data) |
| 2026-09-11 | Production deploy FAILS (`a615085`, August data) — silent |
| 2026-10-14 | Production deploy FAILS (`91e1593`, September data) — silent |
| 2026-11-14 | Production deploy FAILS (`010acb8`, October data) — data never went live |

## 2026-11-14

**Fixed: three months of failed production deploys.**

Symptom: the deployed GUI showed "Latest CPI Data: July, 2026" while the repo
held October data. Cause was upstream — the API project had not deployed since
12 August, and the GUI was faithfully displaying stale API output.

Build log (`vercel inspect dpl_A2QgFjMh6StxHZZ3fHAVS5HpbU95 --logs`):

```
Using Python 3.13 from .python-version
Using uv 0.13.5 (x86_64-unknown-linux-gnu)
Installing required dependencies from pyproject.toml...
Error: [BUILD_FAILED] Failed to run "uv sync --active --no-dev --link-mode hardlink --locked --no-editable"
error: No interpreter found for Python 3.13.0 in managed installations or search path
```

`.python-version` pinned an exact patch (`3.13.0`). Vercel's builder ships the
3.13 *line* (3.13.17) as a managed install and has Python downloads disabled, so
an exact patch request can never resolve. Reproduced identically on a clean
managed-install dir with downloads disabled:

```
A: .python-version = 3.13.0 → error: No interpreter found for Python 3.13.0 ...
B: .python-version = 3.13   → builds
```

**Fix:** `.python-version` → `3.13` (commit `199376e`). Deploy went green in 13s;
`/cpi-data` now serves October 2026 (337.511) and the GUI shows it.

Lesson: never pin a Python *patch* version for Vercel — only the minor line
(`3.12`, `3.13`, `3.14`).

**Added: `/cpi` monthly series + `GET /latest-data`.**

So the GUI can render every figure from one API response and hold no inflation
math of its own (it previously duplicated the formulas in TypeScript, and threw
away the `/cpi` response it requested). `/cpi` now returns a `series` array
(one entry per month, `value` = what one dollar of the start month is worth),
and `/latest-data` reports the newest month with a CPI figure so the client
doesn't have to derive it from the whole table.

Tests: 7 added (series shape, series values, explicit-end-date honouring,
aggregate figures, `/latest-data` against the query layer).

## Test suite: green

All 26 pass. The three wall-clock time-bombs that always failed ("will break at
the end of the month/year") now assert their relationship to the clock instead of
a snapshot, so they stay valid in any month:

- date helper tests compare against `datetime.now()` and a local month-name list
  rather than a hard-coded "February";
- `get_year_range` is checked as a range from this year back to 1914.

They surfaced a real bug: `get_present_cpi()` started its search at month `0`, so
it reported *January's* CPI of the current year — `325.252` instead of the newest
published figure `337.511`. It now starts from the actual current month, and a
regression test derives the expected figure from the raw data table (not from the
function under test) so the two can't agree with each other by accident.
