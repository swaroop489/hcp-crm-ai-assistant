import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const chatWithAgent = async (message) => {
  try {
    const response = await api.post('/chat/', { message });
    return response.data;
  } catch (error) {
    console.error('Error talking to AI Agent:', error);
    throw error;
  }
};

export default api;
