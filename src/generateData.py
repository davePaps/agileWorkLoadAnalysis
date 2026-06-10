import pandas as pd
import random
from datetime import datetime
from calendar import month_abbr


def generate_agile_data(num_rows=1000, output_file="agile_test_data.csv"):

    counties = [
        "North Hub",
        "South Hub",
        "East Hub",
        "West Hub",
        "Central Hub"
    ]

    gp_practices = [
        "Riverside Medical Centre",
        "Oakwood Surgery",
        "Hilltop Health Centre",
        "Greenfield Practice",
        "St Mary's Surgery",
        "Park View Medical Practice",
        "The Orchard Surgery",
        "Lakeside Health Centre",
        "Willowbrook Practice",
        "Meadow Lane Surgery"
    ]

    specialties = [
        "Cardiology",
        "Oncology",
        "Respiratory",
        "Neurology",
        "Primary Care",
        "Diabetes",
        "Dermatology",
        "Mental Health"
    ]

    team_members = [
        "Sarah Jones",
        "David Smith",
        "Emma Brown",
        "Michael Taylor",
        "Sophie Wilson",
        "James Patel",
        "Rachel White",
        "Tom Evans"
    ]

    studies = [
        ("ASTRA", "Commercial"),
        ("ORION", "Commercial"),
        ("GALAXY", "Commercial"),
        ("PULSE", "Commercial"),
        ("NOVA", "Commercial"),
        ("INSIGHT", "Non-Commercial"),
        ("DISCOVER", "Non-Commercial"),
        ("IMPACT", "Non-Commercial"),
        ("HORIZON", "Non-Commercial"),
        ("FOCUS", "Non-Commercial")
    ]

    # Create unique CPMSIDs per study
    cpms_lookup = {}
    cpms_seed = 100000

    for idx, (study, _) in enumerate(studies):
        cpms_lookup[study] = cpms_seed + idx

    rows = []

    for _ in range(num_rows):

        study_acronym, study_type = random.choice(studies)

        year = random.randint(2023, 2026)
        month_num = random.randint(1, 12)

        timestamp = datetime(
            year,
            month_num,
            random.randint(1, 28),
            random.randint(8, 17),
            random.randint(0, 59),
            random.randint(0, 59)
        )

        activity_month = month_abbr[month_num]

        # Financial year calculation
        if month_num >= 4:
            fy = f"{year}/{str(year + 1)[-2:]}"
        else:
            fy = f"{year - 1}/{str(year)[-2:]}"

        screening_visits = random.randint(0, 30)

        recruited = random.randint(
            0,
            max(screening_visits, 1)
        )

        follow_ups = random.randint(
            recruited,
            recruited * 4 if recruited > 0 else 0
        )

        surveys = random.randint(
            recruited,
            recruited * 3 if recruited > 0 else 5
        )

        row = {
            "Timestamp": timestamp,
            "Activity Month": activity_month,
            "Activity Year": year,
            "Your County Hub": random.choice(counties),
            "Site": random.choice(gp_practices),
            "Study Acronym": study_acronym,
            "Study Type": study_type,
            "Have you Supported set up": random.choice([True, False]),
            "Number Screening Visits": screening_visits,
            "No recruited / Consented patients": recruited,
            "follow ups": follow_ups,
            "pres surveys distributed": surveys,
            "Agile Team member name": random.choice(team_members),
            "FY": fy,
            "CPMSID": cpms_lookup[study_acronym],
            "Managing Specialty": random.choice(specialties)
        }

        rows.append(row)

    df = pd.DataFrame(rows)

    df.to_csv(output_file, index=False)

    return df