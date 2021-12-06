import json
from django.test import TestCase
from employee.models import Employee

class TestEmployee(TestCase):
    url = '/candidates/'
    data1 = {
        "name": "Jane Doe",
        "workExperience": [
            {"start": "Jul 2018", "end": "Aug 2019"},
            {"start": "Sep 2019", "end": "Aug 2021"},
            {"start": "Oct 2019", "end": "Dec 2021"}
        ]
    }
    data2 = {
        "name": "Vasyl Grudin",
        "workExperience": [
            {"start": "Jun 2012", "end": "Dec 2014"},
            {"start": "Jun 2013", "end": "Jan 2015"},
            {"start": "Oct 2017", "end": "Feb 2020"},
            {"start": "Mar 2020", "end": "Jul 2021"},
            {"start": "Jun 2016", "end": "Dec 2019"},
            {"start": "Dec 2017", "end": "Feb 2018"}
        ]
    }

    def test_post_candidates(self):
        response = self.client.post(self.url, json.dumps(self.data1),content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], Employee.objects.first().id)


    def test_get_candidates(self):
        self.client.post(self.url, json.dumps(self.data1), content_type='application/json')
        self.client.post(self.url, json.dumps(self.data2), content_type='application/json')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # Sorted by workExperience
        self.data2['workExperience'].sort(key=lambda exper: (int(exper['start'][-4:]), int(exper['end'][-4:])))
        self.assertEqual(response.data['candidates'][1]['workExperience'] , self.data2['workExperience'])

        #Sorted by totalExperience
        self.assertGreater(response.data['candidates'][1]['totalExperience'], response.data['candidates'][0]['totalExperience'])
# Create your tests here.
