from storage import load_notes,save_notes,generate_id,get_current_time



def add_note(note):
	notes=load_notes()
	new_note={"id":generate_id(notes),"text":note}
	notes.append(new_note)
	save_notes(notes)

def list_notes():
	return load_notes()
def delete_note(note_id):
	notes=load_notes() 
	notes=[n for n in notes if n["id"]!=note_id]
	save_notes(notes)
