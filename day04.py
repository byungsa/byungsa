import pandas as pd

data = {
    "name": ["김철수", "이영희", "박민수", "최지훈", "정수진"],
    "department": ["IT", "인사", "IT", "재무", "IT"],
    "age": [35, 29, 41, 33, 27],
    "login_count": [120, 45, 180, 70, 95]
}

df = pd.DataFrame(data)
print(df)


print(df[df["department"] == "IT"])

print(df[(df["department"] == "IT") & (df["age"] >= 30)])

print(df[(df["department"] == "IT") & (df["login_count"] >= 100)])

print(df.groupby("department")["age"].mean())

print(df.groupby("department")["name"].count())