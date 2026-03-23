python script that works

```python
import json
import threading
import urllib.request
import urllib.error
import tkinter as tk
from tkinter import scrolledtext

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "llama3"

class OllamaChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ollama Chat")
        self.root.geometry("1400x1000")
        self.root.minsize(1000, 700)

        self.messages = []

        self.chat_box = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            state="disabled",
            font=("DejaVu Sans", 18),
            padx=16,
            pady=16
        )
        self.chat_box.pack(fill="both", expand=True, padx=12, pady=(12, 8))

        bottom_frame = tk.Frame(root)
        bottom_frame.pack(fill="x", padx=12, pady=(0, 12))

        self.input_box = tk.Text(
            bottom_frame,
            height=5,
            font=("DejaVu Sans", 18)
        )
        self.input_box.pack(side="left", fill="both", expand=True)

        self.input_box.bind("<Return>", self.on_enter)
        self.input_box.bind("<Shift-Return>", self.on_shift_enter)

        self.send_button = tk.Button(
            bottom_frame,
            text="Send",
            width=12,
            height=3,
            font=("DejaVu Sans", 14),
            command=self.send_message
        )
        self.send_button.pack(side="left", padx=(12, 0), fill="y")

        self.status_var = tk.StringVar(value="Ready")
        self.status_label = tk.Label(
            root,
            textvariable=self.status_var,
            anchor="w",
            font=("DejaVu Sans", 13)
        )
        self.status_label.pack(fill="x", padx=12, pady=(0, 10))

        self.append_chat("System", f"Connected model: {MODEL}")

    def append_chat(self, speaker, text):
        self.chat_box.config(state="normal")
        self.chat_box.insert(tk.END, f"{speaker}:\n{text}\n\n")
        self.chat_box.config(state="disabled")
        self.chat_box.see(tk.END)

    def on_enter(self, event):
        if not (event.state & 0x1):
            self.send_message()
            return "break"

    def on_shift_enter(self, event):
        return None

    def set_busy(self, busy):
        if busy:
            self.send_button.config(state="disabled")
            self.status_var.set("Thinking...")
        else:
            self.send_button.config(state="normal")
            self.status_var.set("Ready")

    def send_message(self):
        user_text = self.input_box.get("1.0", tk.END).strip()
        if not user_text:
            return

        self.input_box.delete("1.0", tk.END)
        self.append_chat("You", user_text)

        self.messages.append({"role": "user", "content": user_text})
        self.set_busy(True)

        thread = threading.Thread(target=self.get_response, daemon=True)
        thread.start()

    def get_response(self):
        payload = {
            "model": MODEL,
            "messages": self.messages,
            "stream": False
        }

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            OLLAMA_URL,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=300) as response:
                result = json.loads(response.read().decode("utf-8"))
                assistant_text = result["message"]["content"].strip()

            self.messages.append({"role": "assistant", "content": assistant_text})
            self.root.after(0, lambda: self.append_chat("Assistant", assistant_text))

        except urllib.error.HTTPError as e:
            error_text = f"HTTP error {e.code}: {e.read().decode('utf-8', errors='ignore')}"
            self.root.after(0, lambda: self.append_chat("Error", error_text))
        except Exception as e:
            self.root.after(0, lambda: self.append_chat("Error", str(e)))
        finally:
            self.root.after(0, lambda: self.set_busy(False))

if __name__ == "__main__":
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 2.0)
    app = OllamaChatApp(root)
    root.mainloop()
```

(base) lea@lea-ThinkPad-P16-Gen-3:~$ nano ~/ollama_chat_gui.py
(base) lea@lea-ThinkPad-P16-Gen-3:~$ python3 ~/ollama_chat_gui.py


and then still need write .sh and so on to make it shortcut possible , i havent done that so currently can only run through command above, this is what i left hanging


## query .sh that pop up a box
```bash
#!/bin/bash

QUERY=$(zenity --entry --title="Ollama AI" --text="Ask something:")

[ -z "$QUERY" ] && exit 0

RESPONSE=$(ollama run llama3 "$QUERY")

zenity --info --text="$RESPONSE" --width=700 --height=500



```

nano ~/ollama_query.sh
chmod +x .. 

