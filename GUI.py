#imports for tkinter , files to use the functions
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from FCFS import FCFS
from SSTF import SSTF
from SCAN import scan
from LOOK import look
from C_SCAN import c_scan
from C_LOOK import c_look

#**********************************************

options = ["FCFS", "SSTF","SCAN","LOOK","C-SCAN","C-LOOK"] #algorithms  list
directions=["Right (inward)","Left (outward)"] #directions list
algorithm=""  #variable will hold the name of selected algorithm
direction=""  #variable will hold the direction of head movement
tot_seek=0    #variabe will hold the total seek time of tracks travelled

#**********************************************

#algorithm selection handling
def on_select(event):
    global algorithm
    algorithm = sel_algorithm.get()
    if algorithm in ["FCFS", "SSTF"]:
        dir_sel.configure(state="disabled")
    else:
        dir_sel.configure(state="normal")
      
#direction selection handling        
def Dir_Sel(event):
    
        global direction
        d=dir_sel.get()
        if(d=="Right (inward)"):
            direction="1"
            
        else:
            direction="-1"
            
#handling what will happen after clicking on the button
def on_click():
    
    disk_req=[]
    entry_req=req_entry.get()
    requests=str_to_list(entry_req)
    
    if(not entry_req and not t_count_entry.get() and not h_pos_entry.get()):
        messagebox.showinfo("Error","no inputs")
    elif(not entry_req):
      messagebox.showinfo("Requests Error","you forget to enter requests")
    elif(not h_pos_entry.get()):
        messagebox.showinfo("Error","you forget to enter the head position")
    elif(not t_count_entry.get()):
        messagebox.showinfo("Error","you forgot tracks count")
    elif(int(h_pos_entry.get())>int(t_count_entry.get()) or int(t_count_entry.get()) < max(requests)+1):
        messagebox.showinfo("Error","wrong in inputs")
    else:
        track_count=int(t_count_entry.get())
        head_pos=int(h_pos_entry.get())
        if(not algorithm and not direction):
            tk.messagebox.showinfo("Error","you must choose")
        elif(not algorithm):
            tk.messagebox.showinfo("Error","you must choose an algorithm")
        elif(not direction and not (algorithm=="FCFS" or algorithm=="SSTF")):
            tk.messagebox.showinfo("Error","you must choose a direction")
        else:
            if algorithm=="FCFS":
               disk_req=FCFS(requests)
            elif(algorithm=="SSTF"):
                disk_req=SSTF(requests,head_pos)
            elif(algorithm=="SCAN"):
                disk_req=scan(head_pos, requests,track_count, direction)
            elif(algorithm=="LOOK"):
                disk_req=look(head_pos, requests,track_count, direction)
            elif(algorithm=="C-SCAN"):
                disk_req=c_scan(head_pos, requests,track_count, direction)
            elif(algorithm=="C-LOOK"):
                disk_req=c_look(head_pos, requests,track_count, direction)
            
            network(track_count,disk_req,head_pos)
    
#convert string of entry to list of int values
def str_to_list(entry_req):
    requests=entry_req.split(' ')
    requests = [x for x in requests if x != ""]
    for i in range(len(requests)):
        requests[i] = int(requests[i])
    return requests
    
#coordinates of (tracks and seek time), graph drawing   
def network(tn, li,first_track,time=1):
    root=tk.Tk()
    root.title(algorithm)
    global tot_seek
    #calaculate seek time
    tot_seek=abs(first_track-li[0])*time
    
    for i in range(1,len(li)):
      tot_seek+=(abs(li[i-1]-li[i])*time)
      
    canvas = tk.Canvas(root, width=800, height=800)
    canvas.create_line(50, 550, 550,550, fill="blue", tags="line") #horezintal line
    canvas.create_line(50, 50, 50,550, fill="blue", tags="line") #vertical line
    canvas.create_text(50,35,text="seek time")
    canvas.create_text(575,550,text="tracks")
    canvas.create_text(275,600, text="order of requests: "+str(li), font=("Arial",14))
    canvas.create_text(275,620, text="total seek time: "+str(tot_seek), font=("Arial",14))
    
    for i in range(0,6):
        n=50+i*100  #handle division of 500 length of axis to 5 locations each space 100 in length
        t=int(i*((tn-1)/5)) #to show the division in x axis as from 0 to tn-1 (range of tracks) as a text
        canvas.create_line(46,n,54,n, fill="blue", tags="line")
        canvas.create_line(n,546,n,554, fill="blue", tags="line")
        canvas.create_text(35,n,text=int(tot_seek-i*(tot_seek/5)) )
        if(i==0):
            continue
        canvas.create_text(n,565,text=t)
        
    track=500/tn
    total_time=550-abs(first_track-li[0])*time*(500/tot_seek) 
    first_track*=track
    canvas.create_line(first_track+50,550,li[0]*track+50,total_time, fill="blue", tags="line",width=3)
   
    for i in range(1,len(li)):
       total=total_time #end time of the previous path
       total_time=total-abs(li[i-1]-li[i])*time*(500/tot_seek) #end time of the current path
       canvas.create_line(li[i-1]*track+50,total,li[i]*track+50,total_time, fill="blue", tags="line",width=3)
       # create circles on the end of each transition
       canvas.create_oval(li[i - 1] * track + 47, total - 3, li[i - 1] * track + 53, total + 3, fill="red")
       
    #small circle at the end point
    canvas.create_oval(li[-1] * track + 47, total_time - 3, li[-1] * track + 53, total_time + 3, fill="red")
    canvas.pack()
    root.mainloop()

#************************************************************

#main gui elements
root=tk.Tk()
root.geometry("500x500")
root.title("Disk Scheduling Algorithms")

#disk requests label
req_lb=tk.Label(text="Enter the disk requests 'space-seperated'", font=("Arial",12),wraplength=200,fg="#333355")
req_lb.pack()

#disk requests Entry
req_entry=tk.Entry(root, font=("Arial",14), bg="lightgrey",fg="#112211",width=22)
req_entry.pack(pady=10)

#head position label
h_pos_lb=tk.Label(text="Enter the head position", font=("Arial",12),wraplength=200,fg="#333355")
h_pos_lb.pack()

#head position entry
h_pos_entry=tk.Entry(root, font=("Arial",14), bg="lightgrey",fg="#112211",width=15)
h_pos_entry.pack(pady=10)

#tracks count label
t_count_lb=tk.Label(text="Enter tracks count", font=("Arial",12),wraplength=200,fg="#333355")
t_count_lb.pack()

#tracks count entry
t_count_entry=tk.Entry(root, font=("Arial",14), bg="lightgrey",fg="#112211",width=15)
t_count_entry.pack(pady=10)

#algorithms selection menu
sel_algorithm = ttk.Combobox(root, values=options,width=25,font=("Arial",12))
sel_algorithm.pack(pady=10)
sel_algorithm.set("-- choose the algorithm --")
sel_algorithm.bind("<<ComboboxSelected>>", on_select)

#direction selection menu
dir_sel = ttk.Combobox(root, values=directions ,width=25,font=("Arial",12))
dir_sel.pack(pady=10)
dir_sel.set("-- choose the direction --")
dir_sel.bind("<<ComboboxSelected>>",Dir_Sel)

#show button to display the graph selected 
btn=tk.Button(root, text="   SHOW   ", command=on_click)
btn.pack(pady=10)

root.mainloop()




