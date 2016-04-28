n = int(input("Enter Total Process : ")) 
wait_time=0
turnaround_time=0
remain=n
count=0
at=[];bt=[];rt=[]
while count<n: 
    at.append(int(input("Enter Arrival Time : "))) 
    bt.append(int(input("Enter Burst Time : "))) 
    rt.append(bt[count]) 
    count+=1 
time_quantum = int(input("Enter Time Quantum: "))
print ("\n\nProcess\t|Turnaround Time|Waiting Time\n\n"); 
time=0;count=0;
while remain!=0: 
    if rt[count]<=time_quantum and rt[count]>0: 
      time+=rt[count] 
      rt[count]=0 
      flag=1
    elif rt[count]>0: 
      rt[count]-=time_quantum
      time+=time_quantum 
    if rt[count]==0 and flag==1: 
      remain-=1 
      print ("P",count+1,"\t|\t",time-at[count],"\t|\t",time-at[count]-bt[count],"\n") 
      wait_time+=time-at[count]-bt[count] 
      turnaround_time+=time-at[count] 
      flag=0 
    if count==n-1: 
      count=0; 
    elif at[count+1]<=time: 
      count+=1 
    else: 
      count=0; 
print ("Average Waiting Time= ",wait_time*1.0/n)
print ("Avg Turnaround Time = ",turnaround_time*1.0/n) 
  
