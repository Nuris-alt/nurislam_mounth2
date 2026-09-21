class Streamer:
    def live(self):
        return "запускаю стрим! Подписывайтесь, ставьте лайки!"
    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"{self.live()} {self.superpower()}"


class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return f"{self.live()} {self.viral()} {self.superpower()}"


class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return f"{self.live()} {self.earn()} {self.viral()}"


glow = GlowStreamer()
viral = ViralCyborg()
donate = DonateMage()

print(GlowStreamer.mro())
print(ViralCyborg.mro())
print(DonateMage.mro())

print(glow.live()) #здесь отрабатывает класс GlowStreamer который объединяет в себе классы Streamer и Mutant. Сначало срабатывает класс Streamer а затем класс Mutant
print(viral.live())#здесь срабатывает класс ViralCyborg в котором есть классы Tiktoker и Mutant. Как и в первом случаи срабатывает тот класс который в порядке стоит первым
print(donate.live())#здесь же срабатывает класс DonateMage который объединяет классы Streamer и Tiktoker. Тут сначало срабатывает класс Streamer а потом класс Tiktoker

print(glow.ultimate_content())
print(viral.ultimate_content())
print(donate.ultimate_content())