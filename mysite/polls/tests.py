from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.
class QuestionMethodTests(TestCase):
    def test_was_published_recently(self):
        time=timezone.now()+datetime.timedelta(days=10)
        future_question=Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(),False)
        
    def test_was_published_recently_with_old_question(self):
        time=timezone.now()-datetime.timedelta(days=20)
        old_question=Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(),False)
    
    def test_was_published_recently_with_recent_question(self):
        time=timezone.now()-datetime.timedelta(hours=1)
        recent_question=Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(),True)