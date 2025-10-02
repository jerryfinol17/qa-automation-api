Hey! I'm Jerry, and this is my API testing playground: experiments, tips, and live code for CRUD ops on JSONPlaceholder. Built with Python, pytest, and Allure for fun, robust checks—data-driven and CI-ready. Hope it sparks ideas or saves you some headaches! Got tweaks? Hit me with 'em—no mercy! ;) 
## Tecnologías
- Python 3.9+
- pytest para testing
- requests para HTTP calls
- Allure para reportes visuales
- JSONPlaceholder API para demo
"""


## Cómo Correr los Tests
1. Clona el repo: `git clone https://github.com/jerryfinol17/qa-automation-api.git`
2. Instala dependencias: `pip install -r requirements.txt`
3. Corre tests: `pytest tests/ --alluredir=reports/allure-results --html=reports/report.html`
4. Genera reporte Allure: `allure serve reports/allure-results`
"""


## Tests Implementados
- 7 tests funcionales cubriendo CRUD en /posts:
  - test_crud_posts[posts_get]: GET /posts (status 200, list con keys requeridas)
  - test_crud_posts[posts_post]: POST /posts (status 201, dict con match de payload)
  - test_crud_posts[posts_put]: PUT /posts/1 (status 200, updates match)
  - test_crud_posts[posts_delete]: DELETE /posts/1 (status 200, response empty)
  - test_posts_get_with_user_filter: GET /posts?userId=1 (filtro, len=10, userId=1)
  - 2 dummies para fixtures (base_url, configs, payloads)

Coverage: 100% de endpoints en config. Reportes en reports/.
![Screenshot 2025-10-02 150505.png](docs/Screenshot%202025-10-02%20150505.png)