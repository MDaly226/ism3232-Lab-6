# week6_lab.py
# Michael Daly

records = [
    {
        "id": 1,
        "name": "Michael",
        "category": "Software",
        "amount": 1500,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "Kelly",
        "category": "Equipment",
        "amount": 1000,
        "status": "Pending",
    },
    {
        "id": 3,
        "name": "Roman",
        "category": "Travel",
        "amount": 1700,
        "status": "Approved",
    },
    {
        "id": 4,
        "name": "Elijah",
        "category": "Travel",
        "amount": 900,
        "status": "Pending",
    },
    {
        "id": 5,
        "name": "Brandon",
        "category": "Equipment",
        "amount": 3000,
        "status": "Pending",
    },
]

# thresholds for loop
LIMIT = 1000
HIGH = 1400
total = 0
flagged = []
high_value = []


for record in records:
    if record["status"] == "Pending":
        total += record["amount"]
        if record["amount"] > LIMIT:
            flagged.append(record)
        if record["amount"] > HIGH:
            high_value.append(record)

# create a summary of records and print txt file
import os

os.makedirs("data", exist_ok=True)

lines = [
    f"Pending total: ${total:,.2f}",
    f"Needs review: {len(flagged)}",
    f"High-value: {len(high_value)}",
]
for line in lines:
    print(line)

with open("data/week6_summary.txt", "w") as f:
    f.write("\n".join(lines) + "\n")

print("\nRecords needing review:")
for r in flagged:
    print(f"  ID {r['id']}: {r['name']} - ${r['amount']:,.2f}")
