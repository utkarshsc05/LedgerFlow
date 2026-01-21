import pandas as pd
import numpy as np

from expenses.models import Expense

def expense_summary(user):

    qs = Expense.objects.filter(user= user).values("amount", "base_category__code")

    if not qs:
        return {
            "total_expense": 0,
            "spending_by_category": {},
            "average_transaction": 0,
            "largest_transaction": 0,
            "standard_deviation": 0,
        }

    df = pd.DataFrame(list(qs))
    df["amount"] = df["amount"].astype(float)
    total_expense = float(df["amount"].sum())

    spending_by_category = (
        df.groupby("base_category__code")["amount"]
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )

    average_transaction = float(np.mean(df["amount"]))
    largest_transaction = float(np.max(df["amount"]))
    standard_deviation = float(np.std(df["amount"]))

    return {
        "total_expense": round(total_expense, 2),
        "spending_by_category": {
            k: round(float(v), 2) for k, v in spending_by_category.items()
        },
        "average_transaction": round(average_transaction, 2),
        "largest_transaction": round(largest_transaction, 2),
        "standard_deviation": round(standard_deviation, 2),
    }

