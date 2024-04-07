import csv,os
from typing import List
# Source of code to be refactored: https://github.com/lamchau/refactoring-exercise/tree/master/python
# ./startup_funding.csv is a snippet from https://github.com/lamchau/refactoring-exercise/blob/master/startup_funding.csv
# Original code to be refactored:

# class FundingRaised:
#   csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"startup_funding.csv")
  
#   @staticmethod
#   def where(options = {}):
#     with open(FundingRaised.csv_path, "rt") as csvfile:
#       data = csv.reader(csvfile, delimiter=',', quotechar='"')
#       # skip header
#       next(data)
#       csv_data = []
#       for row in data:
#         csv_data.append(row)

#     funding = []
#     if 'company_name' in options:
#       result = []
#       for row in csv_data:
#         if row[1] == options['company_name']:
#           result.append(row)
#       csv_data = result

#     if 'city' in options:
#       result = []
#       for row in csv_data:
#         if row[4] == options['city']:
#           result.append(row)
#       csv_data = result

#     if 'state' in options:
#       result = []
#       for row in csv_data:
#         if row[5] == options['state']:
#           result.append(row)
#       csv_data = result

#     if 'round' in options:
#       result = []
#       for row in csv_data:
#         if row[9] == options['round']:
#           result.append(row)
#       csv_data = result

#     output = []
#     for row in csv_data:
#       mapped = {}
#       mapped['permalink'] = row[0]
#       mapped['company_name'] = row[1]
#       mapped['number_employees'] = row[2]
#       mapped['category'] = row[3]
#       mapped['city'] = row[4]
#       mapped['state'] = row[5]
#       mapped['funded_date'] = row[6]
#       mapped['raised_amount'] = row[7]
#       mapped['raised_currency'] = row[8]
#       mapped['round'] = row[9]
#       output.append(mapped)

#     return output

#   @staticmethod
#   def find_by(options):
#     with open(FundingRaised.csv_path, "rt") as csvfile:
#       data = csv.reader(csvfile, delimiter=',', quotechar='"')
#       # skip header
#       next(data)
#       csv_data = []
#       for row in data:
#         csv_data.append(row)

#     if 'company_name' in options:
#       for row in csv_data:
#         if row[1] == options['company_name']:
#           mapped = {}
#           mapped['permalink'] = row[0]
#           mapped['company_name'] = row[1]
#           mapped['number_employees'] = row[2]
#           mapped['category'] = row[3]
#           mapped['city'] = row[4]
#           mapped['state'] = row[5]
#           mapped['funded_date'] = row[6]
#           mapped['raised_amount'] = row[7]
#           mapped['raised_currency'] = row[8]
#           mapped['round'] = row[9]
#           return mapped

#     if 'city' in options:
#       for row in csv_data:
#         if row[4] == options['city']:
#           mapped = {}
#           mapped['permalink'] = row[0]
#           mapped['company_name'] = row[1]
#           mapped['number_employees'] = row[2]
#           mapped['category'] = row[3]
#           mapped['city'] = row[4]
#           mapped['state'] = row[5]
#           mapped['funded_date'] = row[6]
#           mapped['raised_amount'] = row[7]
#           mapped['raised_currency'] = row[8]
#           mapped['round'] = row[9]
#           return mapped

#     if 'state' in options:
#       for row in csv_data:
#         if row[5] == options['state']:
#           mapped = {}
#           mapped['permalink'] = row[0]
#           mapped['company_name'] = row[1]
#           mapped['number_employees'] = row[2]
#           mapped['category'] = row[3]
#           mapped['city'] = row[4]
#           mapped['state'] = row[5]
#           mapped['funded_date'] = row[6]
#           mapped['raised_amount'] = row[7]
#           mapped['raised_currency'] = row[8]
#           mapped['round'] = row[9]
#           return mapped

#     if 'round' in options:
#       for row in csv_data:
#         if row[9] == options['round']:
#           mapped = {}
#           mapped['permalink'] = row[0]
#           mapped['company_name'] = row[1]
#           mapped['number_employees'] = row[2]
#           mapped['category'] = row[3]
#           mapped['city'] = row[4]
#           mapped['state'] = row[5]
#           mapped['funded_date'] = row[6]
#           mapped['raised_amount'] = row[7]
#           mapped['raised_currency'] = row[8]
#           mapped['round'] = row[9]
#           return mapped

#     raise RecordNotFound

# class RecordNotFound(Exception):
#   pass


# Refactored code
class FundingRaised:
  
  
  OUTPUT_FIELDS = ['permalink', 'company_name','number_employees','category', 'city', 'state', 'funded_date','raised_amount', 'raised_currency', 'round']
  SEARCH_OPTIONS_WITH_COLUMN_NUM = {'company_name':1,'city':4, 'state':5, 'round':9}
  csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"startup_funding.csv")
  
  @staticmethod
  def read_csv(csv_file_path: str) -> List:
    with open(FundingRaised.csv_path, "rt") as csvfile:
      data = csv.reader(csvfile, delimiter=',', quotechar='"')
      # skip header
      next(data)
      csv_data = []
      for row in data:
        csv_data.append(row)
    return csv_data

  @staticmethod
  def where(options = {}):
    csv_data = FundingRaised.read_csv(FundingRaised.csv_path)

    for search_option, column_num in FundingRaised.SEARCH_OPTIONS_WITH_COLUMN_NUM.items():
      if search_option in options:
        result = []
        for row in csv_data:
            if row[column_num] == options[search_option]:
                result.append(row)
        csv_data = result

    output = []
    for row in csv_data:
      mapped = {}
      for i in range(0,len(FundingRaised.OUTPUT_FIELDS)):
        mapped[FundingRaised.OUTPUT_FIELDS[i]] = row[i]
      output.append(mapped)

    return output

  @staticmethod
  def find_by(options):
    csv_data = FundingRaised.read_csv(FundingRaised.csv_path)

    for search_option,column_num in FundingRaised.SEARCH_OPTIONS_WITH_COLUMN_NUM.items():
      if search_option in options:
        for row in csv_data:
          if row[column_num] == options[search_option]:
            mapped = {}
            for i in range(0,len(FundingRaised.OUTPUT_FIELDS)):
              mapped[FundingRaised.OUTPUT_FIELDS[i]] = row[i]
            return mapped

    raise RecordNotFound

class RecordNotFound(Exception):
  pass

