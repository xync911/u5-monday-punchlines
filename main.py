"""Copy entry.txt to the output directory for the make.fun entry.

The entry is a single joke about Monday mornings, no longer than
200 characters.
Monday shows up to work before the speaker does, sits in their
chair, and drinks their coffee. The day itself is the rude
coworker, and the punchline is that it wins every week.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
