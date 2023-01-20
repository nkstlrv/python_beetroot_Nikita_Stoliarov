import json

demo_phonebook = [
  {
    "Number": "1782174849",
    "Name": "Michael",
    "Surname": "Scott",
    "Country": "USA",
    "City": "Scranton",
    "State": "Pennsylvania",

  },
  {
    "Number": "+390556667788",
    "Name": "Alan",
    "Surname": "Turing",
    "Country": "UK",
    "City": "Wilmslow",
    "State": "England",

  }
]
with open ("../phonebook.json", "w") as pb:
    json.dump(demo_phonebook, pb)
