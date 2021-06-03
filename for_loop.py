

numbers = [6,5,3,8,4,2,5,4,11]
sum = 0
for val in numbers:
   sum = sum + val
print(" The sum is ", sum)

print(range(10))
print(list(range(10)))
print(list(range(2,8)))
print(list(range(2,20,3)))
print("###########################")
genre = ['pop','rock','jazz']
for i in range(len(genre)):
    print("I like ",genre[i])
print("###########################")
digits = [0,1,5]
for i in digits:
    print(i)
else:
    print("No items left.")    
print("########################")
student_name = 'Bla'
marks = { 'James':90,'Jules':55,'Arthur':77 }
for student in marks:
    if student == student_name:
        print(marks[student])
        break
  #  print(student) # printira imenat
  #  print(marks[student]) #printira 4islata
  #  break
else:
    print('No entry with that name found.')


