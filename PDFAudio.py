import pyttsx3 #pip install pyttsx3
import PyPDF2  #pip install PyPDF2

text = open('your_pdf_name.pdf', 'rb' # Enter ypur pdf name here and make sure its in same dirctory as your program
reader = PyPDF2.PdfFileReader(text)
pages = reader.numPages #total number of pages with starting index 0

speaker = pyttsx3.init()
speaker.say("From what page should i read?? ") # from what page to read 
speaker.runAndWait()
start = int(input()) # taking input page number

for i in range((start-1), pages): # as starting index is 0 so start-1
    page = reader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
