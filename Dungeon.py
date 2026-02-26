# Treassure Hunt
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
import time
import random as rd
import pygame
import climage
from pygame import mixer

pygame.mixer.init()
mixer.music.load("background.mp3")
mixer.music.play(-1)
print("Welcome to this dungeon of madness")
import colorama
from colorama import Fore, Style


def screen(image_path=None, width=90):
    os.system("cls")
    if image_path:
        print(climage.convert(image_path, width=width, is_unicode=True))
        print()

def beffect(dial: str,audio,speed:float=1.0):
   leng=dial
   aud=audio
   delay=aud.get_length()/len(leng)
   aud.play()
   for x in dial:
       print(Fore.CYAN + x,end="",flush=True)
       time.sleep(delay)
   print()

def meffect(dial: str, audio, speed: float = 1.0):
    delay = audio.get_length() / len(dial)
    audio.play()
    for x in dial:
        print(Fore.YELLOW + x, end="", flush=True)
        time.sleep(delay)
    print()
def yeffect(dial: str, audio, speed: float = 1.0):
    delay = audio.get_length() / len(dial)
    audio.play()
    for x in dial:
        print(Fore.MAGENTA + x, end="", flush=True)
        time.sleep(delay)
    print()

def feffect(dial: str,audio,speed:float=1.0):
   leng=dial
   aud=audio
   delay=aud.get_length()/len(leng)
   aud.play()
   for x in dial:
       print(Fore.GREEN + x,end="",flush=True)
       time.sleep(delay)
   print()

def beffect(dial: str,audio,speed:float=1.0):
   leng=dial
   aud=audio
   delay=aud.get_length()/len(leng)
   aud.play()
   for x in dial:
       print(Fore.CYAN + x,end="",flush=True)
       time.sleep(delay)
   print()

def effect(dial: str, audio, speed: float = 1.0):
    leng = dial
    aud = audio
    delay = aud.get_length() / len(leng)
    aud.play()
    for x in dial:
        print(Fore.RED + x, end="", flush=True)
        time.sleep(delay)
    print()


