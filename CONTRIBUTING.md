# Contributing

`catalog.json` is the single source of truth. `README.md`, `llms.txt` and `docs/index.html` are
generated from it, so never edit those by hand.

## Add a library

```bash
python3 scripts/refresh_catalog.py --add owner/repo --category Animation --tags swiftui,effects --no-refresh
python3 scripts/render.py
python3 scripts/render.py --check
```

Then open a pull request with the diff. `--category` must be one of Alert, Animation,
Collection View, Indicator, Menu, Table View, Transition, UI. Add `--featured` for a
standout library and `--title` when the repository name is ambiguous (for example
`Grid (exyte)`).

Optional: drop a preview GIF (under 5 MB) at `motion-book/<title>.gif` and set the
entry's `gif` field to that path. The MotionBook app streams previews from here.

### What gets in

- Actively maintained (a push in the last two years, not archived) and builds on the
  current Xcode.
- A real motion / transition / UI-animation library for iOS (UIKit or SwiftUI).
- At least 200 GitHub stars, or a clear reason in the pull request why it belongs
  anyway.
- A README that shows how to install and use it.

## Fix or remove an entry

Edit `catalog.json`, run `python3 scripts/render.py`, and open a pull request. To remove a
library, open an issue or a pull request that deletes its object.

## Refreshing numbers

The `refresh` workflow runs every Monday: it pulls stars, last push, license, archived
state, the latest tag and Swift Package Manager support for every entry, regenerates the
generated files and commits the result. You can run the same locally with an
authenticated `gh`:

```bash
python3 scripts/refresh_catalog.py && python3 scripts/render.py
```

## Agents welcome

Pull requests prepared by coding agents are fine as long as they follow the steps above
and `python3 scripts/render.py --check` passes. Keep each pull request to one library (or
one refresh) so review stays quick.
