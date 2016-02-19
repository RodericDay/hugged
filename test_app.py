import hug
import app


def test_get():
    assert hug.test.post(app, 'quotes', {'text': 'Thing'}).status == '200 OK'
    for k in hug.test.get(app, 'quotes').data[0].keys():
        assert k in ['author', 'text', 'qid']
