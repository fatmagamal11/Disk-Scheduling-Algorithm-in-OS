'''
SCAN
1. sort requests coming from entry
2. determine the direction of head movement
3. put all values in the requests higher than the first head_pos 
4. check if there are requests in the reverse direction , if not found stop , if found
5. complete to the last track in the current direction,then
6. put all the values in requests from the end of the current direction to the start of the reverse direction
(if [10 5 20 35 2] , h_pos: 22, requests num=50, dir right) ==> 
22==>35 ==> 50 ==>20==>10 ==>5 ==>2
'''
def scan(head, requests, tn, direction):
    li=[]
    check=0
    #sort the list
    requests.sort()
    
    #direction of right (innermost)
    if(direction=='1'):
        #use this loop to put all the requests higher than head , then check if there is a requests lower
        for e in requests:
            if e>head:
                li.append(e)
            if(e<head):
                check+=1
       #if there are no requests , so it returns the li as the ordered list
       #if there are requests , so append the last track in the direction (track count - 1)
        if(check!=0):    
            li.append(tn-1)
            #reverse the requests list
            requests.reverse()
            #append all elements that lower than head postion as it is coming from innermost to outermost
            for e in requests:
                if e<head:
                    li.append(e)
        
    #direction of left (outermost)
    elif(direction == '-1'):
        #this loop for appending all values lower than head position, then check if there are requests in the reverse direction
        for e in requests:
            if e<head:
                li.append(e)
            if(e>head):
                check+=1
        #reverse li elements to come from right to left correctly
        li.reverse()
        #if there are requests in right , go to zero , and then put all elements higher than head position in li
        if(check!=0):
            li.append(0)
            for e in requests:
                if e>head:
                    li.append(e)
    #finally returning the ordered list
    return li
