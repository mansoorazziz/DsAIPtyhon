# Chat System using OOP

class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f"{self.sender}: {self.content}"


class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(f"{user} joined {self.name}")

    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user} left {self.name}")

    def send_message(self, user, content):
        if user in self.users:
            message = Message(user, content)
            self.messages.append(message)
            print(message)
        else:
            print(f"{user} is not in the chat room!")

    def view_history(self):
        print(f"\nChat history in {self.name}:")
        for msg in self.messages:
            print(msg)


# Example usage
if __name__ == "__main__":
    # Create chat room
    room = ChatRoom("Python Learners")

    # Create users
    u1 = User("Mansoor Aziz")
    u2 = User("Maria Mansoor")

    # Users join the room
    room.join(u1)
    room.join(u2)

    # Sending messages
    room.send_message(u1, "Hello everyone!")
    room.send_message(u2, "Hi Mansoor, welcome!")

    # View chat history
    room.view_history()

    # User leaves
    room.leave(u1)
