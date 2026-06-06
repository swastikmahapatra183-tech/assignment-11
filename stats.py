"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    pass


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    pass


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    pass


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    pass
"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    totals: dict[str, float] = {}
    counts: dict[str, int] = {}

    for record in records:
        name = record["name"]
        score = record["score"]

        totals[name] = totals.get(name, 0) + score
        counts[name] = counts.get(name, 0) + 1

    return {
        name: round(totals[name] / counts[name], 2)
        for name in totals
    }
ans

def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    return {record["subject"] for record in records}


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    averages = average_per_student(records)
    return max(averages.items(), key=lambda item: item[1])


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    averages = average_per_student(records)

    return sorted(
        name
        for name, average in averages.items()
        if average >= threshold
    )
