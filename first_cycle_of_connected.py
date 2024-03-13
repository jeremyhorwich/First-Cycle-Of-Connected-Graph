def find_first_cycle(path: dict, current_vertex="root", branch=None):
    if branch is None:
        branch = set()
    target = None

    branch.add(current_vertex)
    if current_vertex not in path:
        branch.remove(current_vertex)
        return None
    
    next_vertices = path[current_vertex]
    for next in next_vertices:
        if next in branch:
            target = next
            break
        branch.add(current_vertex)
        first_cycle_in_branch = find_first_cycle(path, next, branch)
        if first_cycle_in_branch is not None:
            return first_cycle_in_branch
        
    if target is None:
        branch.remove(current_vertex)
        return None
    
    cycle = [target]
    previous_vertex_in_cycle = target
    looped_back_on_target = False
    while not looped_back_on_target:
        for node in path[previous_vertex_in_cycle]:
            if node == target:
                return cycle
            if node not in branch:
                continue
            cycle.append(node)
            previous_vertex_in_cycle = node