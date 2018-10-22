import pandas as pd
from app.models import Event
from app import db


# TODO: Filter out too large differences in time as these are likely different sessions
# TODO: (currently we check all diffs between 2 events)
def calculate_leaderboard(amount_of_floors):
    all_events = pd.read_sql(Event.query.statement, db.engine)

    if len(all_events) <= 0:
        return []
    else:
        # Filter needed columns and sort by time
        relevant_events_sorted = all_events[["username", "location", "time"]].sort_values("time")

        # Calculate the difference for time and location per user
        # (resulting in the number of floors done and the time taken for this)
        difference_matrix = relevant_events_sorted.groupby("username").diff(1).join(relevant_events_sorted[["username"]])

        # Filter the requested amount of floors done and get columns for time and user only
        results_matrix = difference_matrix.loc[difference_matrix['location'] == amount_of_floors][["time", "username"]]

        # Get minimum time for each user
        return results_matrix.loc[results_matrix.groupby("username")['time'].idxmin()].to_dict(orient='records')
