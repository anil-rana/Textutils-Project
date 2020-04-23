# I have created this file ---> Anil Rana
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	# params = {'name':'anil', 'place':'Mars'}
	return render(request, 'index.html')
	# return HttpResponse("Hello")



# def removepunc(request):
# 	# Get the text from the browser here...........
# 	djtext = request.GET.get('text', 'default')
# 	print(djtext)
#
# 	# Analyze the text here...............
# 	return HttpResponse("This function remove punchtuation from string.")
#
#
# def capfirst(request):
# 	return HttpResponse("This function capitalize the string.")
#
#
# def newlineremove(request):
# 	return HttpResponse("This function remove new line from the string.")
#
#
# def spaceremove(request):
# 	return HttpResponse("This function remove extra space from the string.")
#
#
# def charcount(request):
# 	return HttpResponse("This function count total character in the string.")


def analyze(request):
	# Get the text from the browser here...........
	djtext = request.POST.get('text', 'default')

	# Check checkbox value
	removepunc = request.POST.get('removepunc', 'off')
	fullcaps = request.POST.get('fullcaps', 'off')
	newlineremover = request.POST.get('newlineremover', 'off')
	extraspaceremover = request.POST.get('extraspaceremover', 'off')
	charcount = request.POST.get('charcount', 'off')

	# Check which checkbox is one.......
	if removepunc == "on":
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''

		# Remove punctuation from string.
		analyzed = ""
		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char

		params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}

		djtext = analyzed

		# Analyze the text here...............
		# return render(request, 'analyze.html', params)



	if (fullcaps == "on"):
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()

		params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

		# Analyze the text here...............
		# return render(request, 'analyze.html', params)
		djtext = analyzed


	if (newlineremover == "on"):
		analyzed = ""
		for char in djtext:
			if char != '\n' and char != '\r':
				analyzed = analyzed + char

		params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}

		# Analyze the text here...............
		# return render(request, 'analyze.html', params)
		djtext = analyzed


	if (extraspaceremover == "on"):
		analyzed = ""
		for index, char in enumerate(djtext):  # enumerate function give value with index number.
			if not(djtext[index] == " " and djtext[index + 1] == " "):
				analyzed = analyzed + char

		params = {'purpose': 'Removed Space', 'analyzed_text': analyzed}

		# Analyze the text here...............
		# return render(request, 'analyze.html', params)
		djtext = analyzed

	if (charcount == "on"):
		analyzed = len(djtext)
		params = {'purpose': 'Total Character Found', 'analyzed_text': analyzed}

		# Analyze the text here...............
	if (removepunc == "off" and fullcaps == "off" and newlineremover == "off" and extraspaceremover == "off" and charcount == "off"):
		# return HttpResponse("Please select any above operaton and try again.")
		params = {'purpose': 'Error Occured!!!', 'analyzed_text':'Please select any operaton and try again.'}

	return render(request, 'analyze.html', params)



