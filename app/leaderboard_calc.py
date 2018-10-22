import pandas as pd
from app.models import Event
from app import db


def calculate_leaderboard(amount_of_floors):
    all_events = pd.read_sql(Event.query.statement, db.engine)[["username", "location", "time"]].sort_values("time")

    difference_matrix = all_events.groupby("username").diff(1).join(all_events[["username"]])
    results_matrix = difference_matrix.loc[difference_matrix['location'] == amount_of_floors][["time", "username"]]
    return results_matrix.loc[results_matrix.groupby("username")['time'].idxmin()].to_dict(orient='records')
