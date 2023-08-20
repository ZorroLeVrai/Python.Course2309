import json

# python object(dictionary) to be dumped
dict1 ={
	"emp1": {
		"name": "Lisa",
		"designation": "programmer",
		"age": "34",
		"salary": "54000"
	},
	"emp2": {
		"name": "Elis",
		"designation": "Trainee",
		"age": "24",
		"salary": "40000"
	},
}

# the json file where the output must be stored
with open("myfile.json", "w") as out_file:
    json.dump(dict1, out_file, indent = 2)

with open("myfile.json", "r") as in_file:
    json_obj = json.load(in_file)
    print(json.dumps(json_obj, indent=2))