def Shadows(user):
    screen("shadow.png")
    mixer.music.load("shadows.mp3")
    mixer.music.play(-1)

    yeffect(
        "You step beyond the last ray of light. 🌑\n"
        "The air grows heavy, as if the darkness itself is watching.\n"
        "Your shadow stretches unnaturally, moving when you do not. 👤🖤\n"
        "A whisper coils around your thoughts:\n"
        "“Every hero carries a shadow… but not all survive meeting it.”\n\n",
        mixer.Sound("sd1.mp3")
    )

    print(f"""{Fore.WHITE}
        ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
        ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
        ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
        ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
        ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
        ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝
    """)

    yeffect(
        "Three paths reveal themselves:\n\n"
        "1️⃣ Follow the whispering voices 🗣️🌫️\n"
        "2️⃣ Walk into the hall of mirrors 🪞👁️\n"
        "3️⃣ Descend into absolute darkness 🕳️⬇️\n"
        "4️⃣ Turn back while you still can cause some truths are better not to seek reflection of light 🏃‍♂️💨\n\n",
        mixer.Sound("sd2.mp3")
    )
    print(f"{Fore.RED}{user} {Fore.YELLOW}Choose how you face the shadows:")
    choice = int(input())
    print()
    if choice == 1:
        yeffect(
            "You follow the whispering voices 🗣️🌫️.\n"
            "They begin as guidance, then twist into accusation.\n"
            "Every regret you buried claws its way back.\n"
            "The voices grow louder until thought itself shatters.\n\n"
            "The shadows feast on your mind.\n"
            "You fade screaming into the dark. ☠️🖤\n",
            mixer.Sound("sd3.mp3")

        )
        loss()

    elif choice == 2:
        yeffect(
            "You step into the hall of mirrors 🪞👁️.\n"
            "Reflections multiply, yet one remains still.\n"
            "It does not judge. It waits.\n\n"
            "You feel the shadows hesitate.\n"
            "This path… continues.\n\n",
            mixer.Sound("sd4.mp3")
        )
        yeffect(
            "You move deeper into the hall of mirrors 🪞.\n"
            "The reflections stop copying you.\n"
            "They watch.\n\n"
            "A voice echoes:\n"
            "“How will you face yourself?”\n\n",
            mixer.Sound("sd7.mp3")
        )

        yeffect(
            "1️⃣ Challenge the strongest reflection ⚔️\n"
            "2️⃣ Shatter every mirror 💥🪞\n"
            "3️⃣ Kneel and beg for mercy 🙇‍♂️\n"
            "4️⃣ Turn away and walk forward 🚶‍♂️🌑\n\n",
            mixer.Sound("sd8.mp3")
        )
        print(f"{Fore.RED} {user} Time to descide your fate otherwise shadows will....")
        final_choice = int(input())
        print()


        if final_choice == 1:
            yeffect(
                "You attack ⚔️.\n"
                "The reflection moves faster.\n\n"
                "One strike.\n"
                "Darkness.\n\n"
                "You cannot defeat yourself by force. ☠️🪞\n",
                mixer.Sound("sd9.mp3")
            )
            loss()


        elif final_choice == 2:
            yeffect(
                "Mirrors shatter 💥.\n"
                "Shadows spill out.\n\n"
                "Rage turns on its master.\n\n"
                "The hall collapses. ☠️🌑\n",
                mixer.Sound("sd10.mp3")
            )
            loss()


        elif final_choice == 3:
            yeffect(
                "You kneel 🙇‍♂️.\n"
                "The reflections smile.\n\n"
                "Mercy is never offered here.\n\n"
                "Your voice fades. ☠️🖤\n",
                mixer.Sound("sd11.mp3")
            )
            loss()


        elif final_choice == 4:
            yeffect(
                "You turn away 🚶‍♂️.\n"
                "The mirrors scream behind you.\n\n"
                "You do not fight.\n"
                "You do not flee.\n\n"
                "The hall dissolves.\n\n"
                "An obsidian chest waits 🖤.\n"
                "Inside: the Shadow Relic 💎.\n\n"
                "The shadows bow.\n"
                "You move on. 🗝️👑\n",
                mixer.Sound("sd12.mp3")
            )
            treasure(user)

        else:
            print("⚠️ Invalid choice. Hesitation seals your fate. ☠️")
            loss()



    elif choice == 3:
        yeffect(
            "You descend into absolute darkness 🕳️⬇️.\n"
            "There is no floor. No sound. No end.\n"
            "The darkness does not attack — it erases.\n\n"
            "You vanish without echo or memory.\n"
            "Even the shadows forget you. ☠️🌑\n",
            mixer.Sound("sd5.mp3")
        )
        loss()

    elif choice == 4:
        yeffect(
            "You turn back 🏃‍♂️💨.\n"
            "The light behind you fractures, reflecting endlessly.\n"
            "You realize too late:\n"
            "To flee the shadow, you must still face the light.\n\n"
            "Caught between both, you are torn apart.\n"
            "Neither side claims you. ☠️🌓\n",
            mixer.Sound("sd6.mp3")
        )
        loss()

    else:
        print("⚠️ Invalid choice. Hesitation seals your fate. ☠️")
        loss()
    mixer.music.stop()

