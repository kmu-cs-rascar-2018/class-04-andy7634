#########################################################################
# Date: 2018/08/09
# file name: GPIO_PWM_Buzzer_Song_Example.py
# Purpose: this code has been generated for contorl Buzzer Module
# if program is run then Buzzer make music "school bell is ringing"
#########################################################################

# coding=utf-8
"""
Buzzer 를 제어하기 위해 RPi.GPIO 모듈을 GPIO로 import 합니다.
sleep 함수를 사용하기 위해서 time 모듈을 import 합니다.
"""
import time
import RPi.GPIO as GPIO

# Raspberry Pi의 buzzer_pin을 8번으로 사용합니다.
buzzer_pin = 8

# BCM GPIO 핀 번호를 사용하도록 설정합니다.
GPIO.setmode(GPIO.BOARD)

"""
음계별 표준 주파수
[ 도, 레, 미, 파, 솔, 라 시, 도]
"""
# scale = [261.6, 293.6, 329.6, 349.2, 391.9, 440.0, 493.8, 523.2]

notes = {"E2": 82.4, "F2": 87.3, "F#2": 92.4, "G2": 97.9, "G#2": 103.82, "A2": 110.0, "A#2": 116.5, "B2": 123.4,
         "C3": 130.8, "C#3": 138.5, "D3": 146.8, "D#3": 155.5, "E3": 164.8, "F3": 174.6,
         "F3#": 184.9, "G3": 195.9, "G#3": 207.6, "A3": 220.0, "A#3": 233.0, "B3": 246.9, "C4": 261.6, "C#4": 277.1,
         "D4": 293.6, "D#4": 311.1, "E4": 329.6, "F4": 349.2, "F#4": 369.9, "G4": 391.9, "G#4": 415.3, "A4": 440.0,
         "A#4": 466.1, "B4": 493.8, "C5": 523.2, "C#5": 554.3, "D5": 587.3, "D#5": 622.2, "E5": 659.2, "F5": 698.4,
         "F#5": 739.9, "G5": 783.9, "G#5": 830.6, "A5": 880.0, "A#5": 932.3, "B5": 987.7, "G6": 1567.9, "rest": 0.1}

"""
buzzer_pin 을 GPIO 출력으로 설정합니다. 이를 통해 led_pin으로
True 혹은 False를 쓸 수 있게 됩니다.
"""
GPIO.setup(buzzer_pin, GPIO.OUT)

BPM = 4

# Song Array
# list = [4, 4, 5, 5, 4, 4, 2, 4, 4, 2, 2, 1, 4, 4, 5, 5, 4, 4, 2, 4, 2, 1, 2, 0]


# 엘리제를 위하여
# 미 레# 미 레# 미 시 레 도 라 (16분쉼표)
# 도 미 라 시 (16분쉼표)
elise1_notes = [notes["E4"], notes["D#4"], notes["E4"], notes["D#4"], notes["E4"], notes["B3"], notes["D4"],
                notes["C4"], notes["A3"], notes["rest"], notes["C3"], notes["E3"], notes["A3"], notes["B3"],
                notes["rest"]]
elise1_beats = [1 / 16, 1 / 16, 1 / 16, 1 / 16, 1 / 16, 1 / 16, 1 / 16, 1 / 16, 1 / 8, 1 / 16, 1 / 16, 1 / 16, 1 / 16,
                1 / 8, 1 / 16]

elise2_notes = [notes["E3"], notes["G#3"], notes["B3"], notes["C4"], notes["rest"]]
elise2_beats = [1 / 16, 1 / 16, 1 / 16, 1 / 8, 1 / 16]

elise3_notes = elise1_notes
elise3_beats = elise1_beats

elise4_notes = [notes["E3"], notes["C4"], notes["B3"], notes["A3"], notes["rest"]]
elise4_beats = [1 / 16, 1 / 16, 1 / 16, 1 / 8, 1 / 8]

# 카트라이더 우승
# 결승: 라라시도 레레도시미 (쉼표) 미미 미도#라 (쉼표) 미도#라 (쉼표) 미 (쉼표) 라라라라
cart_rider_win_notes = [notes["A4"], notes["A4"], notes["B4"], notes["C5"], notes["D5"], notes["D5"], notes["C5"],
                        notes["B4"], notes["E5"], notes["rest"],
                        notes["E5"], notes["E5"], notes["rest"],
                        notes["E5"], notes["C#5"], notes["A4"], notes["rest"],
                        notes["E5"], notes["C#5"], notes["A4"], notes["rest"],
                        notes["E5"], notes["rest"],
                        notes["A5"], notes["A5"], notes["A5"], notes["A5"]]

cart_rider_win_beats = [0.4, 0.4, 0.15, 0.2, 0.4, 0.4, 0.15, 0.2, 0.75, 0.01,
                        0.5, 0.5, 0.01,
                        0.33, 0.22, 0.2, 0.01,
                        0.33, 0.22, 0.2, 0.01,
                        0.5, 0.1,
                        0.21, 0.13, 0.21, 0.13
                        ]

