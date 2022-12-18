import os
import re
import heapq

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Valve:
    def __init__(self, name:str, flow_rate:int, paths:list, is_open=False):
        self.name = name
        self.flow_rate = flow_rate
        self.paths = paths
        self.is_open = is_open

    def __lt__(self, other):
        """Overload < operator for comparing Valve."""
        return self.flow_rate*(not self.is_open) > other.flow_rate*(not other.is_open)


def traverse_graph(valves:dict, current_valve:Valve, total_flow:int, time_remaining:int, path:list):
    if time_remaining < 1:
        return total_flow
    
    if current_valve.flow_rate > 0:
        current_valve.is_open = True
        time_remaining -= 1
    
    for valve in list(valves.values()):
        if valve.is_open:
            total_flow += current_valve.flow_rate

    #return max_possible_flow

def traverse_graph_a_star(valves:dict, current_valve:Valve, total_flow:int, time_remaining:int, path:list):
    # create a priority queue to store the unexplored valves, with the heuristic function as the key
    queue = []
    
    def heuristic(valve:Valve, time_remaining:int) -> int:
        """Estimate the cost by heuristic function.

        Args:
            valve (Valve): goal
            time_remaining (int): _description_

        Returns:
            int: the cost of reaching the goal from the current state (valve)
        """
        # in this case, the heuristic function simply returns the flow rate of the valve
        return -((time_remaining-1)*valve.flow_rate*(not valve.is_open))
    
    def update_total_flow(valves:dict, time_remaining:int) -> int:
        retval = 0
        opened_valves = []
        for valve in valves.values():
            if valve.is_open:
                retval += valve.flow_rate
                opened_valves.append(valve.name)

        print(f"Valves {opened_valves} are open, releasing {retval} pressure.")
        return retval

    # push the starting valve onto the queue
    heapq.heappush(queue, (heuristic(current_valve, time_remaining), current_valve))
    
    # create a set to store the explored valves
    explored = set()
    
    while queue:
        # pop the valve with the lowest heuristic value from the queue
        cost, valve = heapq.heappop(queue)
        print(cost)
        
        # skip the valve if it has already been explored
        # dont go back
        if valve in explored:
            continue
        
        explored = set()
        # add the valve to the explored set
        explored.add(valve)
        
        # check if we have run out of time
        if time_remaining < 1:
            break
        
        # decrement the time remaining
        # update the total flow for all open valves
        time_remaining -= 1
        print(f"Minute {29-time_remaining}: Moving to {valve.name}")
        total_flow += update_total_flow(valves, time_remaining)
        
        # if the valve is closed, spend 1 minute to open it
        if not valve.is_open and valve.flow_rate > 0:
            valve.is_open = True
            time_remaining -= 1
            print(f"Minute {29-time_remaining}: Opening valve {valve.name}")
            total_flow += update_total_flow(valves, time_remaining)
        
        queue = []
        # add the valve's neighbors to the queue
        for neighbor in valves[valve.name].paths:
            heapq.heappush(queue, (heuristic(valves[neighbor], time_remaining), valves[neighbor]))
    
    # return the maximum possible flow

    while time_remaining != -1:
        time_remaining -= 1
        print(f"Minute {29-time_remaining}: Standing still...")
        total_flow += update_total_flow(valves, time_remaining)
    return total_flow


if __name__ == "__main__":

    valves = {}

    with open(os.path.join(__location__,"tinput.txt")) as file: #5350
        lines = [line for line in (l.strip() for l in file)]

        for line in lines:
            data = line.split()
            
            # extract the name, flow rate, and paths for the valve
            name = data[1]
            flow_rate = int(re.findall(r'\d+',data[4])[0])
            paths = [path.replace(",", "") for path in data[9:]]
            
            valves[name] = Valve(name, flow_rate, paths)

    start_valve = valves["AA"]
    total_flow  = traverse_graph_a_star(valves, start_valve, 0, 30, [])
    print(total_flow)