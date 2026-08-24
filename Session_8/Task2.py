steps = [8000, 9500, 11200, 7000, 10500]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
i=0
while i < len(steps):
    if(steps[i]>10000):
        print(f"First day over 10,000 steps: {days[i]} with {steps[i]} steps.")
        break
    i=i+1
   
# for i in range(len(steps)):
#     if(steps[i]>10000):
#         print(f"First day over 10,000 steps: {days[i]} with {steps[i]} steps.")
#         break