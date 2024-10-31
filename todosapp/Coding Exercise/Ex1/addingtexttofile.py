

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            member = input("Add new member: ") + "\n"

            file = open('members.txt', 'r')
            members = file.readlines()
            file.close()

            members.append(member)

            file = open('members.txt', 'w')
            file.writelines(members)
            file.close()


        case 'show':
            file = open('members.txt', 'r')
            members = file.readlines()
            file.close()

            for index, item in enumerate(members):

                print(item)

        case 'exit':
            break