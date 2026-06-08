from django.shortcuts import render
 
def index(request):
    books = [
        {'title': 'Norwegian Wood', 'author': 'Haruki Murakami', 'year': 1987, 'rating': '4/5'},
        {'title': 'Kafka on the Shore', 'author': 'Haruki Murakami', 'year': 2002, 'rating': '5/5'},
        {'title': 'The Sound of Waves', 'author': 'Yukio Mishima', 'year': 1954, 'rating': '4.5/5'},
    ]
    return render(request, 'catalog/index.html', {'books': books})