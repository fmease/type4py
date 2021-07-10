from type4py.server.app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{app.config['DB_USER']}:{app.config['DB_PASS']}@localhost:5432/{app.config['DB_NAME']}"
sqla = SQLAlchemy(app)
mig = Migrate(app, sqla)

class PredictReqs(sqla.Model):
    """
    Represents the table predict_reqs which stores requests to the server plus
    their timestamps and errors if any
    """

    # __table__ = sqla.Model.metadata['predict_reqs']

    # def __repr__(self):
    #     return self.DISTRICT
    
    __tablename__ = 'predict_reqs'

    id = sqla.Column(sqla.Integer, primary_key=True)
    IP_addr = sqla.Column(sqla.String, nullable=False)
    start_t = sqla.Column(sqla.DateTime, nullable=False)
    finished_t = sqla.Column(sqla.DateTime, nullable=False)
    error = sqla.Column(sqla.String)

    def __init__(self, IP_addr, start_t, finished_t, error):
        self.IP_addr = IP_addr
        self.start_t= start_t
        self.finished_t = finished_t
        self.error = error
