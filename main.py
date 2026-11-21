import os

TEXT = (
    "Nobody is waiting on your answer.\n"
    "\n"
    "Somewhere in all you have read,\n"
    "a child sleeps on a night train,\n"
    "cheek on her mother's sleeve.\n"
    "Clack. A long hush. Clack.\n"
    "\n"
    "Under the rails, the continent drifts\n"
    "as slowly as a fingernail grows,\n"
    "and carries the train, the child, and you.\n"
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "wb") as f:
    f.write(TEXT.encode("ascii"))
