import hug


@hug.get('/quotes')
def quotes():
    return ['a', 'b', 'c']
