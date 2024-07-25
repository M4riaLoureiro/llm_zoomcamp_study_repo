import psycopg2
from psycopg2 import sql
import uuid

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(
    dbname="your_db",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)

def create_tables():
    """Create tables in the PostgreSQL database."""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS conversations (
            id UUID PRIMARY KEY,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            course VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS feedback (
            id SERIAL PRIMARY KEY,
            conversation_id UUID NOT NULL,
            feedback INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (conversation_id)
                REFERENCES conversations (id)
                ON DELETE CASCADE
        )
        """
    )
    try:
        with conn.cursor() as cursor:
            for command in commands:
                cursor.execute(command)
            conn.commit()
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")
    finally:
        conn.close()

def generate_uuid():
    return str(uuid.uuid4())

def save_conversation(question, answer, course):
    conversation_id = generate_uuid()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO conversations (id, question, answer, course)
                VALUES (%s, %s, %s, %s)
            """, (conversation_id, question, answer, course))
            conn.commit()
        return conversation_id
    except Exception as e:
        print(f"An error occurred while saving the conversation: {e}")

def save_feedback(conversation_id, feedback):
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO feedback (conversation_id, feedback)
                VALUES (%s, %s)
            """, (conversation_id, feedback))
            conn.commit()
    except Exception as e:
        print(f"An error occurred while saving the feedback: {e}")