# 카트라이더 BGB1
# 도도솔 솔파미파파 도
cart_rider_bgm1_notes = [notes["C4"], notes["C4"], notes["G4"], notes["G4"], notes["F4"], notes["E4"], notes["F4"],
                         notes["F4"], notes["C5"]]
cart_rider_bgm1_beats = [0.26, 0.15, 0.6, 0.15, 0.15, 0.15, 0.28, 0.15, 0.6]

# 카트라이더 카운트다운
# B4(G2) B4(G2) B4(G2) G5(G6)
# 시4(솔2) 시(솔) 시(솔) 솔5(솔6)
cart_rider_countdown_notes_part1 = [notes["B4"], notes["B4"], notes["B4"], notes["G5"]]
cart_rider_countdown_notes_part2 = [notes["G2"], notes["G2"], notes["G2"], notes["G6"]]

cart_rider_countdown_beats = [0.67, 0.67, 0.67, 0.3]

# 전방 감지기
# G#5
# 솔#5
obstacle_sound_notes = [notes["G#5"], notes["rest"]]

# 위험 소리
# A#2
# 라#2
danger_sound_notes = [notes["A#2"]]

try:
    p = GPIO.PWM(buzzer_pin, 100)
    p.start(4)  # start the PWM on 5% duty cycle

    # for i in range(len(list)):
    #     print(i + 1)
    #     p.ChangeFrequency(scale[list[i]])
    #     if i == 6 or i == 11 or i == 18 or i == 23:
    #         time.sleep(0.6)
    #     else:
    #         time.sleep(0.3)

    print()
    print("엘리제를 위하여 시작!!")
    print("elise1")
    for i in range(len(elise1_notes)):
        p.ChangeFrequency(elise1_notes[i])
        time.sleep(BPM * elise1_beats[i])
        print(i, "번째 음 출력했음.")

    print("elise2")
    for i in range(len(elise2_notes)):
        p.ChangeFrequency(elise2_notes[i])
        time.sleep(BPM * elise2_beats[i])
        print(i, "번째 음 출력했음.")

    print("elise3")
    for i in range(len(elise3_notes)):
        p.ChangeFrequency(elise3_notes[i])
        time.sleep(BPM * elise3_beats[i])
        print(i, "번째 음 출력했음.")

    print("elise4")
    for i in range(len(elise4_notes)):
        p.ChangeFrequency(elise4_notes[i])
        time.sleep(BPM * elise4_beats[i])
        print(i, "번째 음 출력했음.")

    print()
    print("카트라이더 결승 시작!!!")
    for i in range(len(cart_rider_win_notes)):
        p.ChangeFrequency(cart_rider_win_notes[i] / 2)
        time.sleep(cart_rider_win_beats[i])
        print(i, "번째 음 출력했음.")

    print()
    print("카트라이더 bgm1 시작!!")
    for i in range(len(cart_rider_bgm1_notes)):
        p.ChangeFrequency(cart_rider_bgm1_notes[i])
        time.sleep(cart_rider_bgm1_beats[i])
        print(i, "번째 음 출력했음.")

    print()
    print("카트라이더 카운트다운 시작!!")
    for i in range(len(cart_rider_countdown_notes_part1)):
        p.ChangeFrequency(cart_rider_countdown_notes_part1[i])
        time.sleep(cart_rider_countdown_beats[i])
        print(i, "번째 1파트 음 출력했음.")

    for i in range(len(cart_rider_countdown_notes_part2)):
        p.ChangeFrequency(cart_rider_countdown_notes_part2[i])
        time.sleep(cart_rider_countdown_beats[i])
        print(i, "번째 2파트 음 출력했음.")

    print()
    print("위험 알림 시작!!")
    p.ChangeFrequency(danger_sound_notes[0])
    time.sleep(1)

    p.stop()  # stop the PWM output
    print()
    print("종료!!")

    # ======================================
    # 전방 감지기 실행소스 추가
    # =====================================

    distance = 10  # 이 값은 초음파 센서에서 거리 측정값 받아오셈
    DISTANCE_SOUND_BPM = 0.01  # 상수값 적절하게 조정하셈
    while distance > 5 and distance < 30:
        print("주의!! 전방 장애물과의 거리:", distance, "cm")

        # 5cm ~ 10cm 사이에서는 경보음 연속으로 계속 울림 (rest 없음)
        while distance < 10:
            p.ChangeFrequency(obstacle_sound_notes[0])
            time.sleep(0.3)
            distance = 10  # 이 값은 초음파 센서에서 거리 측정값 받아오셈

        # 거리에 비례해서 rest길이 조정
        else:
            p.ChangeFrequency(obstacle_sound_notes[0])
            time.sleep(0.3)
            p.ChangeFrequency(obstacle_sound_notes[1])
            time.sleep(distance * DISTANCE_SOUND_BPM)
            distance = 10  # 이 값은 초음파 센서에서 거리 측정값 받아오셈



finally:
    GPIO.cleanup()
