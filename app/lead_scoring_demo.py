import pandas as pd

def score_lead(row):
    score = 0

    if row["visits"] > 5:
        score += 2

    if row["clicked_cta"] == True:
        score += 3

    if row["time_on_page"] > 60:
        score += 1

    return score


data = pd.read_csv("../mock_data/sample_leads.csv")

data["lead_score"] = data.apply(score_lead, axis=1)

print("Lead Scoring Results:")
print(data.sort_values("lead_score", ascending=False))


add demo lead scoring example