def Hills(user):
    screen('hill.png')
    mixer.music.load("hills.mp3")
    mixer.music.play(-1)
    beffect("The hero chooses the path of the hills. 🌄\nThe climb is steep, the fog thick, and the air carries strange echoes that distort every sound.\nSuddenly, the hero stumbles upon a circle of jagged stones ⛰️.\nAt the center lies a weathered staff ⚔️, half-buried in the earth.\nThe staff hums faintly when touched, resonating with the stone circle.\nThe whispers rise:\nThe hills test those who command their voice… choose wisely, or be swallowed by silence.\n",mixer.Sound("hd1.mp3"))
    print(fr"""{Fore.GREEN}
      /\
     /**\
    /****\   /\      /\    /\ 
   /      \ /**\    /**\  /**\
  /  /\    /    \  /    \/    \
 /__/__\__/______\/____________\
""")
    beffect("1) Pull the staff free with brute force. 💪🪨\n2) Strike the stones with the staff, testing their reaction. ⚔️✨\n3) Place the staff upright in the center of the circle. 🪄⛰️\n4) Ignore the staff and continue climbing. 🚶‍♂️🌫️\n",mixer.Sound("hd2.mp3"))
    print(f"{Fore.RED}{user} {Fore.CYAN}Your decision will descide your fate")
    choi=int(input())
    print("\n")
    if choi == 1:
        beffect("❌ You pull the staff with brute force 💪🪨. The earth groans, the staff snaps ⚔️💥, and a rockslide buries the circle. \nPoetically, the hills whisper your last breath... you died. ☠️⛰️",mixer.Sound("hd3.mp3"))
        loss()
    elif choi == 2:
        beffect("❌ You strike the stones ⚔️✨. The runes flare too brightly ⚡, a deafening echo disorients you, and you stumble into the ravine. \nThe echoes sing your fall... you died. ☠️🌫️",mixer.Sound("hd4.mp3"))
        loss()
    elif choi == 3:
        beffect("✅ You place the staff upright in the circle 🪄⛰️. The stones vibrate 🎶, the echoes align, and the ground splits open. 🌍✨\nFrom the earth rises a bronze medallion 🥇, glowing with destiny. The hills bow to your courage, revealing the path below. 🌑🗝️",mixer.Sound("hd6.mp3"))
        beffect("The hero lifts the bronze medal from the earth. 🥇🌍\nOn its surface, engraved in ancient script, are the words:The treasure awaits. ✨📜\nAs the medal glows faintly, the ground rumbles. 🌌⚡⛰️\nA hidden passage opens, leading into a cavern carved deep beneath the hills. 🕳️🌄🌫️\nInside, the hero finds a massive stone gate ⛰️🚪, sealed by three interlocking mechanisms. 🔒⚙️⚙️⚙️\nEach mechanism hums faintly, echoing the unpredictable rhythm of the hills. 🎶🌬️🪨\nThe whispers return, resonating through the cavern walls: 🌀👤\nOnly one path aligns with truth. Choose wrongly, and the hills will consume you. 🌬️🗝️☠️\n",mixer.Sound("hd7.mp3"))
        beffect("1)Force the gate open with brute strength 💪⛰️🪨⚡☠️\n2)Place the bronze medal into the central mechanism 🥇⚙️✨🚪🌟\n3)Strike the mechanisms with the staff to disrupt them ⚔️💥🎶🌀☠️\n4)Wait silently, hoping the gate opens on its own ⏳🌫️👤🪨☠️\n",mixer.Sound("hd8.mp3"))
        print(f"{Fore.RED} {user} Time to decide which option will lead us to treasure\n")
        choi1=int(input())
        if choi1 == 1:
            beffect("❌ You force the gate with brute strength 💪⛰️. The stone resists, then collapses in fury ⚡🪨. The hills roar, burying you beneath their weight. 🌄☠️\nPoetically, the echoes sing your last breath... you died. 🌀💀",mixer.Sound("hd9.mp3"))
            loss()
        elif choi1 == 2:
            beffect("✅ You place the bronze medal into the central mechanism 🥇⚙️✨. The gears align 🎶⚡, the gate rumbles open 🚪🌌, and golden light floods the cavern. 🌟🏆\nThe treasure of the hills awaits you, earned by truth and courage. 🌄🗝️💎",mixer.Sound("hd10.mp3"))
            treasure(user)
        elif choi1 == 3:
            beffect("❌ You strike the mechanisms with the staff ⚔️💥. The rhythm shatters 🎶🌀, a deafening echo consumes the cavern 🌫️⚡. The shadows rise and silence your voice forever. 👤☠️\nThe hills remember your fall... you died. 💀🌄",mixer.Sound("hd11.mp3"))
            loss()
        elif choi1 == 4:
            beffect("❌ You wait silently ⏳🌫️. The gate does not open 🚪❌. Instead, the walls close in 🪨⚡, crushing hope and breath alike. 🌌☠️\nThe hills consume your silence... you died. 🌀💀",mixer.Sound("hd12.mp3"))
            loss()
        else:
            print("⚠️ Invalid choice. Greed blinds you 🌑🌀, and the hills consume your soul. ☠️⛰️")
            loss()
    elif choi == 4:
        beffect("❌ You ignore the staff 🚶‍♂️🌫️. The fog thickens, the path vanishes, and you wander endlessly. \nThe hills consume your soul... you died. ☠️🌀",mixer.Sound("hd5.mp3"))
        loss()
    else:
        print("⚠️ Invalid choice. Your greed blinds you, and the hills consume you. 🌄🌀☠️")
        loss()
    mixer.music.stop()
    print()


