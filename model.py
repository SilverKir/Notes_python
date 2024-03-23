

class NoteBook:
    def __init__(self, path: str="notes.json", separator: str=";"):
        self.notebook={}
        self.path=path
        self.separator=separator

    def open_file(self):
        with open(self.path,'r', encoding='UTF-8') as file:
            self.notebook={i: item for i, item in
                           enumerate(list(map(lambda x: x.strip().split(self.separator),file.readlines())),1)}


    def save_file(self):
        data=[]
        for contact in self.notebook.values():
            data.append(self.separator.join(contact))
        data='\n'.join(data)
        with open(self.path,'w',encoding='UTF-8') as file:
            file.write(data)


    def next_id(self):
        return (max(self.notebook) + 1) if self.notebook else 1

    def new_note(self,note: list[str]):
        self.notebook[self.next_id()]=note

    def find_note(self, word:str) -> dict[int,list[str]]:
        result={}
        for u_id, note in self.notebook.items():
            if word.lower() in str(note).lower():
                result[u_id]=note
        return result


    def change_contact(self, c_id: int, c_contact: list[str]):
        self.notebook[c_id]=c_contact


    def delete_contact(self,c_id: int)-> list[str]:
        return self.notebook.pop(c_id)