class User:

    def __init__(self,user_id,usernmae):
        self.id = user_id
        self.usernmae = usernmae
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("001","angle")
user_2 = User("002", "jack")

user_1.follow(user_1)
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(f"user_2.followers: {user_2.followers}")
print(f"user_2.followers: {user_2.following}")

# print(user_2.followers)
# print(user_2.following)