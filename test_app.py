import hug
import app


def test_get():
    assert hug.test.post(app, 'quotes', {'text': 'Thing'}).status == '200 OK'
    assert hug.test.get(app, 'quotes').data == ['Thing']
