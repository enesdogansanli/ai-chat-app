import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const sendMessage = async (message) => {
  try {
    const response = await api.post('/chat/message', { content: message });
    return response.data;
  } catch (error) {
    console.error('API error:', error);
    throw error;
  }
};