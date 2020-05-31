from flask import Blueprint, render_template

from idoctor.forms.calendar_forms import CalendarForm

calendar_bp = Blueprint('calendar', __name__, url_prefix='/calendars')


@calendar_bp.route('/', methods=['GET', 'POST'])
def calendar():
    form = CalendarForm()

    if form.validate_on_submit():
        pass

    return render_template('calendar.html', form=form)