from django.apps import AppConfig 

class MoviesConfig(AppConfig):
    name = 'movies'
    description = ''
    image = """movies/img.jpg"""
    image_caption = 'Proyecto'
    body = """Tries to find the movie you are describing."""