password=input("please provide your password to check if it is strong or weak ? ")
pass_len=len(password)
if pass_len >= 8 and '@' in password and " " not in password:
    print ("The password you have enter is strong")
else:
    print ("The provided password is weak")