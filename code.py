import board
import audiobusio
import digitalio
import audiomp3
import time
import busio
import pwmio
from adafruit_motor import servo
import adafruit_hcsr04
meeting = False

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP4, echo_pin=board.GP3)

servo_a_pin = pwmio.PWMOut(board.GP5, frequency=50)
servo_a = servo.Servo(servo_a_pin, min_pulse=1000, max_pulse=2000)
audio_out = audiobusio.I2SOut(board.GP1, board.GP0, board.GP2)

# Function to play MP3 audio from a file
def play_audio(file_path):
    with open(file_path, "rb") as f:
        mp3_decoder = audiomp3.MP3Decoder(f)
        audio_out.play(mp3_decoder)
        while audio_out.playing:
            time.sleep(0.1)

while True:
    dist = sonar.distance/100
    if (dist <= 15):
        meeting = True
    else:
        meeting = False
    if meeting == True:
        play_audio("demo.mp3")
        servo_a.angle = 90
    else:
        servo_a.angle = 0
