import os
import csv
import random

def clear_output_file(file_path):
    try:
        with open(file_path, 'w', newline='') as csvfile:
            pass  # Opening in write mode and immediately closing clears the file
        print(f"Cleared contents of {file_path}")
    except IOError as e:
        print(f"Error clearing {file_path}: {e}")

def add_header(file_path):
    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            writer.writerow(['question', 'answer', 'user_answer'])
        print(f"Added header to {file_path}")
    except IOError as e:
        print(f"Error adding header to {file_path}: {e}")

def is_header_row(row):
    return row == ['question', 'answer', 'user_answer']

def read_all_questions(topics_folder):
    all_questions = []
    topic_files = [f for f in os.listdir(topics_folder) if f.endswith('.csv')]
    
    for topic_file in topic_files:
        topic_name = os.path.splitext(topic_file)[0]
        file_path = os.path.join(topics_folder, topic_file)
        
        try:
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter='|')
                first_row = next(reader, None)
                
                if first_row and not is_header_row(first_row):
                    all_questions.append((topic_name, *first_row))
                
                for row in reader:
                    all_questions.append((topic_name, *row))
            
            print(f"Read {len(all_questions)} questions from {topic_file}")
        except IOError as e:
            print(f"Error reading file {topic_file}: {e}")
    
    return all_questions

def shuffle_questions():
    topics_folder = 'topics'
    output_file = 'questions.csv'
    
    clear_output_file(output_file)
    add_header(output_file)
    
    all_questions = read_all_questions(topics_folder)
    random.shuffle(all_questions)
    
    try:
        with open(output_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            for question in all_questions:
                writer.writerow(question[1:])  # Exclude the topic name
        print(f"Added {len(all_questions)} questions to {output_file}")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")

if __name__ == "__main__":
    shuffle_questions()
    print("All questions have been shuffled and written to questions.csv")