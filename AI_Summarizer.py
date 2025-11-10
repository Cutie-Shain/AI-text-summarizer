import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import heapq
import tkinter as tk
from tkinter import scrolledtext

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text():
    text = text_input.get("1.0", tk.END)
    if not text.strip():
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter some text to summarize!")
        return

    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    freqTable = {}
    for word in words:
        word = word.lower()
        if word not in stopWords and word.isalnum():
            freqTable[word] = freqTable.get(word, 0) + 1

    sentences = sent_tokenize(text)
    sentenceValue = {}
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                sentenceValue[sentence] = sentenceValue.get(sentence, 0) + freq

    summary_sentences = heapq.nlargest(3, sentenceValue, key=sentenceValue.get)
    summary = " ".join(summary_sentences)

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, summary)

# GUI setup
root = tk.Tk()
root.title("AI Text Summarizer 🧠")
root.geometry("700x500")
root.configure(bg="#f5f5f5")

title_label = tk.Label(root, text="AI Text Summarizer", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=("Arial", 11))
text_input.pack(padx=10, pady=10)

summarize_button = tk.Button(root, text="Summarize Text", command=summarize_text, font=("Arial", 12, "bold"), bg="#0078D7", fg="white")
summarize_button.pack(pady=10)

result_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=8, font=("Arial", 11))
result_box.pack(padx=10, pady=10)

root.mainloop()
