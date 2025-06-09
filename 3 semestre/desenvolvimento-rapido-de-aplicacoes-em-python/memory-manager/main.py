
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

# Database initialization
def init_db():
    conn = sqlite3.connect('memories.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            image TEXT,
            emotion TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Database helper functions
def get_db_connection():
    conn = sqlite3.connect('memories.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_memory(memory_id):
    conn = get_db_connection()
    memory = conn.execute('SELECT * FROM memories WHERE id = ?', (memory_id,)).fetchone()
    conn.close()
    return memory

# Routes
@app.route('/')
def index():
    conn = get_db_connection()
    memories = conn.execute('SELECT * FROM memories ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', memories=memories)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']
        emotion = request.form['emotion']
        
        if not title or not emotion:
            flash('Title and emotion are required!')
            return render_template('create.html')
        
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO memories (title, description, image, emotion) VALUES (?, ?, ?, ?)',
            (title, description, image, emotion)
        )
        conn.commit()
        conn.close()
        
        flash('Memory created successfully!')
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/edit/<int:memory_id>', methods=['GET', 'POST'])
def edit(memory_id):
    memory = get_memory(memory_id)
    
    if memory is None:
        flash('Memory not found!')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']
        emotion = request.form['emotion']
        
        if not title or not emotion:
            flash('Title and emotion are required!')
            return render_template('edit.html', memory=memory)
        
        conn = get_db_connection()
        conn.execute(
            'UPDATE memories SET title = ?, description = ?, image = ?, emotion = ? WHERE id = ?',
            (title, description, image, emotion, memory_id)
        )
        conn.commit()
        conn.close()
        
        flash('Memory updated successfully!')
        return redirect(url_for('index'))
    
    return render_template('edit.html', memory=memory)

@app.route('/delete/<int:memory_id>', methods=['POST'])
def delete(memory_id):
    memory = get_memory(memory_id)
    
    if memory is None:
        flash('Memory not found!')
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    conn.execute('DELETE FROM memories WHERE id = ?', (memory_id,))
    conn.commit()
    conn.close()
    
    flash('Memory deleted successfully!')
    return redirect(url_for('index'))

@app.route('/view/<int:memory_id>')
def view(memory_id):
    memory = get_memory(memory_id)
    
    if memory is None:
        flash('Memory not found!')
        return redirect(url_for('index'))
    
    return render_template('view.html', memory=memory)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