def loss(speed: float = 0.6):
    screen("death.png")
    mixer.music.load("dead.mp3")
    mixer.music.play(-1)

    audio = mixer.Sound("loss.mp3")
    audio.play()
    ascii_art = f"""
{Fore.RED}
        █████████
       ███░░░░░███
      ███   ☠   ███
       ███░░░░░███
        █████████
    """
    print(ascii_art)

    message = "A hero died trying... Play again, brave soul. Treasure beholds for no one but the one who earns it"
    delay = (audio.get_length() / len(message)) * speed
    for char in message:
        print(Fore.RED + char, end="", flush=True)
        time.sleep(delay)
    time.sleep(2)
    torch_frames = [
        Fore.YELLOW + "   🔥 ",
        Fore.RED + "   🔥 ",
        Fore.LIGHTRED_EX + "   🔥 "
    ]
    for i in range(10):
        print(torch_frames[i % len(torch_frames)], end="\r")
        time.sleep(0.2)
    print(f"\n{Fore.YELLOW}Designed & Developed by Shivam Joshi")
    time.sleep(5)
    mixer.music.fadeout(20000)


def Forest(user):
    screen("forrest.png")
    mixer.music.load("fbgm.mp3")
    pygame.mixer.music.set_volume(0.5)
    mixer.music.play(-1)
    horror = mixer.Sound("feefect2.mp3")
    horror.play()
    print("Welcome to the Forest")
    feffect(
        "🌲🌳🌲🌳🌲\nThe FOREST looms before you...\nIts towering trees blot out the sky, and the air hums with whispers carried by the wind.\nFireflies flicker like fallen stars, but their glow only deepens the shadows.\nEvery step feels watched... every rustle hides intent. The forest is alive.\nIt does not welcome you. It tests you. It deceives you. And only those who endure its trials may claim its secret treasure...\n",
        mixer.Sound("fintro.mp3"))
    print(fr"""{Fore.GREEN}
      /\
     /**\
    /****\   /\      /\    /\ 
   /      \ /**\    /**\  /**\
  /  /\    /    \  /    \/    \
 /__/__\__/______\/____________\
""")
    feffect(
        "as you pushes deeper into the forest. The Marshall light flickers, and suddenly the beam catches something strange: an ancient lantern hanging from a crooked branch. It glows faintly, though no flame burns inside. As the hero approaches, the forest itself seems to hold its breath.\nA  whisper rises from the mist \nOnly one action will awaken the path. Choose wrong, and the forest will consume you.\n1. Light the ancient lantern with the Marshall beam—it might awaken its glow.\n2. Smash the lantern to break the forest’s illusion.\n3. Step past the lantern, ignoring it, and continue forward.\n4. Place the lantern on the ground and listen—it hums faintly, as if alive.\n",
        mixer.Sound("fd1.mp3"))
    print(f"{Fore.RED} {user} Time to make your decision\n")
    dec = int(input())
    if dec == 1:
        feffect("💨 The lantern erupts in smoke... your lungs collapse, vision fades... ☠️ You are dead.\n",
                mixer.Sound("fd2.mp3"))
        loss()
    elif dec == 2:
        feffect(
            "💥 The lantern shatters... shards crawl like insects 🐛, burrowing into your flesh. Screams echo... ☠️ You are dead.\n",
            mixer.Sound("fd3.mp3"))
        loss()
    elif dec == 3:
        feffect(
            "🌲 You step past... the forest closes in, branches snap shut 🕸️. Darkness devours you whole... ☠️ You are dead.\n",
            mixer.Sound("fd4.mp3"))
        loss()
    elif dec == 4:
        feffect(
            "✅ You place the lantern down 🌍... it hums 🎶 with the forest’s heartbeat 💓. Roots glow 🌱, revealing a hidden trail 🌌!",
            mixer.Sound("fd5.mp3"))
        feffect(
            "As you follows the glowing trail revealed by the lantern 🏮.\nThe mist thins, and suddenly the forest opens into a hidden grove 🌳✨.\nAt its center lies a stone pedestal, cracked and ancient, with a faint golden shimmer radiating from beneath it 💎.\nThe whispers return, but now they sound playful, almost mocking:\nTreasure awaits if you dare to choose.🗝️\n",
            mixer.Sound("fd6.mp3"))
        feffect(
            "As you sets the lantern on the moss. 🏮\nIt hums once, brightens, and a thin beam slides along the ground to a low stone slab. ✨\nThe slab lifts like a lid and beneath it is a shallow hollow with a small iron ring fixed in the earth. 🪨🔩\nThe lantern’s light warms the ring as if recognizing it. 🔥\n",
            mixer.Sound("fd7.mp3"))
        feffect(
            "1️⃣ Pull the iron ring with your hands. 🪝🤚\n2️⃣ Use the Marshall light 🔦 to heat the ring. 🔥\n3️⃣ Place the lantern on the ring and let it rest. 🏮➡️🔩\n4️⃣ Ignore the ring and dig beside the slab. ⛏️🕳️\n",
            mixer.Sound("fd8.mp3"))
        print(f"{Fore.RED}{user}Time to make a choice\n")
        dec1 = int(input())
        if dec1 == 1:
            feffect(
                "❌ You yank the ring with brute force — the earth snaps shut like a jaw. Roots coil around you; the light dies. ☠️",
                mixer.Sound("fd9.mp3"))
            loss()
        elif dec1 == 2:
            feffect(
                "✅ You train the Marshall light 🔦 on the iron ring. The metal warms, clicks free, and the hollow opens with a golden sigh. 🧰🗝️\n✨ Inside: a brass key and a folded map — the first piece of treasure. The path forward glows. 🌿➡️🌟",
                mixer.Sound("fd00.mp3"))
            horror.stop()
            mixer.music.stop()
            treasure(user)
        elif dec1 == 3:
            feffect(
                "❌ You set the lantern on the ring. Its hum binds to the iron and the lantern fuses to the earth — the hollow seals and the light is lost. ☠️🏮🔒",
                mixer.Sound("fd10.mp3"))
            loss()
        elif dec1 == 4:
            feffect(
                "❌ You start digging beside the slab. The ground caves in; the chest is crushed beneath falling stone. Dust swallows the grove. ☠️🕳️",
                mixer.Sound("fd11.mp3"))
            loss()
        else:
            print("⚠️ Invalid choice. Forest consume your greed and you")
            loss()

    else:
        print("⚠️ Invalid choice Youre consumed by the forest.\n")
        loss()

    horror.stop()
    mixer.music.stop()


