email = input("Enter your email address\n").strip()

user = email[:email.index("@")]
# print(user)

domain = email[email.index("@")+1:email.index(".")]

# print(domain.capitalize()," is the domain name")

print(f"{user} is the username and {domain}.com is the domain name ")