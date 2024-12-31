import sqlite3

def get_user_preferences(user_id):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('SELECT preferences FROM users WHERE id=?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0].split(',') if result else []

def save_user_preferences(user_id, preferences):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO users (id, preferences) VALUES (?, ?)', 
              (user_id, ','.join(preferences)))
    conn.commit()
    conn.close()

def update_preferences(user_id, new_preferences):
    preferences = get_user_preferences(user_id)
    preferences.extend(new_preferences)
    save_user_preferences(user_id, preferences)
