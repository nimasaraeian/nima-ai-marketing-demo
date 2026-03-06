import csv

DATA_PATH = "mock_data/sample_leads.csv"


def score_lead(visits, clicked_cta, time_on_page):
    """
    Simple demo scoring logic to simulate AI-assisted lead prioritization.
    """

    score = 0

    # engagement signals
    if visits > 5:
        score += 2

    if clicked_cta:
        score += 3

    if time_on_page > 60:
        score += 2

    return score


def classify_lead(score):
    """
    Convert numeric score into marketing priority.
    """

    if score >= 6:
        return "HIGH"
    elif score >= 4:
        return "MEDIUM"
    else:
        return "LOW"


def analyze_leads():
    """
    Load mock data and produce prioritized leads.
    """

    results = []

    with open(DATA_PATH, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            visits = int(row["visits"])
            clicked_cta = row["clicked_cta"].lower() == "true"
            time_on_page = int(row["time_on_page"])

            score = score_lead(visits, clicked_cta, time_on_page)
            priority = classify_lead(score)

            results.append({
                "lead_id": row["lead_id"],
                "score": score,
                "priority": priority
            })

    return results


if __name__ == "__main__":
    leads = analyze_leads()

    print("AI Lead Prioritization Demo")
    print("---------------------------")

    for lead in leads:
        print(
            f"Lead {lead['lead_id']} → Score: {lead['score']} | Priority: {lead['priority']}"
        )
