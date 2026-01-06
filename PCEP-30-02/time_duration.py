hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

dura_hour = int(dura / 60)
dura_mins = int(dura % 60)

print("Total duration:",dura_hour,":",dura_mins)

holder1 = int(mins + dura_mins)
holder2 = int(holder1 / 60)
holder3 = hour + dura_hour + holder2

end_hour = holder3 % 24
end_mins = int(holder1 % 60)

print(holder1,holder2,holder3)
print("End time:",end_hour,":",end_mins)