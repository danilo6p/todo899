
from app import database
from datetime import datetime


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)


class Task(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    """:type : int"""

    description = database.Column(database.String(200), nullable=False)
    """:type : str"""
    
    status = database.Column(database.String(20), default="A fazer")
    """:type : str"""

    date_created = database.Column(database.DateTime, default=datetime.utcnow)
    """:type : datetime"""
    
    date_doing = database.Column(database.DateTime)
    """:type : datetime"""
    
    date_done = database.Column(database.DateTime)
    """:type : datetime"""
    
    time_spend = database.Column(database.String(20))
    """:type : string"""
    
    time_estimated = database.Column(database.String(20))
    """:type : string"""
    
    category = database.Column(database.String(50))
    """:type : string"""

    def __repr__(self):
        """override __repr__ method"""
        return f"Task: #{self.id}, content: {self.description}"
    
    
