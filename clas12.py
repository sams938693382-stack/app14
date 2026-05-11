class Instagram:
    def __init__(self, login, like):
        self.login = login
        self.like = like

    def add_like(self, son):
        self.like += son
        print(f"❤️ {son} ta like qoshildi")

    def info(self):
        print(f"📸 Login: @{self.login}")
        print(f"👍 Like: {self.like}")


acc = Instagram("shox_edit", 1200)

acc.add_like(300)
acc.add_like(700)

acc.info()