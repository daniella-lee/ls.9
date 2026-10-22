total_chores=4
original_count= total_chores
print(f"you have{original_count}chores to finish today!\n")

complete_count=0
cn=1

while cn<= total_chores:

    if cn==1:next_chore="make bed"
    elif cn==2:next_chore="homework"
    elif cn==3:next_chore="take out trash"
    elif cn==4:"feed the pet"

    answer = input(f"have u finished: {next_chore}? (yes/no): ")

    if answer=="yes":
        complete_count +=1
        cn +=1
        print("good! chore compleat")
    else:
        print("finish it, okay?")

    print("chores remaining", total_chores-complete_count)
    print()

print("all done!!!!")
print("good work doin the job!\n")
print("now lets look at an infinite loop")
test_value=0
safety_counter=0
while test_value <= 0:
        print("this condition never change, so this would run foreverrrr")
        safety_counter+=1
        if safety_counter==3:
            print("(stoppin here on perpose-a real infinite loop never stopes on its own)")
            break

print("\n=====chore checklist summary=====")
print("chores assigned today:",original_count)
print("chores compleated:", complete_count)
print("chores remaining:", total_chores-complete_count)
print("===================================")