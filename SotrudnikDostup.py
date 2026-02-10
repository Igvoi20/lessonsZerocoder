class User:
    def __init__(self, user_id, name):
        self._id = user_id
        self._name = name
        self._access_level = "user"

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = "admin"

    def add_user(self, users_list, user):
        users_list.append(user)

    def remove_user(self, users_list, user_id):
        for user in users_list:
            if user.get_id() == user_id:
                users_list.remove(user)
                break


users = []

admin = Admin(1, "Ivan")
user1 = User(2, "Igor")
user2 = User(3, "Alex")

admin.add_user(users, user1)
admin.add_user(users, user2)

admin.remove_user(users, 2)

print(users[0].get_name(), users[0].get_access_level())
