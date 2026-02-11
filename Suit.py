# Suitn vs Komputer
import time
import random
print('PERTANDINGAN SUIT KITA VS COM')
print('-'*20)
def pertandingan_suit():
    mulai_suit = 0
    Menang = 0
    Kalah = 0
    Seri = 0
    Pilihan = ['✂️', '📃', '🪨'] # Pilihan
    while mulai_suit < 3:
        Kita = str(input('Suit kamu: ')).capitalize() # Suit kita
        if Kita not in Pilihan:
            print('Error, diluar pilihan')
            continue
        komputer = random.choice(Pilihan)
        print('KOMPUTER SEDANG MEMILIH TUNGGU SEBENTAR')
        time.sleep(3)
        print(f'Pilihan komputer: {komputer}') # Pilihan komputer
        if Kita == komputer:
            print('Seri😬')
            Seri +=1
        elif (Kita == '✂️' and komputer == '📃') or \
        (Kita == '📃' and komputer == '🪨') or \
        (Kita == '🪨' and komputer == '✂️'):
            Menang +=1
            print('Kamu menang😊')
        else:
            Kalah +=1
            print('Kamu kalah😔')
        mulai_suit +=1
        print(f'Ronde mulai suit {mulai_suit}')

        if Menang == 2:
            print('Selamat kamu Menang')
            break
    while Menang == Seri or Menang > Kalah or Kalah < Seri:
        Kita = str(input('Suit kamu: ')).capitalize() # Suit kita
        if Kita not in Pilihan:
            print('Error, diluar pilihan')
            continue
        komputer = random.choice(Pilihan)
        print('KOMPUTER SEDANG MEMILIH TUNGGU SEBENTAR')
        time.sleep(3)
        print(f'Pilihan komputer: {komputer}') # Pilihan komputer
        if Kita == komputer:
            print('Seri😬')
            Seri +=1
        elif (Kita == '✂️' and komputer == '🪨') or \
        (Kita == '🪨' and komputer == '✂️') or \
        (Kita == '🪨' and komputer == '🪨'):
            Menang +=1
            print('Kamu menang😊')
        else:
            Kalah +=1
            print('Kamu kalah😔')
        mulai_suit +=1
        print(f'Ronde mulai suit {mulai_suit}')
        
    print(f'\nHASIL PERTANDINGAN SUIT KAMU')
    print('-'*30)
    print(f'Menang {Menang}')    
    print(f'Kalah {Kalah}')    
    print(f'Seri {Seri}')
    print(f'Permainan berlangsung {mulai_suit} kali')
    print('-'*30)
    if Menang >= 2:
        print('Kamu menang dalam pertandingan ini')
    else:
        print('Kamu kalah dalam pertandingan ini')    
pertandingan_suit()