def Cave(user):
    screen("cave pic.png")
    mixer.music.load("cave.mp3")
    pygame.mixer.music.set_volume(0.2)
    mixer.music.play(-1)
    cin = mixer.Sound("in_cave.mp3")
    d6 = "You step into the cave. The air is damp, and water drips steadily from the ceiling. Shadows flicker against the walls. A faint scratching sound echoes deeper inside…"
    del6 = cin.get_length() / len(d6)
    cin.play()
    for i in "You step into the cave. The air is damp, and water drips steadily from the ceiling. Shadows flicker against the walls. A faint scratching sound echoes deeper inside…":
        print(Fore.RED + i, end="", flush=True)
        time.sleep(del6)

    print(fr"""
  {Fore.MAGENTA}
        ________
      /         \
     |    CAVE   |
      \_________/
        ~  ~  ~
    """)
    print(f"Aight {Fore.RED}{user}.....")
    dial7 = mixer.Sound("caved2.mp3")
    d7 = "🔥 As you entered the cave...\n🕯️ The torch flickers… then dies. 🌑 Darkness swallows everything.\n👂 Suddenly, you hear something strange — a faint sound 💧, a shifting shadow 👤, a cold draft 🌬️.\n⚡ Your instincts scream: choose quickly, or perish… 💀\n\n"
    length = dial7.get_length() / len(d7)
    dial7.play()
    for i in d7:
        print(Fore.RED + i, end="", flush=True)
        time.sleep(length - 0.)
    time.sleep(1)
    bear = mixer.Sound("bear.mp3")
    bear.play()
    dial8 = "Make your choice:\n1) Follow the faint dripping water 💧\n2) Chase the shifting shadow 👤\n3) Step into the cold draft 🌬️\n4) Stand still and wait ⏳\nEnter 1, 2, 3, or 4: \n"
    del8 = mixer.Sound("cavechoice.mp3")
    len8 = del8.get_length() / len(dial8)
    del8.play()
    for i in dial8:
        print(Fore.RED + i, end="", flush=True)
        time.sleep(len8)

    survive = int(input(

    ))
    if survive == 1:

        effect(
            "💧 You move toward the faint dripping sound...The darkness parts, revealing a glowing underground pool. You survived this choice!\n GOOD CHOICE blud!!!You swim through the cold, glowing water. The pool feels endless, but finally, your hands touch a rocky edge\nAs you pull yourself up, the chamber is silent… yet something stirs. Four paths reveal themselves along the pool’s edge.\nChoose wisely — only one leads to safety, the others to doom…"
            , mixer.Sound("survive1.mp3"), speed=0.6)
        print(f"{Fore.RED}Think Quick {Fore.CYAN}{user}")
        effect(
            "1) Follow the glowing crystal 💎\n2) Step onto the mossy ledge 🌿\n3) Climb toward the dripping waterfall 💧\n4) Enter the shadowed archway 🌓\nChoose carefully !!! (1,2,3,4)\n",
            mixer.Sound("cavesur2.mp3"), speed=0.6)
        survive2 = int(input())
        mixer.music.stop()
        if survive2 == 2:
            effect(
                "🌿 You step onto the mossy ledge...The moss is slick! You slip back into the pool, dragged under by unseen currents. 💀",
                mixer.Sound("loss2.mp3"), speed=0.8)
            loss()
        elif survive2 == 1:
            effect(
                "💎 You follow the glowing crystals...The crystals crumble, releasing toxic fumes. You collapse, choking in the darkness. 💀",
                mixer.Sound("sur2.mp3"), speed=0.8)
            loss()

        elif survive2 == 3:
            effect(
                "💧 You climb toward the waterfall...The water roars as you push through the curtain. Behind it, a secret passage glows faintly. You survived and found the way forward! 🎉",
                mixer.Sound("surw.mp3"), speed=0.8)
            treasure(user)

        elif survive2 == 4:
            effect(
                "🌑 You enter the shadowed archway...A beast lurks within. It lunges, claws flashing. You fall to the ground, defeated. 💀 \n",
                mixer.Sound("survw2.mp3"), speed=0.8)
            loss()
        else:
            print("Invalid choice. The cave consumes you in silence... 💀")
            loss()


    elif survive == 2:
        effect(
            "👤 You chase the shifting shadow...Suddenly, claws tear through the silence. The beast lunges — you are slain. 💀",
            mixer.Sound("sur3.mp3"), speed=0.8)
        loss()
    elif survive == 3:
        effect(
            "🌬️ You step into the cold draft...The ground vanishes beneath you — it was a chasm! You plunge into endless darkness. 💀",
            mixer.Sound("sur4.mp3"), speed=0.8)
        loss()
    elif survive == 4:
        effect(
            "⏳ You decide to stand still, waiting in silence...The cave trembles... rocks collapse from above. You are buried alive. 💀",
            mixer.Sound("sur5.mp3"), speed=0.8)
        loss()
    else:
        print("Invalid choice. The cave consumes you anyway... 💀")
        loss()
    mixer.music.stop()



