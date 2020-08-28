class Vocabulary:
    def __init__(self, english, chinese, prof = 0):
        self.english = english
        self.chinese = chinese
        self.prof = prof

    def down(self):
        self.prof -= 1

    def up(self):
        self.prof += 1

    def __str__(self):
        return self.english

vc_bye = Vocabulary('bye','再见')
vc_bye.up()
print(str(vc_bye))
print(vc_bye.english + " -> " + vc_bye.chinese)