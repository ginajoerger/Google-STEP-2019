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
    links = open("wiki-links.txt", "r")
    for i in links:
        first, second = i.split(",")
        second = second.strip("\n")
        if first not in all_links.keys():
            all_links[first] = [second]
        else:
            all_links[first].append(second) 
    links.close()
    
    ####
    
    page_names = open("wiki-pages.txt", "r")
    name_list = {}
    for i in page_names:
        first, second = i.split(",")
        second = second.strip("\n")
        name_list[first] = second  
    page_names.close()
    
    ####
                
    starting_point = input("Where do you want to start?: ")
    
    start_number_is = [number for number, name in name_list.items() if name == starting_point]
    look_for_start = start_number_is[0]
    
    ending_point = input("Where do you want to end?: ")
    
    end_number_is = [number for number, name in name_list.items() if name == ending_point]
    look_for_end = end_number_is[0]
            
    print("You are " + str(len(find_shortest_path(all_links, look_for_start, look_for_end))-1) + " step(s) away from Jacob.")
    print(find_shortest_path(all_links, look_for_start, look_for_end))
    
            
main()