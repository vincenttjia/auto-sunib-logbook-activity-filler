import requests

ssourl = "https://activity-enrichment.apps.binus.ac.id/Auth/SSOStudentLogin?token=GANTI DENGAN TOKEN MASING-MASING"
Activity = "Aws Academy"
Description = "Aws Academy"


Febuary_logbook_id = "0686b6ba-1ab5-40c4-a44e-ddcf18d7dd5a"
March_logbook_id = "002d4297-5962-4ffc-976e-9a28d0f74c43"
April_logbook_id = "c5033105-000e-4607-b40c-cc339c11b5e2"

def main():
  global ssourl,Activity,Description,Febuary_logbook_id,March_logbook_id,April_logbook_id

  s = requests.session()
  s.get(ssourl)
  url = "https://activity-enrichment.apps.binus.ac.id/LogBook/StudentSave"

  # INSERT OFF
  #FEBRUARY
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":Febuary_logbook_id,"model[Date]":"2021-02-22T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":Febuary_logbook_id,"model[Date]":"2021-02-23T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":Febuary_logbook_id,"model[Date]":"2021-02-24T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":Febuary_logbook_id,"model[Date]":"2021-02-25T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":Febuary_logbook_id,"model[Date]":"2021-02-26T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":Febuary_logbook_id,"model[Date]":"2021-02-27T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":Febuary_logbook_id,"model[Date]":"2021-02-28T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  #MARET
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-02T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-04T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-06T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-09T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-011T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-12T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-13T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-16T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-18T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-20T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-23T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-27T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-30T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  # APRIL
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":April_logbook_id,"model[Date]":"2021-04-01T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":April_logbook_id,"model[Date]":"2021-04-02T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":April_logbook_id,"model[Date]":"2021-04-03T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":April_logbook_id,"model[Date]":"2021-04-06T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":April_logbook_id,"model[Date]":"2021-04-08T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":April_logbook_id,"model[Date]":"2021-04-10T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":April_logbook_id,"model[Date]":"2021-04-11T00:00:00","model[Activity]":"OFF","model[ClockIn]":"OFF","model[ClockOut]":"OFF","model[Description]":"OFF"}
  r = s.post(url, data=payload)
  print(r.json())



  # INSERT Log Book
  # MARET
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-01T00:00:00","model[Activity]":Activity,"model[ClockIn]":"03:20 pm","model[ClockOut]":"07:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-03T00:00:00","model[Activity]":Activity,"model[ClockIn]":"09:20 am","model[ClockOut]":"13:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-05T00:00:00","model[Activity]":Activity,"model[ClockIn]":"03:20 pm","model[ClockOut]":"07:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-08T00:00:00","model[Activity]":Activity,"model[ClockIn]":"03:20 pm","model[ClockOut]":"07:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-10T00:00:00","model[Activity]":Activity,"model[ClockIn]":"11:20 am","model[ClockOut]":"13:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-15T00:00:00","model[Activity]":Activity,"model[ClockIn]":"01:20 pm","model[ClockOut]":"07:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-17T00:00:00","model[Activity]":Activity,"model[ClockIn]":"09:20 am","model[ClockOut]":"01:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-19T00:00:00","model[Activity]":Activity,"model[ClockIn]":"03:20 pm","model[ClockOut]":"07:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-22T00:00:00","model[Activity]":Activity,"model[ClockIn]":"03:20 pm","model[ClockOut]":"07:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-24T00:00:00","model[Activity]":Activity,"model[ClockIn]":"03:20 pm","model[ClockOut]":"05:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-25T00:00:00","model[Activity]":Activity,"model[ClockIn]":"07:20 pm","model[ClockOut]":"09:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-26T00:00:00","model[Activity]":Activity,"model[ClockIn]":"03:20 pm","model[ClockOut]":"07:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-29T00:00:00","model[Activity]":Activity,"model[ClockIn]":"03:20 pm","model[ClockOut]":"07:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":March_logbook_id,"model[Date]":"2021-03-31T00:00:00","model[Activity]":Activity,"model[ClockIn]":"09:20 am","model[ClockOut]":"01:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())

  #APRIL
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":April_logbook_id,"model[Date]":"2021-04-05T00:00:00","model[Activity]":Activity,"model[ClockIn]":"03:20 pm","model[ClockOut]":"05:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":April_logbook_id,"model[Date]":"2021-04-07T00:00:00","model[Activity]":Activity,"model[ClockIn]":"09:20 am","model[ClockOut]":"01:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())
  payload = {"model[ID]":"00000000-0000-0000-0000-000000000000","model[LogBookHeaderID]":April_logbook_id,"model[Date]":"2021-04-09T00:00:00","model[Activity]":Activity,"model[ClockIn]":"03:20 pm","model[ClockOut]":"07:00 pm","model[Description]":Description}
  r = s.post(url, data=payload)
  print(r.json())

if __name__ == '__main__':
  main()