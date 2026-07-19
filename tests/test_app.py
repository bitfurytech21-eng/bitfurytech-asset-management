import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location("app_module", ROOT / "app.py")
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)


def test_dashboard_requires_login():
    app = app_module.create_app()
    client = app.test_client()

    response = client.get("/dashboard", follow_redirects=False)
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


def test_auth_pages_render_successfully():
    app = app_module.create_app()
    client = app.test_client()

    for route in ["/", "/login", "/register"]:
        response = client.get(route)
        assert response.status_code == 200, route
