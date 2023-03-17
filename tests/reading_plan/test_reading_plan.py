from unittest.mock import patch
from tech_news.analyzer.reading_plan import ReadingPlanService


def test_reading_plan_group_news():
    with patch("tech_news.database.find_news") as mock_find_news:
        mock_find_news.return_value = [
            {
                "url": "https://blog.betrybe.com/novidades/noticia-bacana",
                "title": "Notícia bacana",
                "writer": "Eu",
                "summary": "Algo muito bacana aconteceu",
                "reading_time": 4,
                "timestamp": "04/04/2021",
                "category": "Ferramentas",
            },
            {
                "url": "https://blog.betrybe.com/novidades/noticia-legal",
                "title": "Notícia bacana 2",
                "writer": "Você",
                "summary": "Algo muito bacana aconteceu de novo",
                "reading_time": 1,
                "timestamp": "07/04/2022",
                "category": "Novidades",
            },
            {
                "url": "https://blog.betrybe.com/novidades/noticia-bacana",
                "title": "Notícia demorada",
                "writer": "Eu",
                "summary": "Um negócio rolou aí",
                "reading_time": 30,
                "timestamp": "04/04/2021",
                "category": "Ferramentas",
            },
        ]
        reading = ReadingPlanService().group_news_for_available_time(10)

        assert len(reading["readable"]) == 2
        assert len(reading["unreadable"]) == 1
        assert reading["readable"][0]["unfilled_time"] == 6
        assert reading["readable"][1]["unfilled_time"] == 10
        with ValueError:
            ReadingPlanService().group_news_for_available_time(0)
