# app.py

from flask import Flask
from sqlalchemy.event import listen

from models import Todo, Priority, Base
from sqlalchemy import event, DDL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.test'
db = SQLAlchemy(app)


#first solution
# @event.listens_for(Priority.__table__, 'after_create')
# def insert_initial_values(*args, **kwargs):
#     db.session.add(Priority(name='low'))
#     db.session.add(Priority(name='medium'))
#     db.session.add(Priority(name='high'))
#     db.session.commit()


# second solution
# def insert_initial_values(*args, **kwargs):
#     db.session.add(Priority(name='low'))
#     db.session.add(Priority(name='medium'))
#     db.session.add(Priority(name='high'))
#     db.session.commit()
#
#
# event.listen(Priority.__table__, 'after_create', insert_initial_values)

# third solution
event.listen(Priority.__table__, 'after_create',
             DDL(""" INSERT INTO priority (id, name) VALUES (1, 'low'), (2, 'medium'), (3, 'high') """))


@app.before_first_request
def setup():
    # Recreate database each time for demo
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)

    low_priority = db.session.query(Priority).filter_by(name=u'low').first()
    medium_priority = db.session.query(Priority).filter_by(name=u'medium').first()
    high_priority = db.session.query(Priority).filter_by(name=u'high').first()

    db.session.add(Todo(title=u'title1', description=u'description1', priority_id=low_priority.id))
    db.session.add(Todo(title=u'title2', description=u'description2', priority_id=medium_priority.id))
    db.session.add(Todo(title=u'title3', description=u'description3', priority_id=high_priority.id))
    db.session.commit()


@app.route('/')
def index():
    todos = db.session.query(Todo).join(Priority).all()

    return u"<br>".join([u"{0}: {1}: {2}".format(todo.title, todo.description, todo.priority.name) for todo in todos])


if __name__ == '__main__':
    Base.metadata.create_all(bind=db.engine)
    app.run(debug=True)
