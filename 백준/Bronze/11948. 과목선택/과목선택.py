subject = [] 
for _ in range(6):  
    subject.append(int(input())) 
subject1 = sorted(subject[:4]) 
subject2 = subject[4:] 
print(sum(subject1[1:]) + max(subject2))