print(climage.convert("cave pic.png", is_unicode=True))
print()
input("Press Enter to start...")


def begin():
    intro = mixer.Sound("intro.mp3")
    length = intro.get_length()
    intro.play()
    i1 = "Welcome to this Dungeon of Madness!!! Here you have to survive and find "
    i2 = " and conquer the "
    del1 = length / len(i1)
    for i in i1:
        print(Fore.RED + i, end="", flush=True)
        time.sleep(del1 - 0.03)
    print(f"{Fore.YELLOW}Treasure", end="", flush=True)
    for j in i2:
        print(Fore.RED + j, end="", flush=True)
        time.sleep(del1 - 0.03)
    print(f"{Fore.RED}Quest!!!", end="", flush=True)
    print("\n")
    user = input("What should I call you? : ")
    greet = mixer.Sound("greet.mp3")
    d2 = " lets start this journey together ill guide you. Do you see that Ancient gate?!!!"
    del2 = greet.get_length() / len(d2)
    greet.play()

    print(f"Welcome {Fore.RED}{user}", end="", flush=True)
    for i in " lets start this journey together ill guide you. Do you see that Ancient gate?!!!":
        print(Fore.RED + i, end="", flush=True)
        time.sleep(del2)
    time.sleep(1.2)
    print()

    print(fr"""{Fore.RED}
      ┌─────────────────────────┐
      │     ANCIENT GATE        │
      └─────────────────────────┘
             _________
            |         |
            |   ___   |
            |  |   |  |
            |  |   |  |
            |__|___|__|
    """)
    d3 = f"So {user} you want to enter the gate? And find what your destiny beholds for you? (Yes or No) :"
    choose = mixer.Sound("choice.mp3")
    del3 = choose.get_length() / len(d3)
    choose.play()
    print(f"So {Fore.RED}{user}", end="", flush=True)
    for x in " you want to enter the gate? And find what your destiny beholds for you? (Y/N) :":
        print(Fore.RED + x, end="", flush=True)
        time.sleep(del3 - 0.03)
    print()

    choice = input().lower()
    if (choice == 'y'):
        d4 = "Which Path should we follow? "
        path = mixer.Sound("path.mp3")
        del3 = path.get_length() / len(d4)
        path.play()
        for x in "Which Path should we follow? ":
            print(Fore.RED + x, end="", flush=True)
            time.sleep(del3 - 0.02)
        time.sleep(1)
        print()

        print(fr"""{Fore.RED}
                            🌲🌳🌲🌳🌲
                                FOREST
                                  ↑
                                  |
                         CAVE <───|───> HILL ⛰️🌄🦅
                        🕳️🪨🦇
                                  ↓
                               SHADOWS
                               🌑👤👻



              """)
        d5 = "Enter the level you want to enter "
        way = mixer.Sound("way.mp3")
        del5 = way.get_length() / len(d5)
        way.play()
        for x in d5:
            print(Fore.RED + x, end="", flush=True)
            time.sleep(0.13)
        print(
            f"\n{Fore.RED}For {Fore.GREEN}Forest {Fore.RED}enter 1\n{Fore.RED}For {Fore.MAGENTA}Cave {Fore.RED}enter 2\n{Fore.RED}For {Fore.CYAN}Shadows {Fore.RED}enter 3\n{Fore.RED}For the {Fore.BLUE}Hills {Fore.RED}enter 4")
        rounds = int(input("\n"))
        mixer.music.stop()
        if (rounds == 1):
            print("You have entered the Forest")
            name1= Forest(user)
        elif (rounds == 2):
            print("You have entered the CAVE")
            name = Cave(user)
        elif (rounds == 3):
            print("You have entered the SHADOWS")
            name2=Shadows(user)
        elif (rounds == 4):
            print("You have entered the HILLS")
            name3=Hills(user)
        else:
            print("Invalid choice")

    elif (choice == 'n'):
        pass
    else:
        print("Invalid choice. Try Again")
    return user