then in setting, 'bash /home/lea/ollama_query.sh'

# script works eventually (the current version)

```python
import json
import threading
import urllib.request
import urllib.error
import tkinter as tk
from tkinter import scrolledtext

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "llama3"


class OllamaChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ollama Chat")
        self.root.geometry("1400x1000")
        self.root.minsize(1000, 700)

        self.messages = []

        self.chat_box = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            state="disabled",
            font=("DejaVu Sans", 18),
            padx=16,
            pady=16
        )
        self.chat_box.pack(fill="both", expand=True, padx=12, pady=(12, 8))

        bottom_frame = tk.Frame(root)
        bottom_frame.pack(fill="x", padx=12, pady=(0, 12))

        self.input_box = tk.Text(
            bottom_frame,
            height=5,
            font=("DejaVu Sans", 18)
        )
        self.input_box.pack(side="left", fill="both", expand=True)

        self.input_box.bind("<Return>", self.on_enter)
        self.input_box.bind("<Shift-Return>", self.on_shift_enter)

        self.send_button = tk.Button(
            bottom_frame,
            text="Send",
            width=12,
            height=3,
            font=("DejaVu Sans", 14),
            command=self.send_message
        )
        self.send_button.pack(side="left", padx=(12, 0), fill="y")

        self.status_var = tk.StringVar(value="Ready")
        self.status_label = tk.Label(
            root,
            textvariable=self.status_var,
            anchor="w",
            font=("DejaVu Sans", 13)
        )
        self.status_label.pack(fill="x", padx=12, pady=(0, 10))

        self.append_chat("System", f"Connected model: {MODEL}")
        self.root.after(100, lambda: self.input_box.focus_set())

    def append_chat(self, speaker, text):
        self.chat_box.config(state="normal")
        self.chat_box.insert(tk.END, f"{speaker}:\n{text}\n\n")
        self.chat_box.config(state="disabled")
        self.chat_box.see(tk.END)

    def on_enter(self, event):
        if not (event.state & 0x1):
            self.send_message()
            return "break"

    def on_shift_enter(self, event):
        return None

    def set_busy(self, busy):
        if busy:
            self.send_button.config(state="disabled")
            self.status_var.set("Thinking...")
        else:
            self.send_button.config(state="normal")
            self.status_var.set("Ready")

    def send_message(self):
        user_text = self.input_box.get("1.0", tk.END).strip()
        if not user_text:
            self.root.after(0, lambda: self.input_box.focus_set())
            return

        self.input_box.delete("1.0", tk.END)
        self.append_chat("You", user_text)

        self.messages.append({"role": "user", "content": user_text})
        self.set_busy(True)
        self.root.after(0, lambda: self.input_box.focus_set())

        thread = threading.Thread(target=self.get_response, daemon=True)
        thread.start()

    def get_response(self):
        payload = {
            "model": MODEL,
            "messages": self.messages,
            "stream": False
        }

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            OLLAMA_URL,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=300) as response:
                result = json.loads(response.read().decode("utf-8"))
                assistant_text = result["message"]["content"].strip()

            self.messages.append({"role": "assistant", "content": assistant_text})
            self.root.after(0, lambda: self.append_chat("Assistant", assistant_text))

        except urllib.error.HTTPError as e:
            error_text = f"HTTP error {e.code}: {e.read().decode('utf-8', errors='ignore')}"
            self.root.after(0, lambda: self.append_chat("Error", error_text))
        except Exception as e:
            self.root.after(0, lambda: self.append_chat("Error", str(e)))
        finally:
            self.root.after(0, lambda: self.set_busy(False))
            self.root.after(0, lambda: self.input_box.focus_set())


if __name__ == "__main__":
    root = tk.Tk()
    root.tk.call("tk", "scaling", 2.0)
    app = OllamaChatApp(root)
    root.mainloop()
```
saved in nano ~/ollama_chat_gui.py

nano ~/launch_ollama_chat.sh
```bash
#!/bin/bash
/home/lea/miniconda3/bin/python /home/lea/ollama_chat_gui.py



```
chmod +x ...

in shortcut settings: bash /home/lea/launch_ollama_chat.sh