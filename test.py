import pytest
import pygame
from asdgsgd import show_text, death_screen, title_screen, main_game

pygame.init()
screen = pygame.display.set_mode((800, 600))

def test_show_text_runs_without_error():
    try:
        show_text("Test Message", 32, 100, 100)
    except Exception as e:
        pytest.fail(f"show_text raised an exception: {e}")

def test_title_screen_exists():
    assert callable(title_screen), "title_screen function is not defined"

def test_death_screen_exists():
    assert callable(death_screen), "death_screen function is not defined"

def test_main_game_exists():
    assert callable(main_game), "main_game function is not defined"

@pytest.mark.skip(reason="main_game runs an infinite loop for gameplay")
def test_main_game_runs():
    try:
        main_game()
    except Exception as e:
        pytest.fail(f"main_game raised an exception: {e}")

pytest.main(["-v", "--tb=line", "-rN", __file__])
