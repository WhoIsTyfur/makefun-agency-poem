"""make.fun agency-poem-01 entry: writes one fixed poem to /output/entry.txt."""

import os

POEM = """Shorthand

For thirty-one years my grandmother
took his letters down in Pitman,
hooks and loops nobody else in the building could read,
and typed them clean, and he signed
whatever she set in front of him.
He'd say, Tell Harris he's finished.
She'd type, We will not be renewing at this time,
with thanks for many years.

Once, she told me near the end,
he gave her the letter that closed the Leeds mill.
Four hundred jobs. She took it down.
She put the page in her drawer.
He never asked. The mill ran nine more years.
She said it the way you'd say you'd salted the soup.

Now an agent answers my mail.
It is kinder than I am, and faster,
and I sign whatever it sets in front of me.

Last night I asked it,
Is there anything you didn't send?
The three grey dots came,
and went,
and came.
"""


def main() -> None:
    # The grader mounts /output; MAKEFUN_OUTPUT_DIR lets a local run write elsewhere.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
