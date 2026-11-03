"""Bug prioritization: priority score = severity x business impact."""
import csv
from pathlib import Path

BUGS_FILE = Path(__file__).parent / "bugs.csv"


def priority_score(severity, impact):
    """Transparent rule-based score (1 to 25)."""
    return int(severity) * int(impact)


def priority_label(score):
    if score >= 20:
        return "Critical"
    if score >= 12:
        return "High"
    if score >= 6:
        return "Medium"
    return "Low"


def load_bugs(path=BUGS_FILE):
    with open(path, newline="", encoding="utf-8") as f:
        bugs = list(csv.DictReader(f))
    for b in bugs:
        b["score"] = priority_score(b["severity"], b["impact"])
        b["priority"] = priority_label(b["score"])
    return sorted(bugs, key=lambda b: b["score"], reverse=True)


if __name__ == "__main__":
    print(f"{'ID':<8}{'Title':<46}{'Sev':<5}{'Imp':<5}{'Score':<7}Priority")
    print("-" * 80)
    for b in load_bugs():
        print(f"{b['id']:<8}{b['title']:<46}{b['severity']:<5}{b['impact']:<5}"
              f"{b['score']:<7}{b['priority']}")