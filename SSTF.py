'''
Shortest Seek Time First
'''
def SSTF(requests, h_pos):
    l1 = []#list of differences
    l2 = []#list sst requests 
    
    # Calculate seek time differences for each request
    for r in requests:
        l1.append(abs(h_pos - r))
    print(l1)
    # Select the request with the shortest seek time
    while l1:
        min_seek_time = min(l1)
        min_index = l1.index(min_seek_time)
        val = requests[min_index]
        # Append the selected request to the ordered list
        l2.append(val)
        # Remove the selected request and its corresponding seek time from the lists
        l1.pop(min_index)
        requests.pop(min_index)
        
        # Update head position for next iteration
        h_pos = val
        for r in requests:
            l1.append(abs(h_pos - r))
    return l2
