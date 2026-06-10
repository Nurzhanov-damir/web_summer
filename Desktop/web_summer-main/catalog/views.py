from django.shortcuts import render

def index(request):
    books = [
        {'title': 'Norwegian Wood', 'author': 'Haruki Murakami', 'year': 1987, 'rating': 4, 'cover': 'https://i.pinimg.com/236x/b9/2a/59/b92a59fe53813d5d9b20a22a4ddbd7a2.jpg?nii=t'},
        {'title': 'Kafka on the Shore', 'author': 'Haruki Murakami', 'year': 2002, 'rating': 5, 'cover': 'https://ir.ozone.ru/s3/multimedia-1-e/9361659290.jpg'},
        {'title': 'The Sound of Waves', 'author': 'Yukio Mishima', 'year': 1954, 'rating': 4, 'cover': 'https://m.media-amazon.com/images/I/81T5nut042L.jpg'},
    ]
    return render(request, 'catalog/index.html', {'books': books})