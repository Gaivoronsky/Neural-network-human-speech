import speech_recognition as sr


print("Привет, поговори со мной")

def record_recognition():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Говорите")
		audio = r.listen(source)

	try:
		text = r.recognize_google(audio, language="ru-RU").lower()
		print("Вы сказали: " + text)

	except sr.UnknownValueError:
		print("Я вас не поняла")
		text = record_recognition()

	write_to_file(text)


def write_to_file(text):
	with open("pred.txt", "w") as file:
		file.write(str(text) + ' ')