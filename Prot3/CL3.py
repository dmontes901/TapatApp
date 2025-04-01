import requests
import tkinter as tk
from tkinter import messagebox

class DAOUser:
    token_cache = {}
    
    @staticmethod
    def getUserByCredentials(username, password):
        if username in DAOUser.token_cache:
            return DAOUser.token_cache[username]
        
        response = requests.post("http://localhost:10050/prototip2/login", json={"username": username, "password": password})

        if response.status_code == 200:
            userData = response.json()
            DAOUser.token_cache[username] = userData
            return userData
        else:
            return None

class DAOChild:
    @staticmethod
    def getChildren(user_id, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"http://localhost:10050/prototip2/children/{user_id}", headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login App")
        self.root.geometry("400x300")
        
        self.create_login_screen()
    
    def create_login_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        
        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        
        tk.Button(self.root, text="Login", command=self.login).pack()
    
    def create_main_screen(self, user_data, children):
        self.clear_screen()
        
        tk.Label(self.root, text=f"Welcome, {user_data['username']}!", font=("Arial", 14)).pack()
        tk.Label(self.root, text=f"Email: {user_data['email']}").pack()
        tk.Label(self.root, text=f"Token: {user_data['token']}").pack()
        
        tk.Label(self.root, text="Children Info:", font=("Arial", 12)).pack()
        
        if children:
            for child in children:
                tk.Label(self.root, text=f"ID: {child['id']}, Name: {child['child_name']}, Sleep Avg: {child['sleep_average']}").pack()
        else:
            tk.Label(self.root, text="No children associated.").pack()
        
        tk.Button(self.root, text="Logout", command=self.create_login_screen).pack()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        response = requests.post("http://localhost:10050/prototip2/login", json={"username": username, "password": password})
        
        if response.status_code == 200:
            user_data = response.json()
            token = user_data['token']
            
            headers = {"Authorization": f"Bearer {token}"}
            children_response = requests.get(f"http://localhost:10050/prototip2/children/{user_data['id']}", headers=headers)
            
            children = children_response.json() if children_response.status_code == 200 else []
            self.create_main_screen(user_data, children)
        else:
            messagebox.showerror("Error", "Invalid credentials")
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()