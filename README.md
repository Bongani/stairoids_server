# WBAA on Stairoids

## How to run

    docker build -t stairoids .
    docker run -p 9000:9000 stairoids
    

## Endpoints

### /event (POST)

Expects a POST with the following body:

```json
{
  "username":"john",
  "location":8,
  "time":112,
}
```

> Using CURL: `curl -d '{"username":"john","location":8,"time":112}' -H "Content-Type: application/json" -X POST http://localhost:9000/event`

### /leaderboard/<amount_of_floors> (GET)

Expects a GET with as parameter the amount of floors climbed for this leaderboard.
Example:
- `amount_of_floors=8` gives the best time per user ascending `8` floors. 
- `amount_of_floors=-6` gives the best time per user descending `6` floors.

Response:

```json
[
  {
    "time": 10.0,
    "username": "john"
  },
  {
      "time": 6.0,
      "username": "niels"
    }
]
```
