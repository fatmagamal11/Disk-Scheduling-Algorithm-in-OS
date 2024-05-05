'''
SCAN
1. sort requests coming from entry
2. determine the direction of head movement
3. put all values in the requests higher than the first head_pos 
4. check if there are requests in the reverse direction , if not found stop , if found
5. put all the values in requests from the end of the current direction to the start of the reverse direction
(if [10 5 20 35 2] , h_pos: 22, requests num=50 dir right) ==> 
22==>35 ==>20==>10 ==>5 ==>2
'''
def look(head, requests, tn, direction):
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
        #if there are  requests , so it returns the first request in the reverse direction 
        if(check!=0):  
            #the reverse here to obtain that the value entered is the nearest value of head position in the reverse direction
            requests.reverse()
            for e in requests:
                if e<head:
                    li.append(e)
    #direction of left (outermost)
    elif(direction == '-1'):
        for e in requests:
            if e<head:
                li.append(e)
            if(e>head):
                check+=1
        #reverse the li list
        li.reverse()
        #if there are requests in right , go to first request in the rverse direction, then put all the rest elements higher than head position in li
        if(check!=0):
            for e in requests:
                if e>head:
                    li.append(e)
    #finally returning the ordered list
    return li
                