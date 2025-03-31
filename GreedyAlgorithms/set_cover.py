"""
Set covering problem

Cover all states with minimum radio stations.
NP-complete - greedy gives approximation!
"""

def set_cover(states_needed, stations):
    states_needed = set(states_needed)
    picked = []

    while states_needed:
        best = None
        covered = set()

        for station, states in stations.items():
            overlap = states_needed & states
            if len(overlap) > len(covered):
                best = station
                covered = overlap

        states_needed -= covered
        picked.append(best)

    return picked


states = {"mt", "wa", "or", "id", "nv", "ut"}
stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv"},
}

print("Pick:", set_cover(states, stations))
