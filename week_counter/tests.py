from datetime import date
from http import HTTPStatus

from django.test import TestCase

from .views import count_week, MainForm


class CounterTestCase(TestCase):
    def test_first_day(self):
        start_date = date(2019, 1, 1)
        end_date = date(2019, 1, 1)
        result = count_week(start_date, end_date)
        self.assertEqual(1, result)

    def test_first_week(self):
        start_date = date(2019, 1, 1)
        end_date = date(2019, 1, 5)
        result = count_week(start_date, end_date)
        self.assertEqual(1, result)

    def test_second_week(self):
        start_date = date(2019, 1, 1)
        end_date = date(2019, 1, 6)
        result = count_week(start_date, end_date)
        self.assertEqual(2, result)


class MainViewTestCase(TestCase):
    def test_first_day(self):
        start_date = date(2019, 1, 1)
        end_date = date(2019, 1, 1)
        response = self.client.post('/week/', data={'start_date': start_date, 'end_date': end_date})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotContains(
            response, 'Искомая дата раньше даты отсчета', html=True
        )
        self.assertContains(response, 'Номер недели: 1', html=True)

    def test_first_week(self):
        start_date = date(2019, 1, 1)
        end_date = date(2019, 1, 5)
        response = self.client.post('/week/', data={'start_date': start_date, 'end_date': end_date})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotContains(
            response, 'Искомая дата раньше даты отсчета', html=True
        )
        self.assertContains(response, 'Номер недели: 1', html=True)

    def test_second_week(self):
        start_date = date(2019, 1, 1)
        end_date = date(2019, 1, 6)
        response = self.client.post('/week/', data={'start_date': start_date, 'end_date': end_date})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotContains(
            response, 'Искомая дата раньше даты отсчета', html=True
        )
        self.assertContains(response, 'Номер недели: 2', html=True)

    def test_start_date_after_end_date(self):
        start_date = date(2020, 1, 1)
        end_date = date(2019, 1, 1)
        response = self.client.post('/week/', data={'start_date': start_date, 'end_date': end_date})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response, 'Искомая дата раньше даты отсчета', html=True
        )


class MainFormTestCase(TestCase):
    def test_first_day(self):
        start_date = date(2019, 1, 1)
        end_date = date(2019, 1, 1)
        form = MainForm(data={'start_date': start_date, 'end_date': end_date})
        self.assertNotIn('__all__', form.errors)

    def test_start_date_after_end_date(self):
        start_date = date(2020, 1, 1)
        end_date = date(2019, 1, 1)
        form = MainForm(data={'start_date': start_date, 'end_date': end_date})
        self.assertEqual(form.errors['__all__'], ['Искомая дата раньше даты отсчета'])
