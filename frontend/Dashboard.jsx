import React, { useState, useEffect } from 'react';
import api from './api';

function Dashboard() {
  const [notes, setNotes] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    fetchNotes();
  }, []);

  const fetchNotes = async () => {
    try {
      const response = await api.getNotes(searchTerm);
      setNotes(response.data);
    } catch (error) {
      // Handle error
    }
  };

  const handleCreateNote = async (title, content) => {
    try {
      await api.createNote(title, content);
      fetchNotes();
    } catch (error) {
      // Handle error
    }
  };

  const handleUpdateNote = async (id, title, content) => {
    try {
      await api.updateNote(id, title, content);
      fetchNotes();
    } catch (error) {
      // Handle error
    }
  };

  const handleDeleteNote = async (id) => {
    try {
      await api.deleteNote(id);
      fetchNotes();
    } catch (error) {
      // Handle error
    }
  };

  return (
    <div>
      <h1>Dashboard</h1>
      <input type="text" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} placeholder="Search notes" />
      <button onClick={() => handleCreateNote('New Note', '')}>Create Note</button>
      <ul>
        {notes.map((note) => (
          <li key={note.id}>
            <h2>{note.title}</h2>
            <p>{note.content}</p>
            <button onClick={() => handleUpdateNote(note.id, note.title, note.content)}>Edit</button>
            <button onClick={() => handleDeleteNote(note.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
