import os
import re
from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@dataclass
class Valve:
    """Object to hold valve info."""
    name: str
    flow_rate: int
    paths: list
    paths_rated: list

def rate_path(paths:list, end):
    """Compute shortest path to a valve."""
    cost = 0

    while True:
        cost += 1
        possible_paths = set()

        for x in paths:
            if x == end:
                return cost

            for y in valves[x].paths:
                possible_paths.add(y)

        paths = possible_paths

def traverse_graph(is_open:set, valves:dict, total_flow:int, current_valve:Valve, time_remaining:int):
    """Traverse graph of valves in all possible way and set max_total_flow to global variable.

    Args:
        is_open (set): Set of all valves that are open or has no flow if opened.
        valves (dict): Dict of all valves worth visiting.
        total_flow (int): Total flow in current path.
        current_valve (Valve): Valve you are currently in. Will be opened if it is not yet.
        time_remaining (int): Remaining time before volcano erupts.
    """
    global max_total_flow
    if total_flow > max_total_flow:
        max_total_flow = total_flow

    if time_remaining <= 0:
        return

    if current_valve.name not in is_open:
        #print(f"Minute {30-time_remaining}: Opening valve {current_valve.name}")
        traverse_graph(is_open.union([current_valve.name]),valves, total_flow + current_valve.flow_rate * time_remaining, current_valve, time_remaining - 1)
    else:
        for target in [valves[possible_target] for _,possible_target in current_valve.paths_rated if not valves[possible_target].name in is_open]:
            time_cost = 0
            for cost, path in current_valve.paths_rated:
                if path == target.name:
                    time_cost = cost
                    break
            
            #print(f"Minute {30-time_remaining}: Moving to {target}, cost {time_cost}")
            traverse_graph(is_open, valves, total_flow, target, time_remaining - time_cost)


if __name__ == "__main__":

    valves  = {}
    is_open = set()
    # worth needs all vavles with the flow and starting valve
    worth_valves = set(["AA"])

    with open(os.path.join(__location__,"input.txt")) as file: #5350
        lines = [line for line in (l.strip() for l in file)]

        for line in lines:
            data = line.split()
            
            # extract the name, flow rate, and paths for the valve
            name = data[1]
            flow_rate = int(re.findall(r'\d+',data[4])[0])
            paths = [path.replace(",", "") for path in data[9:]]
            
            valves[name] = Valve(name, flow_rate, paths, [])
            if flow_rate == 0: 
                is_open.add(name)
            else:
                worth_valves.add(name)

    #simplify input graph of valves to include only important ones 
    for valve_1 in sorted(list(worth_valves)):
        for valve_2 in list(worth_valves):
            if valve_1 != valve_2 and valve_2 != "AA":
                rated_path = (rate_path(valves[valve_1].paths, valve_2), valve_2)
                valves[valve_1].paths_rated.append(rated_path)

    valves_to_search = {k:v for (k,v) in valves.items() if not v.name in is_open or v.name is "AA"}

    max_total_flow = 0
    #higher than 1420
    traverse_graph(is_open, valves_to_search, 0, valves["AA"], 30-1)
    print(max_total_flow)