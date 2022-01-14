from django import forms
from django.shortcuts import render

YEARS = [x for x in range(2010, 2050)]


class MainForm(forms.Form):
    start_date = forms.DateField(label='Дата отсчета ', widget=forms.SelectDateWidget(years=YEARS))
    end_date = forms.DateField(label='Искомая дата', widget=forms.SelectDateWidget(years=YEARS))

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data['start_date']
        end_date = cleaned_data['end_date']
        if end_date < start_date:
            raise forms.ValidationError('Искомая дата раньше даты отсчета')


def count_week(start_date, end_date):
    """
    Расчет номера недели по алгоритму, описанному в readme
    """
    first_day = start_date.isoweekday()
    week_number = ((end_date - start_date).days + first_day) // 7 + 1
    return week_number


def process_dates(request):
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            week_number = count_week(start_date, end_date)
            return render(request, 'index.html', {'form': form.as_p, 'week_number': week_number})
        else:
            return render(request, 'index.html', {'form': form.as_p})

    form = MainForm(initial={'start_date': '2019-01-01', 'end_date': '2019-01-05'})
    return render(request, 'index.html', {'form': form.as_p})
