from app import app
from flask import request
from unittest import TestCase
import resource_handler

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class NULAWebScraperTestCase(TestCase):
  @classmethod
  def setUpClass(cls):
    print("INSIDE SET UP CLASS")

  @classmethod
  def tearDownClass(cls):
    print("INSIDE TEAR DOWN CLASS")
  
  def setUp(self):
    print("INSIDE SET UP")
  
  def tearDown(self):
    print("INSIDE TEAR DOWN")
  
  """Testing a GET request"""
  def test_resource_menu_form(self):
    with app.test_client() as client:
      res = client.get('/')
      html = res.get_data(as_text=True)

      self.assertEqual(res.status_code, 200)
      self.assertIn('<h1 class="text-center">NAMI Urban LA Resource Page Search Engine</h1>', html)
  
  """Testing a POST request"""
  def test_resource_menu_submit(self):
    with app.test_client() as client:
      res = client.post('/resources/0', data={'category_name': 'Crisis Support, Helplines & Warmlines'})
      html = res.get_data(as_text=True)

      self.assertEqual(res.status_code, 200)
      self.assertIn('<b> Check Out These Links for  Crisis Support, Helplines &amp; Warmlines:</b>', html)

  """Testing the resource handler"""
  def test_get_resources(self):
    self.assertEqual(resource_handler.get_resources(0), 
            ['http://www.suicidepreventionlifeline.org',
            'http://www.hopeline.com',
            'mailto:info@nami.org',
            'https://www.nami.org/Find-Support/NAMI-HelpLine',
            'https://www.crisistextline.org',
            'http://www.TeenLineOnline.org',
            'https://calyouth.org',
            'http://www.TheTrevorProject.org',
            'https://www.translifeline.org',
            'http://dmh.lacounty.gov/',
            'http://www.211.org',
            'https://www.7cups.com',
            'http://prpsn.org/services/warm-line',
            'https://www.nationaleatingdisorders.org',
            'https://www.veteranscrisisline.net',
            'https://www.samhsa.gov/find-help/national-helpline',
            'https://addictionresource.com',
            'https://www.samhsa.gov/find-help/disaster-distress-helpline',
            'https://www.thehotline.org',
            'https://www.rainn.org'])
