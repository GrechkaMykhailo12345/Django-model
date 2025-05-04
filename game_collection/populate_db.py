import sys
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "game_collection.settings")
django.setup()

from catalog.models import Genre, Game

# Створення жанрів
genre_action = Genre.objects.create(name="Action")
genre_rpg = Genre.objects.create(name="RPG")
genre_strategy = Genre.objects.create(name="Strategy")
genre_puzzle = Genre.objects.create(name="Puzzle")

print("Створено жанри:", Genre.objects.all())

# Створення ігор
game1 = Game.objects.create(title="Counter-Strike 2", release_year=2023, rating=9.5)
game1.genres.add(genre_action)
game1.genres.add(genre_rpg)

game2 = Game.objects.create(title="Half-Life 2", release_year=2004, rating=9.0)
game2.genres.add(genre_rpg)
game2.genres.add(genre_strategy)

game3 = Game.objects.create(title="Portal 2", release_year=2011, rating=9.7)
game3.genres.add(genre_puzzle)

print("Створено ігри:", Game.objects.all())
for game in Game.objects.all():
    print(f"{game.title}: {', '.join(g.name for g in game.genres.all())}")