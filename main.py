from person import Person

human = Person(name='Эна', hp=100, mood=80, money=50)

print(human)
human.change_state()
print(human)

if human.hp <= 0:
    print("Эна умерла")
    print("")
    breakpoint()
elif human.mood <= 0:
    print("У Эны депрессия")
    print("")
    breakpoint()
elif human.money <= 0:
    print("Эна обанкротилась")
    print("")

human.go_to_work()
if human.mood < 20:
    human.money = human.money - human.money * 0.2
elif human.hp < 30:
    human.money = human.money - human.money * 0.2
print("Эна пошла на работу")
print(human)


if human.hp < 50:
    human.go_to_hospital()
    if human.money < 20:
        human.hp = human.hp - human.hp * 0.5
    print("Эна пошла в больницу")
    print(human)

if human.mood > 20:
    human.go_to_park()
    if human.money < 20:
        human.mood = human.mood - human.mood * 0.8
    print("Эна пошла погулять в парк")
    print(human)

