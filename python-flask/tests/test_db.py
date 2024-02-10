import sqlite3

import pytest

from flaskr.db import get_db

def test_get_close_db(app):
    with app.app_context():
        db=get_db()
        assert db is get_db()  # same connection is returned everytime

    
    with pytest.raises(sqlite3.ProgrammingError) as e:  # after the context connetion is closed
        db.execute('select 1')
    
        assert 'closed' in str(e.value) # after the context connetion is closed

# The init-db command should call the init_db function and output a message.

def test_init_db(runner, monkeypatch):
    class Recoder(object):
        called = False
    
    def fake_init_db():
        Recoder.called = True


    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)

    result = runner.invoke(args=['init-db'])

    assert 'Initialized' in result.output
    assert Recoder.called
