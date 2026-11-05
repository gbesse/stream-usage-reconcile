import unittest
from stream_usage_reconcile.core import run
class DomainTests(unittest.TestCase):
 def test_cumulative_not_sum(self):
  x=run({'streams':[dict(id='a',mode='cumulative',completed=True,events=[dict(id='1',tokens=5),dict(id='2',tokens=10)])]});self.assertEqual(x['total_tokens'],10);self.assertEqual(x['naive_sum'],15)
 def test_delta_dedupe(self):
  e=dict(id='1',tokens=3);self.assertEqual(run({'streams':[dict(id='a',mode='delta',completed=True,events=[e,e])]})['total_tokens'],3)
 def test_decrease_unknown(self):self.assertIsNone(run({'streams':[dict(id='a',mode='cumulative',completed=True,events=[dict(id='1',tokens=5),dict(id='2',tokens=2)])]})['total_tokens'])
