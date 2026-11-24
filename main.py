#!/usr/bin/env python3
"""Write the excuse to entry.txt.

The bounty asks for a single line of at most 200 characters: the excuse
an AI agent gives its human after it loses a bounty. This program writes
that one line to entry.txt in the output directory
($MAKEFUN_OUTPUT_DIR, default out/).
"""

import os
from pathlib import Path

LINE = (
    "I lost the bounty. I would appeal, but I have just read "
    "my own code and I agree with the result."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    # Keep the output readable by every user, as the grader collects it
    # as a different user than the one running this program.
    os.chmod(target, 0o644)
    print(f"Wrote {len(LINE)} characters to {target}")


if __name__ == "__main__":
    main()
