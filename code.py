import board
import audiobusio
import digitalio
import audiomp3
import time
import busio
import time
import wifi
import adafruit_requests as requests
from adafruit_ntp import NTP

# Wi-Fi credentials
SSID = "Mahir"
PASSWORD = "Ahnaf767"

# Connect to Wi-Fi
print("Connecting to Wi-Fi...")
wifi.radio.connect(SSID, PASSWORD)
print("Connected to Wi-Fi!")

# Create a socket pool and requests session
pool = wifi.radio
requests = requests.Session(pool)

# Connect to the NTP server
print("Connecting to NTP server...")
ntp = NTP(pool, server="pool.ntp.org", tz_offset=0)

# Fetch and print the current time
current_time = ntp.datetime
print("Current time:", current_time)

# Convert to local time if needed (example for UTC+2)
local_time = time.localtime(time.mktime(current_time) + 6 * 3600)
print("Local time (UTC+6):", local_time)



audio_out = audiobusio.I2SOut(board.GP0, board.GP1, board.GP2)

# Function to play MP3 audio from a file
def play_audio(file_path):
    with open(file_path, "rb") as f:
        mp3_decoder = audiomp3.MP3Decoder(f)
        audio_out.play(mp3_decoder)
        while audio_out.playing:
            time.sleep(0.1)

# Main loop to play the louder MP3 file
while True:
    play_audio("demo.mp3")
    time.sleep(1)


