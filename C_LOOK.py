'''
C_LOOK
1. sort requests coming from entry
2. determine the direction of head movement
3. put all values in the requests higher than the first head_pos 
4. check if there are requests in the reverse direction , if not found stop , if found
5. change its starting  direction and doesn't service any requests in the new direction
6. start serving requests when reaching to the last request found in the new direction 
7. then complete serving the requests till the end of requests but in the old direction
(if [10 5 20 35 2] , h_pos: 22, requests num=50  dir right) ==> 
22==>35 ==> 2 ==>5==>10==>20 (here it complete and not service 20, 10 ,5 ,2) it wait till take its first direction 
and serviced the requests
'''
def c_look(head, requests, tn, direction):
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
            requests.reverse()
            for e in requests:
                if e>head:
                    li.append(e)
    return li
                

    