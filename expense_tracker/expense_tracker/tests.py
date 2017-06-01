
from pyramid import testing
from pyramid.response import Response


def test_home_view_returns_response():
    from expense_tracker.views.default import list_view_page
    request = testing.DummyRequest()
    response = list_view_page(request)
    assert isinstance(response, Response)

def test_creat_view_returns_response():
    from expense_tracker.views.default import create_view_page
    request = testing.DummyRequest()
    response = create_view_page(request)
    assert isinstance(response, Response)

def test_home_view_returns_good():
    from expense_tracker.views.default import list_view_page
    request = testing.DummyRequest()
    response = list_view_page(request)
    assert response.status_code == 200

def test_creat_view_returns_good():
    from expense_tracker.views.default import create_view_page
    request = testing.DummyRequest()
    response = create_view_page(request)
    assert response.status_code == 200
