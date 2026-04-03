import typer
from service import add_note,list_notes,delete_note 
app=typer.Typer()
@app.command()
def add(text:str):
	add_note(text)
	print("заметка добавлена")
@app.command()
def list():
	notes=list_notes()
	for n in notes:
		print(f'{n["id"]}:{n["text"]}')
@app.command()
def delete(note_id:int):
	delete_note(note_id)	
	print("заметка удалена")
if __name__=="__main__":
	app()
