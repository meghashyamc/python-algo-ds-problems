from refactoring import funding_raised


# These test are from https://github.com/lamchau/refactoring-exercise/tree/master/python
# They have been copied here to test refactoring/funding_raised.py


def test_where_returns_events():
  assert len(funding_raised.FundingRaised.where({'company_name': 'Facebook'})) == 7

def test_where_returns_correct_keys():
  row = funding_raised.FundingRaised.where({'company_name': 'Facebook'})[0]
  keys = ['permalink', 'company_name', 'number_employees', 'category', 'city', 'state', 'funded_date', 'raised_amount', 'raised_currency', 'round']
  values = ['facebook', 'Facebook', '450', 'web', 'Palo Alto', 'CA', '1-Sep-04', '500000', 'USD', 'angel']
  for i in range(0, len(keys)):
    assert row[keys[i]] == values[i]

def test_where_returns_events_by_city():
  assert len(funding_raised.FundingRaised.where({'city': 'Tempe'})) == 3

def test_where_returns_events_by_state():
  assert len(funding_raised.FundingRaised.where({'state': 'CA'})) == 873

def test_where_returns_events_by_company():
  assert len(funding_raised.FundingRaised.where({'company_name': 'Facebook', 'round': 'a'})) == 1

def test_where_returns_events_by_type():
  assert len(funding_raised.FundingRaised.where({'round': 'a'})) == 582

def test_where_returns_no_events():
  assert len(funding_raised.FundingRaised.where({'company_name': 'NotFacebook'})) == 0

def test_find_by_event_by_company_name():
  row = funding_raised.FundingRaised.find_by({'company_name': 'Facebook'})
  keys = ['permalink', 'company_name', 'number_employees', 'category', 'city', 'state', 'funded_date', 'raised_amount', 'raised_currency', 'round']
  values = ['facebook', 'Facebook', '450', 'web', 'Palo Alto', 'CA', '1-Sep-04', '500000', 'USD', 'angel']
  for i in range(0, len(keys)):
    assert row[keys[i]] == values[i]

def test_find_by_event_by_state():
  row = funding_raised.FundingRaised.find_by({'state': 'CA'})
  keys = ['permalink', 'company_name', 'number_employees', 'category', 'city', 'state', 'funded_date', 'raised_amount', 'raised_currency', 'round']
  values = ['digg', 'Digg', '60', 'web', 'San Francisco', 'CA', '1-Dec-06', '8500000', 'USD', 'b']
  for i in range(0, len(keys)):
    assert row[keys[i]] == values[i]

test_where_returns_events()
test_where_returns_correct_keys()
test_where_returns_events_by_city()
test_where_returns_events_by_state()
test_where_returns_events_by_company()
test_where_returns_events_by_type()
test_where_returns_no_events()
test_find_by_event_by_company_name()
test_find_by_event_by_state()