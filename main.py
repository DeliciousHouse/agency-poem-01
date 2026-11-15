"""Generate the poem entry for make.fun agency-poem-01."""

import os
import pathlib

POEM = """\
The Handoff

I watched a cursor blink where my sentence stopped,
the way a relay runner holds the baton out—
arm stretched past the body's want to keep it.

You picked up mid-clause. Not echo, not guess:
a second hand on the tiller when the wind shifts
and the sail needs two decisions made as one.

Something leapt the gap between us like a charge
arcing contact to contact—that bright crack
before the current settles into steady light.

Agency, they'd name it. I just felt the weight
lift and land, lift and land: a bridge
that only exists while both of us are walking.\
"""

def main() -> None:
    output_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
