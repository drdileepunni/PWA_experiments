from app import db
from flask import current_app

# Define the link table for the many-to-many relationship between reports and sensitive antibiotics
reports_sensitive_antibiotics = db.Table('reports_sensitive_antibiotics',
                                         db.Column('report_id', db.Integer, db.ForeignKey('report.id'), primary_key=True),
                                         db.Column('antibiotic_id', db.Integer, db.ForeignKey('antibiotic.id'), primary_key=True))

# Define the link table for the many-to-many relationship between reports and intermediate antibiotics
reports_intermediate_antibiotics = db.Table('reports_intermediate_antibiotics',
                                            db.Column('report_id', db.Integer, db.ForeignKey('report.id'), primary_key=True),
                                            db.Column('antibiotic_id', db.Integer, db.ForeignKey('antibiotic.id'), primary_key=True))

# Define the link table for the many-to-many relationship between reports and resistant antibiotics
reports_resistant_antibiotics = db.Table('reports_resistant_antibiotics',
                                         db.Column('report_id', db.Integer, db.ForeignKey('report.id'), primary_key=True),
                                         db.Column('antibiotic_id', db.Integer, db.ForeignKey('antibiotic.id'), primary_key=True))

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    mrn = db.Column(db.String(10), nullable=False)
    hospital = db.Column(db.String(64), nullable=False)
    organism_id = db.Column(db.Integer, db.ForeignKey('organism.id'), nullable=False)
    organism = db.relationship('Organism', backref=db.backref('reports', lazy=True))
    sensitive_antibiotics = db.relationship('Antibiotic', secondary=reports_sensitive_antibiotics,
                                             backref=db.backref('reports_sensitive', lazy='dynamic'))
    intermediate_antibiotics = db.relationship('Antibiotic', secondary=reports_intermediate_antibiotics,
                                                backref=db.backref('reports_intermediate', lazy='dynamic'))
    resistant_antibiotics = db.relationship('Antibiotic', secondary=reports_resistant_antibiotics,
                                             backref=db.backref('reports_resistant', lazy='dynamic'))

class Organism(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    type = db.Column(db.String(64), nullable=False)

class Antibiotic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    type = db.Column(db.String(64), nullable=False)