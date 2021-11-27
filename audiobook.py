import PyPDF2

pdf = PyPDF2.PdfFileReader(open('file.pdf',  'rb'))

import pyttsx3 

fala = pyttsx3.init()


for page_num in range(pdf.numPages):
    text = pdf.getPage(page_num).extractText()
    fala.say(text)
    fala.runAndWait()

fala.stop()

fala.save_to_file(text, 'audio.mp3')
fala.runAndWait()