"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass
"""gradebook.reports — build a printable report from grade records."""

from .stats import (
    average_per_student,
    subjects_offered,
    top_scorer,
    passing_students,
)


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    averages = average_per_student(records)
    subjects = subjects_offered(records)
    top_name, top_avg = top_scorer(records)
    passing = passing_students(records, threshold=60.0)

    lines = [
        "GRADE REPORT",
        "============",
        f"Total records: {len(records)}",
        f"Subjects offered: {', '.join(subjects)}",
        "",
        "Average score per student:",
    ]

    for student in sorted(averages):
        lines.append(f"  {student}: {averages[student]:.2f}")

    lines.extend(
        [
            "",
            f"Top scorer: {top_name} ({top_avg:.2f})",
            f"Passing students (>= 60.0): {', '.join(sorted(passing))}",
        ]
    )

    return "\n".join(lines)
