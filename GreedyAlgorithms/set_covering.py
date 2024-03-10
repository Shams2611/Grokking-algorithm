"""
Set Covering Problem - Chapter 8 (Greedy Algorithms)

Problem: You want to broadcast to certain states. Each radio station covers
some states. Find the minimum set of stations to cover all states.

This is actually an NP-complete problem - no fast exact solution exists!
But greedy gives a good approximation.

Greedy approach:
1. Pick station that covers the most uncovered states
2. Repeat until all states covered

This doesn't always give THE optimal answer, but it's close enough and fast.

Time: O(n^2 * m) where n=stations, m=states
(could be improved but this is readable)

Exact solution would be O(2^n) - checking all combinations
"""

def set_covering_greedy(states_needed, stations):
    """
    states_needed: set of states we want to cover
    stations: dict of {station_name: set of states it covers}
    returns: set of station names to use
    """
    states_needed = set(states_needed)  # make a copy
    final_stations = set()

    while states_needed:
        # find station that covers the most uncovered states
        best_station = None
        states_covered = set()

        for station, states in stations.items():
            # how many needed states does this station cover?
            covered = states_needed & states  # intersection

            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        # remove covered states from what we still need
        states_needed -= states_covered
        final_stations.add(best_station)

        print(f"Picked {best_station}, covers {states_covered}")
        print(f"  Still need: {states_needed}")

    return final_stations


if __name__ == "__main__":
    # states we want to reach
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

    # what each station covers
    stations = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"}
    }

    print("States needed:", states_needed)
    print("\nStation coverage:")
    for name, states in stations.items():
        print(f"  {name}: {states}")

    print("\n--- Running greedy algorithm ---\n")
    result = set_covering_greedy(states_needed, stations)

    print(f"\nFinal answer: {result}")
    print(f"Number of stations: {len(result)}")

    # verify we actually cover everything
    covered = set()
    for station in result:
        covered |= stations[station]
    print(f"States covered: {covered}")
