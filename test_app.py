import hug
import app

def test_get():
    r = hug.test.get(app, 'quotes')
    assert r.data == ['a', 'b', 'c']
