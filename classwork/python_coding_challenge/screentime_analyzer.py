#screen time data
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 
#Average screen time
print("Average Screen time:", sum(screen_time)/len(screen_time))
#highest screen time
print("Highest Screen time:",max(screen_time))
#Lowest screen time 
print("Lowest Screen time:",min(screen_time))


count = 0
for time in screen_time:
    if time > 200:
        count += 1

# Display healthy usage days (<180)
healthy_days = []
for i in range(len(screen_time)):
    if screen_time[i] < 180:
        healthy_days.append("Day " + str(i + 1))

# 5. Categorize usage
healthy = 0
moderate = 0
excessive = 0

for time in screen_time:
    if time < 180:
        healthy += 1
    elif time <= 240:
        moderate += 1
    else:
        excessive += 1
print("Days Exceeding 200 Minutes:", count)

print("Healthy Usage Days:")
for day in healthy_days:
    print(day)

print("Healthy:", healthy)
print("Moderate:", moderate)
print("Excessive:", excessive)

