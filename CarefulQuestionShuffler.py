import os
import csv
import random
import shutil

def clear_output_file(file_path):
    try:
        with open(file_path, 'w', newline='') as csvfile:
            pass
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

def create_duplicated_folder(source_folder, dest_folder):
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
    shutil.copytree(source_folder, dest_folder)
    print(f"Created duplicated folder: {dest_folder}")

def get_available_files(folder):
    return [f for f in os.listdir(folder) if f.endswith('.csv') and os.path.getsize(os.path.join(folder, f)) > 0]

def sample_question(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        first_row = next(reader, None)
        if first_row and not is_header_row(first_row):
            questions = [first_row]
        else:
            questions = []
        questions.extend(list(reader))
    
    if not questions:
        return None, []

    sampled_question = random.choice(questions)
    questions.remove(sampled_question)

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(questions)

    return sampled_question, questions

def shuffle_questions():
    topics_folder = 'topics'
    duplicated_folder = 'duplicated'
    output_file = 'questions.csv'

    create_duplicated_folder(topics_folder, duplicated_folder)
    clear_output_file(output_file)
    add_header(output_file)

    all_questions = []
    last_topic = None
    consecutive_count = 0

    while True:
        available_files = get_available_files(duplicated_folder)
        if not available_files:
            break

        if len(available_files) == 1 or (last_topic is None or consecutive_count < 2):
            file_to_sample = random.choice(available_files)
        else:
            file_to_sample = random.choice([f for f in available_files if not f.startswith(last_topic)])

        file_path = os.path.join(duplicated_folder, file_to_sample)
        sampled_question, remaining_questions = sample_question(file_path)

        if sampled_question:
            all_questions.append(sampled_question)
            current_topic = os.path.splitext(file_to_sample)[0]

            if current_topic == last_topic:
                consecutive_count += 1
            else:
                consecutive_count = 1
                last_topic = current_topic

        if not remaining_questions:
            os.remove(file_path)

    random.shuffle(all_questions)

    try:
        with open(output_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            writer.writerows(all_questions)
        print(f"Added {len(all_questions)} questions to {output_file}")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")

    # Remove the duplicated folder after processing
    shutil.rmtree(duplicated_folder)
    print(f"Removed duplicated folder: {duplicated_folder}")

if __name__ == "__main__":
    shuffle_questions()
    print("All questions have been shuffled and written to questions.csv")