
for i in range(1,11):
    print (i)


scores = [95, 70, 85, 60, 100]

#95점 : 합격
#70점 : 불합격
#85점 : 합격
#60점 : 불합격
#100점 : 합격

for score in scores:
    if score >= 80:
     print(f"{score}점이면 합격")
    else:
     print(f"{score}점이면 불합격")