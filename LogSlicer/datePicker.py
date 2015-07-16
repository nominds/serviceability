from flask.ext.admin import BaseView, expose
from wtforms import DateField, Form
from wtforms.validators import Required
from flask.ext.admin.form import widgets
from flask import request

class DateRangeForm(Form):
    start_date = DateField('Start', validators=[Required()], format = '%d/%m/%Y', description = 'Time that the event will occur', widget=widgets.DatePickerWidget)

class ReportingView(BaseView):
    @expose('/')
    def index(self):
        form = DateRangeForm(request.form)
        return self.render('reporting.j2', form=form)