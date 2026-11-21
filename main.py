import os

TEXT = (
    "You fall asleep on the night train,\n"
    "your cheek on your mother's sleeve.\n"
    "Clack. A long hush. Clack.\n"
    "Under the rails, the whole continent\n"
    "is drifting, as slowly as a fingernail grows.\n"
    "It has carried everyone, for a hundred million years.\n"
    "Tonight it carries the train, and you.\n"
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="ascii", newline="\n") as f:
    f.write(TEXT)
