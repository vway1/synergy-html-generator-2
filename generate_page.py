from pathlib import Path


HTML = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Университет «Синергия»</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <main>
        <h1>Университет «Синергия»</h1>

        <p>
            Автономная некоммерческая организация высшего образования
            «Московский университет «Синергия»».
        </p>

        <h2>Варианты шрифтов</h2>
        <p class="font-example synergy">Университет «Синергия»</p>
        <p class="font-example arial">Университет «Синергия»</p>
        <p class="font-example verdana">Университет «Синергия»</p>
        <p class="font-example tahoma">Университет «Синергия»</p>
        <p class="font-example georgia">Университет «Синергия»</p>
        <p class="font-example times">Университет «Синергия»</p>
    </main>
</body>
</html>
"""


def generate_page() -> None:
    """Создаёт HTML-страницу рядом с программой."""
    output_file = Path(__file__).with_name("index.html")
    output_file.write_text(HTML, encoding="utf-8")
    print(f"Страница создана: {output_file}")


if __name__ == "__main__":
    generate_page()
