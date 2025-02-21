# AI Chat Application

A web-based chatbot-AI application that runs locally. Built with React for frontend and FastAPI for backend.

## Features

- Web-based user interface
- Real-time messaging
- AI model integration
- Local database support

## Technology Stack

### Frontend
- React.js
- Tailwind CSS
- Axios

### Backend
- Python
- FastAPI
- SQLite
- AI Model (Deepseek/LLama2 etc.)

## Installation

### Prerequisites
- Python 3.9+
- Node.js 18+
- npm or yarn

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv myvenv

# Activate virtual environment
# For Windows:
myvenv\Scripts\activate
# For Linux/Mac:
source myvenv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload --port 8000

```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the application
npm start
```

## Usage

1. Start the backend (port 8000)
2. Start the frontend (port 3000)
3. Navigate to http://localhost:3000 in your browser

## Project Structure

```bash
ai-chat-app/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.js
│   └── package.json
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   └── main.py
│   └── requirements.txt
└── README.md
```

## Development

### API Endpoints

* ```POST /api/chat/message```: Send a message
* ```GET /api/chat/history```: Get chat history
* ```POST /api/auth/login```: User login
* ```POST /api/auth/register```: User registration

### Available Scripts

Frontend:

```bash
# Run development server
npm start

# Build for production
npm run build

# Run tests
npm test
```

Backend:

```bash
# Run development server
uvicorn app.main:app --reload --port 8000

# Run tests
pytest
```

### Environment Variables

Frontend:

```bash
REACT_APP_API_URL=http://localhost:8000
```

Backend:

```bash
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=your_secret_key
```

## Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'feat: Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request