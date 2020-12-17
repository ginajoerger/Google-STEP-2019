from collections import deque

class NotFound(Exception): pass

def find_shortest_path(graph, start, end):
    visited = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = visited[node]
            return path[::-1]
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited[neighbour] = node
                queue.append(neighbour)
    raise NotFound('No path from {} to {}'.format(start, end))

def main():
    all_links = {} 
    links = open("links.txt", "r")
    for i in links:
        first, second = i.split(",")
        second = second.strip("\n")
        if first not in all_links.keys():
            all_links[first] = [second]
        else:
            all_links[first].append(second) 
    links.close()
    
    ####
    
    nicknames = open("nicknames.txt", "r")
    name_list = {}
    for i in nicknames:
        first, second = i.split(",")
        second = second.strip("\n")
        name_list[first] = second  
    nicknames.close()
    
    ####
                
    x = input("What is your name?: ")
    
    number_is = [number for number, name in name_list.items() if name == x]
    look_for = number_is[0]
            
    print("You are " + str(len(find_shortest_path(all_links, '23', look_for))-1) + " step(s) away from Jacob.")
    print(find_shortest_path(all_links, '23', look_for))
    
            
main()
