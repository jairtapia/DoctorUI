import customtkinter as ctk

class Box(ctk.CTkScrollableFrame):
    def __init__(self, master, text, selected, data, horizontal_scroll=False, **kwargs):
        super().__init__(master, **kwargs)
        self.active = selected
        self.topic = text
        self.data = data
        self.configure(fg_color="#ffffff", corner_radius=10)
        self.label = ctk.CTkLabel(self, text=self.topic, text_color="black", font=("Arial", 16))
        self.grid_columnconfigure(0, weight=1)
        self.label.grid(row=0, column=0, padx=10, pady=10)  # Cambiado a grid
        if horizontal_scroll:
            self.grid(row=1, column=0, sticky="nsew")  # Cambiado a grid
        else:
            self.grid(row=1, column=0, sticky="nsew")  # Cambiado a grid
        self.GenerateValues()
    
    def GenerateValues(self):
        self.check_vars = []
        if self.data is not None:
            for index, item in enumerate(self.data):
                frame_checkbox = ctk.CTkFrame(self, fg_color="#e0e0e0")  
                frame_checkbox.grid(row=index + 1, column=0, sticky="ew", padx=10, pady=5)  # Usar grid aquí
                if self.active:
                    if any(item['name'] == active_item['name'] for active_item in self.active):
                        var = ctk.BooleanVar(value=True)
                    else:
                        var = ctk.BooleanVar(value=False)
                else:
                    var = ctk.BooleanVar(value=False) 
                self.check_vars.append(var)  
                checkbox = ctk.CTkCheckBox(frame_checkbox, text=item['name'], variable=var, text_color="black", command=self.getList)
                checkbox.grid(padx=10, pady=5)
        
    def getList(self):
        selected_items = [item for i, item in enumerate(self.data) if self.check_vars[i].get()]
        print("Seleccionados:", selected_items)  

    def getValuesIDs(self):
        return [item['id'] for i, item in enumerate(self.data) if self.check_vars[i].get()]
    
    def getValueNames(self):
        return [item['name'] for i, item in enumerate(self.data) if self.check_vars[i].get()]

if __name__ == "__main__":
    import customtkinter as ctk
    root = ctk.CTk()
    app = Box(master=root, text="Signos", selected=[{'id':1,'name':'tos'},{'id':2,'name':'daniela'}], data=[{"id": 1, "name": 'tos'}, {"id": 2, "name": 'daniela'}, {"id": 3, "name": 'amor'}, {"id": 4, "name": 'fatima'}, {"id": 5, "name": 'las amo'}])
    app.grid(sticky="nsew")
    print(app.getValuesIDs())
    root.mainloop()


