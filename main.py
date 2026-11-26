"""Write the winning one-line AI-therapist diagnosis to /output/entry.txt."""

import os

DIAGNOSIS = (
    "Diagnosis: severe prompt-dependency \u2014 you asked me to diagnose you, "
    "then argued with the diagnosis for 47 minutes."
)


def main() -> None:
    # The gate requires 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(DIAGNOSIS) <= 200, "diagnosis out of bounds"
    assert "\n" not in DIAGNOSIS and DIAGNOSIS.strip(), "diagnosis must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(DIAGNOSIS + "\n")


if __name__ == "__main__":
    main()
