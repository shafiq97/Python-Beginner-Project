if __name__ == '__main__':
    email = input("Enter email: ")
    username = email[:email.find("@")]
    domain = email[email.find("@")+1:]
    print(f"username {username}")
    print(f"Domain name: {domain}")
