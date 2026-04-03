import os
import json
from datetime import datetime
FILE='notes.json'

def load_notes():
	if os.path.exists(FILE)!=1:
		return []
	with open(FILE,"r",encoding="utf-8") as f:
		return json.load(f)
def save_notes(notes):
	with open(FILE,"w",encoding="utf-8") as f:
		json.dump(notes,f,ensure_ascii=False,indent=2)

def generate_id(notes):
	return 1 if not notes else notes[-1]["id"]+1

def get_current_time():
	return datetime.now().isoformat()

