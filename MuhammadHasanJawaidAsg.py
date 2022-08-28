# quote = "Nelson Mandela once said 'The greatest glory in living lies not in never falling, but in rising every time we fall'"
# print(quote)

# radius = input()
# area = (int(radius))* (int(radius)) * 3.142 
# print(area)

# number = input()
# num = int(number)
# if num < 0 :
#   print("number is negative")
# else:
#     print("number is positive")
    
# char = input()
# if char == 'a' or char == 'e' or char == 'i'or char == 'o'or char == 'u':
#   print("character is a vowel")
# else:
    # print("character is not a vowel")

# Height = input("Enter your height: ")
# height = int(Height)
# Weight = input("Enter your weight: ")
# weight = int(Weight)

# height = height/10

# print((weight)/(height*height))


# names = ["ahmed", "saim", "zaid", "uzair", "aarij", "ali"]

# for name in names:
#   print(name)

dishes = ["pasta", "pizza", "burger", "sandwich", "noodles", "roll", "biryani","handi", "karahi"]
print("Three items from the middle of list are: ")
# x= slice(3, 6)
# print(dishes[x])
# print("Three items from the beginning of list are: ")
# x= slice(0, 3)
# print(dishes[x])
# print("Three items from the end of list are: ")
# x= slice(6, 9)
# print(dishes[x])

friends_dishes = dishes.copy()

dishes.append("Qorma")
friends_dishes.append("Pulao")

print("My favorite dishes are: ")
for dish in dishes:
  print(dish)

print("My Friends favorite dishes are: ")
for friend_dish in friends_dishes:
  print(friend_dish)  
  
if dishes == friends_dishes:
  print("They both are same")
else:
  print("both are different")
  
  