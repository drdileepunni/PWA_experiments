from flask import render_template, request, redirect, url_for
from app import app, db
from app.forms import AddReportForm, AddDataForm
from app.models import Report, Organism, Antibiotic

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_report', methods=['GET', 'POST'])
def add_report():
    form = AddReportForm()
    organisms = Organism.query.all()
    antibiotics = Antibiotic.query.all()
    if request.method == 'POST' and form.validate():
        report = Report(name=form.name.data,
                        mrn=form.mrn.data,
                        hospital=form.hospital.data,
                        organism_id=form.organism.data,
                        sensitive_antibiotics=form.sensitive_antibiotics.data,
                        intermediate_antibiotics=form.intermediate_antibiotics.data,
                        resistant_antibiotics=form.resistant_antibiotics.data)
        db.session.add(report)
        db.session.commit()
        return redirect(url_for('view_reports'))
    return render_template('add_report.html', form=form, organisms=organisms, antibiotics=antibiotics)

@app.route('/view_reports')
def view_reports():
    reports = Report.query.all()
    return render_template('view_reports.html', reports=reports)

@app.route('/add_data_to_db', methods=['GET', 'POST'])
def add_data_to_db():
    form = AddDataForm()
    if request.method == 'POST' and form.validate():
        if form.data_type.data == 'organism':
            organism = Organism(name=form.name.data, type=form.data_value.data)
            db.session.add(organism)
            db.session.commit()
        elif form.data_type.data == 'antibiotic':
            antibiotic = Antibiotic(name=form.name.data, type=form.data_value.data)
            db.session.add(antibiotic)
            db.session.commit()
        return redirect(url_for('add_data_to_db'))
    return render_template('add_data_to_db.html', form=form)
