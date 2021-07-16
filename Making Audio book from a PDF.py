# Modules Needed :

# pip install pyttsx3 # Helps to read in audio format
# pip install PyPDF2 # Helps to read Pdf files

# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
path = open('file.pdf', 'rb') #Opening file read binary mode

# creating a PdfFileReader object
pdf_Reader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdf_Reader.getPage(int(input("Enter the page to be read : ")+1)) # Getting the info from the user for reading a specfic page

# extracting the text from the PDF
text = from_page.extractText() # Inorder to skip the images everything is converted into text

# reading the text
speak = pyttsx3.init() # Initializing the reader function
speak.say(text)
speak.runAndWait()
