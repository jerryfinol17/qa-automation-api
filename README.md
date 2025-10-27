## API Testing Playground: CRUD on JSONPlaceholderHey!
I'm Jerry, and this is my API testing playground: experiments, tips, and live code for CRUD ops on Reqres.in. Built with Python, pytest, and Allure for fun, robust checks—data-driven and CI-ready. Hope it sparks ideas or saves you some headaches! Got tweaks? Hit me with 'em—no mercy! ;) 
## Technologies:
- Python 3.9+
- pytest for testing
- requests for HTTP calls
- Allure for visual reports
- Reqres.in for demos

## How to Run the TestsClone the repo:
1. git clone https://github.com/jerryfinol17/qa-automation-api.git
2. Install dependencies: pip install -r requirements.txt
3. Run tests: pytest tests/ --alluredir=reports/allure-results --html=reports/report.html
4. Generate Allure report: allure serve reports/allure-results

## Implemented Tests:
7 functional tests covering CRUD on /posts:
- test_crud_posts[posts_get]: GET /posts (status 200, list with required keys)
- test_crud_posts[posts_post]: POST /posts (status 201, dict matching payload)
- test_crud_posts[posts_put]: PUT /posts/1 (status 200, updates match)
- test_crud_posts[posts_delete]: DELETE /posts/1 (status 200, empty response)
- test_posts_get_with_user_filter: GET /posts?userId=1 (filter applied, len=10, userId=1)
- 2 dummy tests for fixtures (base_url, configs, payloads)

## Coverage:
100% of endpoints in config. Reports in reports/
![Screenshot 2025-10-02 150505.png](docs/Screenshot%202025-10-02%20150505.png)
