import time
import random
myarray=[]
myarray.append(random.randint(0,9999))
start=time.perf_counter()
sum=0
for i in myarray:
    sum=sum+i
print(sum)
end=time.perf_counter()
print("time taken:",(end-start))
