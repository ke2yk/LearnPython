import winsound
import time
import os

os.system('clear')

# Morse code dictionary
morse_code = {
'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
' ': '/'
}

def text_to_morse(text):
	morse = ""
	for char in text.upper():
		if char in morse_code:
			morse += morse_code[char] + " "
		else:
			morse += char + " "

	return morse.strip()

def play_morse_code(morse):
	for symbol in morse.split():
		time.sleep(0.5) # Pause between letter
		for char in symbol:
			if char == '.':
				winsound.Beep(1000, 300) # Beep for dot
				#time.sleep(0.4) # Pause between letter
			elif char == '-':
				winsound.Beep(1000, 600) # Beep for dash
				#time.sleep(0.2) # Pause between symbols
				#time.sleep(0.4) # Pause between letters

user_input = input("Enter text to convert to Morse code: ")
morse_output = text_to_morse(user_input)
print(f"Morse code: {morse_output}")

play_morse_code(morse_output)
#Morse Code Translator

