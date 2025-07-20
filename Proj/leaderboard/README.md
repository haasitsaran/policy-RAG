# LeaderBoard

A full-stack web application for managing and displaying a leaderboard, built with React (frontend), Node.js/Express (backend), and MongoDB (database).

## Features
- User leaderboard with rankings
- Claim rewards functionality
- User selection and history tracking
- Responsive, modern UI
- RESTful API backend

## Folder Structure
```
leaderboard/
  backend/        # Node.js/Express API
    controllers/
    models/
    routes/
    seed/
    index.js
    package.json
  frontend/       # React app
    public/
    src/
      components/
      services/
      assets/
      App.js
      index.js
    package.json
```

## Tech Stack
- **Frontend:** React, CSS
- **Backend:** Node.js, Express
- **Database:** MongoDB (Atlas recommended)

## Getting Started

### Prerequisites
- Node.js & npm
- MongoDB Atlas account (or local MongoDB)

### Backend Setup
```bash
cd backend
npm install
# Set up .env with your MongoDB URI
npm start
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Environment Variables
- Backend: Create a `.env` file in `backend/` with:
  ```
  MONGODB_URI=your_mongodb_connection_string
  PORT=5000
  ```
- Frontend: If your API is not on localhost, update API URLs in `src/services/api.js`.

## Deployment Guide

### 1. Deploy Backend
- Recommended: [Render](https://render.com/) or [Railway](https://railway.app/)
- Set environment variables (MONGODB_URI, PORT)

### 2. Deploy Frontend
- Recommended: [Vercel](https://vercel.com/)
- Connect your GitHub repo and select the `frontend/` folder
- Update API URLs to point to your deployed backend

### 3. MongoDB
- Use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for a free cloud database
- Whitelist your backend server’s IP

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE) (add a LICENSE file if needed)

## Contact
- GitHub: [Akhil3517/LeaderBoard](https://github.com/Akhil3517/LeaderBoard.git)
- Author: Akhil 