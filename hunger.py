import time
from datetime import datetime, timedelta

class Hunger:
    def __init__(self):
        self.hunger_lvl = 100
        self.days_not_fed = 0
        self.last_fed = datetime.now()
        self.alive = True

    def feed(self):
        self.last_fed = datetime.now()
        self.hunger_lvl = min(100, self.hunger_lvl + 14)
        self.days_not_fed = 0

    def update_hunger(self):
        if self.last_fed <= datetime.now() - timedelta(minutes=0.25):
            self.days_not_fed += 1
        
        if self.days_not_fed != 0:
            self.hunger_lvl = max(0, 100 - self.days_not_fed*14)

    def is_alive(self):
        if self.hunger_lvl == 0:
            print("Your pet has died of hunger.\nGame Over")
            self.alive = False
            return self.alive
        return self.alive


tamagotchi1 = Hunger()

def study_session(tamagotchi):
    input("Press Enter to start a study session")
    start = time.time()
    input("Press Enter to end the study session")
    end = time.time()

    duration = (end - start) / 60
    if duration < 30:
        print("You did not study long enough to feed your tamagotchi.")
    else:
        tamagotchi1.feed()
        print(f"You studied for {int(duration)} minutes. Your tamagotchi has been fed.")

while tamagotchi1.alive:
    tamagotchi1.update_hunger()
    if tamagotchi1.is_alive() == False:
        break
    
    choice = input("Do you want to study and feed your tamagotchi today? (y/n): ")
    if choice.lower() == 'y':
        study_session(tamagotchi1)
    
    print(f"Current hunger level: {tamagotchi1.hunger_lvl}")
    print(f"Days not fed: {tamagotchi1.days_not_fed}")
    
    time.sleep(15)




        