def treasure(user):
    screen("treasure.png")
    mixer.music.load("treasures.mp3")
    mixer.music.play(-1)
    meffect(
        "✨ You’ve survived countless trials and done a fantastic job so far! ✨\nBut in the distance, you see a mysterious glow... 🌌\nA glasglow glowing chamber shimmers ahead, its walls pulsing with strange light. 💡🏰\n\nAt the center lies a massive stone chest bound in iron ⛓️📦.\nAs you approach, glowing runes ignite upon the lid 🔮✨.\nA chilling voice whispers through the chamber:\n🧩Answer me, and the treasure is yours... 🎁\n💀 Fail... and perish.⚡",
        mixer.Sound("tres1.mp3"), speed=0.8)
    time.sleep(0.8)
    print(fr"""{Fore.YELLOW}
        ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
        ┌─────────────────────────┐
        │     GLOWING CHEST 🔮    │
        └─────────────────────────┘
              _________
             /        /|
            /________/ |
            |        | |
            |  👑💎 | /
            |________|/

        ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
  """)
    time.sleep(1)
    meffect(
        "🧩🌌 The chamber hushes as a magical voice whispers...\n 👺 🎶🌫️🧩I answer when you call, yet I never move; I repeat what you say but change nothing; I live where sound can bounce. 🎶\n\nI know you have 0 clue — let me clue you in.\nA) 🔊 Echo\nB) 👤 Shadow\nC) 🗺️ Map\nD) 🤫 Whisper\n\nYour answer (The word): ",
        mixer.Sound('rid.mp3'), speed=0.6)
    riddle = input().lower()

    if riddle == 'echo':
        w = mixer.Sound("door.mp3")
        meffect(
            "✨ The runes blaze white as your answer rings true...\n🔊 Echo— the chamber hums in approval. The iron clasps on the chest unwind with a metallic sigh.\n📦 The lid creaks open, spilling a warm golden light across the floor.\n👑 Inside: a crown encrusted with rubies, strings of pearls, and coins that sing when they touch each other.\n🎉 Congratulations! You solved the riddle and claimed the treasure. Your name will be sung by bards. ✨",
            mixer.Sound("win.mp3"), speed=1.2)
        w.play()

        print(f"\n{Fore.RED}You won {Fore.YELLOW}{user}")
        print(fr"""{Fore.YELLOW}
                ✨✨✨ TREASURE REVEALED ✨✨✨
                    _______________________
                  /                      /|
                 /______________________/ |
                | 👑  💎  💰  💎  👑 |  |
                |                       | /
                |______________________|/
                ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
        """)
        screen("done.png")
        print("I'll see you on the other side\n\n")
        print(f"{Fore.RED}Designed & Developed by Shivam Joshi")
        time.sleep(7)
    else:
        print("The answer to the riddle was wrong. The cave consumes your greed and you're DEAD!!!")
        loss()

    mixer.music.stop()


def main():
    begin()


if __name__ == "__main__":
    main()
    mixer.music.stop()



