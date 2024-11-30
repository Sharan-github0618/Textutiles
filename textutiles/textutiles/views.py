from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def remove(request):
    # Get input text and options
    text = request.POST.get('text', 'default')
    check = request.POST.get('check', 'off')
    extraspace = request.POST.get('extraspaceremove', 'off')
    upper = request.POST.get('uppercase', 'off')
    count = request.POST.get('charcount', 'off')
    remove_newline = request.POST.get('removenewline', 'off')

    # Initialize Analyzed_text
    Analyzed_text = text  # Start with the original text

    # Remove punctuations
    if check == 'on':
        punctuations = '''!@#$%^&*())_-=+'''
        Analyzed_text = ''.join(char for char in Analyzed_text if char not in punctuations)

    # Remove extra spaces
    if extraspace == 'on':
        temp_text = ''
        for index, char in enumerate(Analyzed_text):
            # Ensure not to go out of bounds
            if index < len(Analyzed_text) - 1:
                if char != ' ' or Analyzed_text[index + 1] != ' ':
                    temp_text += char
            else:
                # Always add the last character
                temp_text += char
        Analyzed_text = temp_text

    # Convert to uppercase
    if upper == 'on':
        Analyzed_text = Analyzed_text.upper()

    # Remove new lines
    if remove_newline == 'on':
        Analyzed_text = ''.join(char for char in Analyzed_text if char not in ('\n', '\r'))

    # Count characters (optional)
    char_count = len(Analyzed_text) if count == 'on' else None

    # Prepare context for the template
    params = {
        'text': Analyzed_text,
        'count_value': char_count,
    }

    # Render the response
    return render(request, 'analyze.html', params)
