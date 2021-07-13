import os
import sys

print("""
███████╗██╗███╗░░██╗██████╗░░██████╗███╗░░░███╗
██╔════╝██║████╗░██║██╔══██╗██╔════╝████╗░████║
█████╗░░██║██╔██╗██║██║░░██║╚█████╗░██╔████╔██║
██╔══╝░░██║██║╚████║██║░░██║░╚═══██╗██║╚██╔╝██║
██║░░░░░██║██║░╚███║██████╔╝██████╔╝██║░╚═╝░██║
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚═════╝░╚═╝░░░░░╚═╝""")
print("\n\n\n")
print("Developed By: ")
def names_installed():
    try:
        import names
    except:
        print("Names module is missing")
        sys.exit()
    
    print("NOTE: MANY SOCIALMEDIA ACCOUNTS 'FIND' MAY SEARCH MAY NOT BE AVAILAIBLE")
    print('Please fill in the following info:')
    print("")
    #----------------------------------#
    print('What gender do you want to search:')
    print('[1] : Male')
    print('[2] : Female')
    print('[3] : Any')
    print("")
    print('[00] : Exit')
    user_gender = input("Gender> ")
    print("")
    #----------------------------------#
    print('Full name or Half name:')
    print('[1] : Full')
    print('[2] : Half')
    print("")
    print('[00] : Exit')
    FoH = input("Name Length> ")
    print("")
    #----------------------------------#
    print('How many accounts do you want us to generate: ')
    amount = input("How Many [Enter in numbers]>")
    print("")
    #----------------------------------#
    print('Social Media:')
    print('[1] : Instagram')
    print('[2] : FaceBook')
    print('[3] : Twitter')
    print('[4] : Youtube Channel')
    print('[5] : Google Search')
    print('[6] : Famous Birthdays')
    print('[7] : Pinterest')
    print("")
    print('[00] : Exit')
    SM = input("Name Length> ")
    print("")

    for i in range(int(amount)):
        if FoH == '1':
            if user_gender == '1':
                random_name = names.get_full_name(gender='male')
            elif user_gender == '2':
                random_name = names.get_full_name(gender='female')
            elif user_gender == '3':
                random_name = names.get_full_name()
            elif user_gender == '00':
                sys.exit()
        elif FoH == '2':
            if user_gender == '1':
                random_name = names.get_first_name(gender='male')
            elif user_gender == '2':
                random_name = names.get_first_name(gender='female')
            elif user_gender == '3':
                random_name = names.get_first_name()
            elif user_gender == '00':
                sys.exit()
        elif FoH == '00':
            sys.exit() 
        if SM == '1':
            print("https://www.instagram.com/"+random_name.replace(' ', '_'))
        elif SM == '2':
            print("https://www.facebook.com/"+random_name.replace(' ', '.'))
        elif SM == '3':
            print("https://www.twitter.com/"+random_name.replace(' ', ''))
        elif SM == '4':
            print("https://www.youtube.com/c/"+random_name.replace(' ', ''))
        elif SM == '5':
            print("https://www.google.com/search?q="+random_name.replace(' ', '%20'))
        elif SM == '6':
            print("https://www.famousbirthdays.com/people/"+random_name.replace(' ', '-')+".html")
        elif SM == '7':
            print("https://in.pinterest.com/"+random_name.replace(' ', '')+"/_created/")


is_names_there= input("Do you have names module in python already installed?[y/n] ")
if is_names_there == 'y':
    names_installed()
else:
    os.system('pip3 install names')
    names_installed()
