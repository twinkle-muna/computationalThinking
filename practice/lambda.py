student = [("허준녕", 20153253, 4.2),("김영재", 20153180, 3.7),("한채연", 20153250, 4.5),]
print("Before sorted :", student)
idsort = sorted(student, key = lambda x : x[1])
print("Sort by id :", idsort)
gradesort = sorted(student, key = lambda x : x[2], reverse=True)
print("Sort by grade :", gradesort)