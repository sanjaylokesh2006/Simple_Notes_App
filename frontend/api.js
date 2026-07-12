import axios from 'axios';

const API_URL = 'https://api.example.com/notes';

const api = {
  login: async (username, password) => {
    const response = await axios.post(`${API_URL}/login`, { username, password });
    return response.data;
  },
  getNotes: async (searchTerm) => {
    const response = await axios.get(`${API_URL}?search=${searchTerm}`);
    return response.data;
  },
  createNote: async (title, content) => {
    const response = await axios.post(API_URL, { title, content });
    return response.data;
  },
  updateNote: async (id, title, content) => {
    const response = await axios.put(`${API_URL}/${id}`, { title, content });
    return response.data;
  },
  deleteNote: async (id) => {
    await axios.delete(`${API_URL}/${id}`);
  }
};

export default api;
