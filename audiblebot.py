import pyttsx3
import PyPDF2

pdf = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
pages = pdfReader.numPages

bot = pyttsx3.init()

for num in range(10, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
	bot.say("Hello darkness my old friend")
	bot.runAndWait()
