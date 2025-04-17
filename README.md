# PenCode - Collaborative Code Editor 🚀

PenCode is a real-time collaborative code editor built with Django and WebSockets that allows multiple users to work on code simultaneously. The application features syntax highlighting, code execution capabilities, and real-time collaboration.

## ✨ Features

- **🔄 Real-time Collaboration**: Multiple users can edit code simultaneously with live updates
- **👥 Online User Tracking**: See who's currently working in your coding session
- **🌈 Syntax Highlighting**: Support for multiple programming languages
- **▶️ Code Execution**: Run your code directly in the browser
- **🔐 Authentication System**: User registration and login functionality
- **👨‍💻 Group Management**: Create and join different coding groups
- **🌙 Modern UI**: Dark-themed interface optimized for coding

## 🌐 Supported Languages

- JavaScript (executed in-browser)
- Python
- Java
- C
- C++

## 🛠️ Tech Stack

- **Backend**: Django
- **Real-time Communication**: Django Channels (WebSockets)
- **Frontend**: HTML, CSS, JavaScript
- **Code Editor**: CodeMirror
- **Code Execution**: Piston API (emkc.org)

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/sujal-bansal/Code-Collab-Platform.git
cd Code-Collab-Platform
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the database:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000` in your browser.

## 📁 Project Structure

```
pencode/
├── core/                   # Main app directory
│   ├── consumers1.py       # WebSocket consumer for real-time code editing
│   ├── forms.py            # User registration and group forms
│   ├── models.py           # Database models for Code and Group
│   ├── routing.py          # WebSocket routing configuration
│   ├── urls.py             # URL configurations
│   ├── views.py            # View functions
│   └── templates/core/     # HTML templates
│       └── dark_working.html # Main code editor template
├── static/                 # Static files (CSS, JS)
└── pencode/               # Project settings directory
```

## 📝 How to Use

1. Register a new account or log in with existing credentials
2. Create a new coding group or join an existing one
3. Start coding! Your changes will automatically be visible to other users in the same group
4. Select your preferred programming language from the dropdown
5. Click the "Run Code" button to execute your code and see the output

## 🔌 WebSocket Communication

The application uses WebSockets to enable real-time collaboration:

- When a user connects, they are added to the online users list
- When a user modifies code, changes are broadcast to all connected users
- When a user disconnects, the code is saved to the database

## 🧠 Development Notes

- The project uses Django Channels for WebSocket communication
- Code execution for languages other than JavaScript is handled by the Piston API
- The UI is designed with a dark theme to reduce eye strain during coding sessions

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django Channels](https://channels.readthedocs.io/)
- [CodeMirror](https://codemirror.net/)
- [Piston API](https://github.com/engineer-man/piston)
