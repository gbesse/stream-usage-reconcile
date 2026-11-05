import json,math
from .common import number,integer,identifier,unique_ids
def run(d):
 streams=d['streams'];unique_ids(streams)
 if len(streams)>100:raise ValueError('streams')
 out=[]
 for stream in streams:
  mode=stream['mode'];events=stream['events']
  if mode not in ['delta','cumulative']or len(events)>10000:raise ValueError('mode')
  seen={};total=0;valid=True;duplicates=0;issues=[]
  for event in events:
   eid=identifier(event['id']);value=integer(event['tokens'],0,10**12)
   if eid in seen:
    if seen[eid]!=value:valid=False;issues.append('conflicting_event_id')
    else:duplicates+=1
    continue
   seen[eid]=value
   if mode=='delta':total+=value
   elif value<total:valid=False;issues.append('cumulative_decrease');total=value
   else:total=value
  out.append(dict(id=stream['id'],tokens=total if valid and stream.get('completed')is True else None,observed_tokens=total,duplicate_events=duplicates,issues=issues,complete=valid and stream.get('completed')is True))
 return dict(streams=out,total_tokens=sum(r['tokens']for r in out)if all(r['complete']for r in out)else None,naive_sum=sum(e['tokens']for s in streams for e in s['events']))
