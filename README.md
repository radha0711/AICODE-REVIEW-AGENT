🤖 AI Code Review Agent
📌 Project Overview
AI Code Review Agent is a web-based application that analyzes source code and provides intelligent feedback using Artificial Intelligence. The system helps developers improve code quality by identifying issues, security risks, and possible improvements.
This project uses a simple frontend interface and a FastAPI backend integrated with Google's Gemini AI model to generate code reviews.

🧩 Project Structure
AI-Code-Review-Agent/
│
├── index.html      # Frontend user interface
├── reviewer.py     # Backend API and AI integration
└── README.md       # Project documentation

💻 Frontend (index.html)
The frontend provides a simple and user-friendly interface.
Features:
1.Text area to paste source code
2.Run Analysis button to analyze code
3.Displays AI-generated review output
4.Modern and responsive UI design
5.Communicates with backend using API request
The frontend sends the code to the backend using a POST request and displays the review result.

⚙️ Backend (reviewer.py)
The backend is built using FastAPI and integrates with Google's Gemini AI model.
Features:
1.Receives code from frontend
2.Sends code to Gemini AI model
3.Generates intelligent code review
4.Returns review in structured format
5.Supports CORS for frontend communication

AI Review Includes:
*.Summary
*.Issues
*.Security analysis
*.Improvements
*.Final verdict

🧠 Technologies Used
1.Python
2.FastAPI
3.Google Gemini AI
4.HTML, CSS, JavaScript
5.REST API

▶️ How to Run the Project
Step 1: Install requirements
pip install fastapi uvicorn google-generativeai
Step 2: Run the backend server
uvicorn reviewer:app --reload
Step 3: Open in browser
Open:
http://127.0.0.1:8000

🎯 Purpose of the Project
This project helps developers:
1.Improve code quality
2.Detect issues quickly
3.Learn best coding practices
4.Save time in manual code reviews

🚀 Future Improvements
1.Support multiple programming languages
2.Add authentication
3.Save review history
4.Add file upload option
