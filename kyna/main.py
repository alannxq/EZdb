import ast
import os

def load(file_name):
	if not os.path.exists(file_name):
		with open(f"{file_name}.db", 'w') as f:
			f.write("{}")

	return apple(file_name)

class apple:
	def __init__(self, file_name):
		self.file_name = file_name

		with open(self.file_name, "r+") as f:
			self.content = ast.literal_eval(f.read())

	def get(self, key):
		try: return self.content[key]
		except: return False

	def set(self, key, value):
		self.content[key] = value
		return True

	def asDict(self) -> dict:
		return self.content

	def dump(self):
		with open(self.file_name, "w+") as f:
			f.write(str(self.content))

	def dumpDict(self, dictionary):
		with open(self.file_name, "w+") as f:
			f.write(str(dictionary))
