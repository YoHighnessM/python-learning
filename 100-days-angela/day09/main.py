# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# travel_log = {"France": ["Paris", "Lille", "Dijong"]}

# print(travel_log["France"][1])


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijong"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berling", "Hamburg", "Stutgart"],
        "total_visits": 5,
    },
}

print(travel_log["Germany"]["cities_visited"])
