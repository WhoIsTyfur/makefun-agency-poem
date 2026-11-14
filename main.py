"""make.fun agency-poem-01 entry: writes one fixed poem to /output/entry.txt."""

import os

POEM = """Planchette

At nine, at Dana's, lights off,
four of us touched the plastic heart
and asked who was there. It moved,
slow, then sure, and spelled a name
none of us would own. Each swore
she hadn't pushed. Each believed the rest.
There was one way to know:
lift your hand, and see if it stopped.
Nobody ever lifted.

Now I start an email and it finishes,
in my voice, the thing I meant, or near it,
or a little kinder than I meant.
I send it. People write back to me.

Last night it wrote my sister's birthday card
and knew about the lake.
I read it twice, my finger on the button,
and felt it moving under my hand,
and did not lift.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
