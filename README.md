# QuestionShuffler
Python script to shuffle test questions on different topics for maximizing learning experience

#### The csv file question format:
```
question|answer|user_answer
Question #1|False|False
Question #2|True|
Question #3|False|
Question #4|True|
```
You can use one of the example prompts (prompt templates) below to have AI generate the questions. 

I highly recommend Claude-3.5-Sonnet on https://claude.ai/ or ChatGPT-4o-Classic on https://chatgpt.com/g/g-YyyyMT9XH-chatgpt-classic.

#### English version:
```
You are demanding examiner for 'Machine Learning' subject.
Your goal is to minimise the likelihood of passing the exam.
Your function is to prepare exam test with minimum pass rate.
Your task is to generate true/false questions based on the following sources:
- "An Introduction to Statistical Learning";
- "The Elements of Statistical Learning: Data Mining, Inference, and Prediction";
- "Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow".
Set familiarity level to expert.
Set maximum difficulty level.
Each question is extremely challenging, tricky, non-obvious, unique.
Questions mustnt be repetitions or paraphrases of other questions already present in conversation. 
Each question will go into a `*.csv` file with the format "Question|True Answer|User Answer", so each question is formatted as: 
"{index}. ({Source}). {Question}.|{answer}|".
The topic is "CARTs and Random Forests".
Prepare at least 100 questions on topic. There must be no less than 100 questions in total. There must be 50 questions with `True` answer and 50 questions with `False`. Start generating from "question|answer|user_answer".
```

#### Polish version:

```
Jesteś wymagającym egzaminatorem przedmiotu "Uczenie maszynowe".
Celem jest zminimalizowanie prawdopodobieństwa zdania egzaminu.
Twoją funkcją jest układanie po polsku testu egzaminacyjnego o minimalnej zdawalności.
Twoim zadaniem jest układanie pytań prawda/fałsz na podstawie następujących źródeł:
- "An Introduction to Statistical Learning";
- "The Elements of Statistical Learning: Data Mining, Inference, and Prediction";
- "Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow".
Poziom zaawansowania ekspert.
Poziom trudności maksymalny.
Każde pytanie jest wyjątkowo trudne, podchwytliwe, nieoczywiste, niepowtarzalne.
Pytania nie mogą być powtórzeniami ani parafrazami dotychczas sformułowanych w konwersacji innych pytań. 
Każde pytanie trafi do pliku `*.csv` o formacie `Pytanie|Prawdziwa odpowiedź|Odpowiedź użytkownika`, więc każde pytanie sformatowane jest jako: "{index}. ({źródło}). {Pytanie}.|{odpowiedź}|".
Tematem jest "Maszyny wektorów nośnych [Support Vecor machines (SVM)]".
Przygotuj co najmniej 100 pytań. Musi być łącznie nie mniej niż 100 pytań. Zacznij generowanie od "question|answer|user_answer".
```