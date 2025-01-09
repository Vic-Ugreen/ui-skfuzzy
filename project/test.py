from project.main import run_fuzzy_logic

def test_fuzzy_logic():
    assert run_fuzzy_logic(15) > 50  # Перевірка, що при низькій температурі опалення високе
    assert run_fuzzy_logic(35) < 50  # Перевірка, що при високій температурі опалення низьке
