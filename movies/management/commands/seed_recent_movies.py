from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from movies.models import Genre, Language, Movie, Theater, Seat


class Command(BaseCommand):
    help = 'Seed recent movies with theaters and seats'

    def handle(self, *args, **options):
        language_codes = {
            'Hindi': 'hi',
            'Telugu': 'te',
            'English': 'en',
        }
        movies_data = [
            (
                'Pushpa 2: The Rule',
                'movies/635217f73e372771013edb4c-the-avengers-poster-marvel-movie-canvas1.jpg',
                8.4,
                'Allu Arjun, Rashmika Mandanna',
                'Action drama sequel',
                'https://www.youtube.com/watch?v=g3JUbgOHgdw',
                ['Action', 'Drama'],
                ['Hindi', 'Telugu'],
            ),
            (
                'Devara Part 1',
                'movies/feUv2SYumXlT8E2RhzlYbZxfEGLG5AVrCPxP1gmAaCusxyPnA1.jpg',
                7.8,
                'NTR Jr, Janhvi Kapoor',
                'Coastal action drama',
                'https://www.youtube.com/watch?v=rc61YHl1PFY',
                ['Action', 'Drama'],
                ['Telugu', 'Hindi'],
            ),
            (
                'Kalki 2898 AD',
                'movies/f5VK0h2bprRhR6iRrixcuEfRxSUF4l14F66vQYrsJGmKZ5nTA1.jpg',
                8.2,
                'Prabhas, Deepika Padukone',
                'Sci-fi action spectacle',
                'https://www.youtube.com/watch?v=y1-w1kUGuz8',
                ['Sci-Fi', 'Action'],
                ['Hindi', 'Telugu'],
            ),
            (
                'Stree 2',
                'movies/IQsBhg9t747dLhjXfsChIGZy4XfugER8BF0Gw5MDhIcnY5nTA1.jpg',
                8.1,
                'Rajkummar Rao, Shraddha Kapoor',
                'Horror comedy sequel',
                'https://www.youtube.com/watch?v=KVnheXywIbY',
                ['Horror', 'Comedy'],
                ['Hindi'],
            ),
            (
                'Fighter',
                'movies/download.jpeg',
                7.5,
                'Hrithik Roshan, Deepika Padukone',
                'Aerial action entertainer',
                'https://www.youtube.com/watch?v=6amIq_mP4xM',
                ['Action', 'Thriller'],
                ['Hindi'],
            ),
            (
                'Avengers',
                'movies/download.jpeg',
                8.0,
                'Robert Downey Jr., Chris Evans',
                'Superhero team-up blockbuster',
                'https://www.youtube.com/watch?v=eOrNdBpGMv8',
                ['Action', 'Sci-Fi'],
                ['English'],
            ),
            (
                'Avengers: Endgame',
                'movies/download.jpeg',
                8.4,
                'Robert Downey Jr., Chris Evans',
                'Epic conclusion to the saga',
                'https://www.youtube.com/watch?v=TcMBFSGVi1c',
                ['Action', 'Sci-Fi'],
                ['English'],
            ),
            (
                'Inception',
                'movies/download.jpeg',
                8.8,
                'Leonardo DiCaprio, Joseph Gordon-Levitt',
                'Mind-bending heist thriller',
                'https://www.youtube.com/watch?v=YoHD9XEInc0',
                ['Sci-Fi', 'Thriller'],
                ['English'],
            ),
            (
                'Interstellar',
                'movies/download.jpeg',
                8.6,
                'Matthew McConaughey, Anne Hathaway',
                'Space exploration drama',
                'https://www.youtube.com/watch?v=zSWdZVtXT7E',
                ['Sci-Fi', 'Drama'],
                ['English'],
            ),
            (
                'Joker',
                'movies/download.jpeg',
                8.5,
                'Joaquin Phoenix, Robert De Niro',
                'Psychological character study',
                'https://www.youtube.com/watch?v=zAGVQLHvwOY',
                ['Drama', 'Thriller'],
                ['English'],
            ),
            (
                'Spider-Man',
                'movies/download.jpeg',
                7.9,
                'Tom Holland, Zendaya',
                'Superhero coming-of-age',
                'https://www.youtube.com/watch?v=JfVOs4VSpmA',
                ['Action', 'Sci-Fi'],
                ['English'],
            ),
            (
                'Oppenheimer',
                'movies/download.jpeg',
                8.6,
                'Cillian Murphy, Emily Blunt',
                'Biographical drama',
                'https://www.youtube.com/watch?v=uYPbbksJxIg',
                ['Drama', 'Thriller'],
                ['English'],
            ),
            (
                'Dune',
                'movies/download.jpeg',
                8.0,
                'Timothee Chalamet, Zendaya',
                'Epic sci-fi saga',
                'https://www.youtube.com/watch?v=n9xhJrPXop4',
                ['Sci-Fi', 'Adventure'],
                ['English'],
            ),
            (
                'The Dark Knight',
                'movies/download.jpeg',
                9.0,
                'Christian Bale, Heath Ledger',
                'Iconic superhero thriller',
                'https://www.youtube.com/watch?v=EXeTwQWrcwY',
                ['Action', 'Thriller'],
                ['English'],
            ),
            (
                'Titanic',
                'movies/download.jpeg',
                7.9,
                'Leonardo DiCaprio, Kate Winslet',
                'Epic romance',
                'https://www.youtube.com/watch?v=kVrqfYjkTdQ',
                ['Drama', 'Romance'],
                ['English'],
            ),
            (
                'Avatar',
                'movies/download.jpeg',
                7.8,
                'Sam Worthington, Zoe Saldana',
                'Sci-fi adventure',
                'https://www.youtube.com/watch?v=5PSNL1qE6VY',
                ['Sci-Fi', 'Adventure'],
                ['English'],
            ),
            (
                'Bahubali: The Beginning',
                'movies/download.jpeg',
                8.0,
                'Prabhas, Rana Daggubati',
                'Epic action drama',
                'https://www.youtube.com/watch?v=sOEg_YZQsTI',
                ['Action', 'Drama'],
                ['Telugu', 'Hindi'],
            ),
            (
                'Bahubali 2: The Conclusion',
                'movies/download.jpeg',
                8.2,
                'Prabhas, Anushka Shetty',
                'Epic conclusion',
                'https://www.youtube.com/watch?v=G62HrubdD6o',
                ['Action', 'Drama'],
                ['Telugu', 'Hindi'],
            ),
            (
                'RRR',
                'movies/download.jpeg',
                8.0,
                'NTR Jr, Ram Charan',
                'Action drama spectacle',
                'https://www.youtube.com/watch?v=NgBoMJy386M',
                ['Action', 'Drama'],
                ['Telugu', 'Hindi'],
            ),
            (
                'KGF: Chapter 1',
                'movies/download.jpeg',
                8.2,
                'Yash, Srinidhi Shetty',
                'Action crime drama',
                'https://www.youtube.com/watch?v=-KfsY-qwBS0',
                ['Action', 'Thriller'],
                ['Hindi'],
            ),
            (
                'KGF: Chapter 2',
                'movies/download.jpeg',
                8.3,
                'Yash, Sanjay Dutt',
                'Sequel action drama',
                'https://www.youtube.com/watch?v=Qah9sSIXJqk',
                ['Action', 'Thriller'],
                ['Hindi'],
            ),
        ]

        created_movies = 0
        for idx, (name, image, rating, cast, description, trailer_url, genres, languages) in enumerate(movies_data, start=1):
            movie, created = Movie.objects.get_or_create(
                name=name,
                defaults={
                    'image': image,
                    'rating': rating,
                    'cast': cast,
                    'description': description,
                    'trailer_url': trailer_url,
                },
            )
            if not created:
                movie.image = image
                movie.rating = rating
                movie.cast = cast
                movie.description = description
                movie.trailer_url = trailer_url
                movie.save(update_fields=['image', 'rating', 'cast', 'description', 'trailer_url'])
            else:
                created_movies += 1

            genre_objs = []
            for genre_name in genres:
                genre_obj, _ = Genre.objects.get_or_create(
                    name=genre_name,
                    defaults={'slug': genre_name.lower().replace(' ', '-')},
                )
                genre_objs.append(genre_obj)
            movie.genres.set(genre_objs)

            language_objs = []
            for language_name in languages:
                language_obj, _ = Language.objects.get_or_create(
                    name=language_name,
                    defaults={'code': language_codes.get(language_name, language_name[:2].lower())},
                )
                language_objs.append(language_obj)
            movie.languages.set(language_objs)

            theater, _ = Theater.objects.get_or_create(
                name=f'PVR Screen {idx}',
                movie=movie,
                defaults={'show_time': timezone.now() + timedelta(hours=idx * 2)},
            )

            for seat_no in range(1, 41):
                Seat.objects.get_or_create(theater=theater, seat_number=f'A{seat_no}')
        trailer_backfill = {
            'Avengers': 'https://www.youtube.com/watch?v=eOrNdBpGMv8',
            'Avengers: Endgame': 'https://www.youtube.com/watch?v=TcMBFSGVi1c',
            'Inception': 'https://www.youtube.com/watch?v=YoHD9XEInc0',
            'Interstellar': 'https://www.youtube.com/watch?v=zSWdZVtXT7E',
            'Joker': 'https://www.youtube.com/watch?v=zAGVQLHvwOY',
            'Spider-Man': 'https://www.youtube.com/watch?v=JfVOs4VSpmA',
        }
        for movie_name, trailer_url in trailer_backfill.items():
            Movie.objects.filter(name=movie_name).update(trailer_url=trailer_url)
        self.stdout.write(self.style.SUCCESS(f'Recent movies seeded. Created new movies: {created_movies}'))

