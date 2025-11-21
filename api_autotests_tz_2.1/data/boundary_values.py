class Boundary:
    MIN_ID = 0
    MAX_ID = 2**63 - 1

    INVALID_IDS = [
        -1000,
        MAX_ID + 1,
        "string",
        None
    ]
