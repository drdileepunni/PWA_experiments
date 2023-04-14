from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SelectMultipleField, validators

class AddReportForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    mrn = StringField('MRN', [validators.DataRequired(), validators.Length(min=1, max=10)])
    hospital = StringField('Hospital', [validators.DataRequired()])
    organism = SelectField('Organism', coerce=int, validators=[validators.DataRequired()])
    sensitive_antibiotics = SelectMultipleField('Sensitive Antibiotics', coerce=int, validators=[validators.DataRequired()])
    intermediate_antibiotics = SelectMultipleField('Intermediate Antibiotics', coerce=int)
    resistant_antibiotics = SelectMultipleField('Resistant Antibiotics', coerce=int, validators=[validators.DataRequired()])

class AddDataForm(FlaskForm):
    data_type = SelectField('Data Type', choices=[('organism', 'Organism'), ('antibiotic', 'Antibiotic')],
                            validators=[validators.DataRequired()])
    organism_name = StringField('Organism Name', [validators.DataRequired()])
    antibiotic_name = StringField('Antibiotic Name', [validators.DataRequired()])
    organism_type = StringField('Organism Type')
    antibiotic_type = StringField('Antibiotic Type')

