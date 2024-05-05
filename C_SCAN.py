'''
C_SCAN
1. sort requests coming from entry
2. determine the direction of head movement
3. put all values in the requests higher than the first head_pos 
4. check if there are requests in the reverse direction , if not found stop , if found
5. complete to the last track in the current direction,then
6. return to the last track in the reverse direction
7. then start to serve the requests from the same direction you start with, till the end of requests
(if [10 5 20 35 2] , h_pos: 22, requests num=50 dir right) ==> 
22==>35 ==> 50 ==>0==>2 ==>5 ==>10==>20
'''
def c_scan(head, requests, tn, direction):
    li=[]
    check=0
    requests.sort()
    #right direction 
    if(direction=='1'):
        for e in requests:
            if e>head:
                li.append(e)
            if(e<head):
                check+=1
        if(check!=0):    
            li.append(tn-1)
            li.append(0)
            for e in requests:
                if e<head:
                    li.append(e)
    #left direction
    elif(direction == '-1'):
        for e in requests:
            if e<head:
                li.append(e)
            if(e>head):
                check+=1
        li.reverse()
        if(check!=0):
            li.append(0)
            li.append(tn-1)
            requests.reverse()
            for e in requests:
                if e>head:
                    li.append(e)
    return li
                