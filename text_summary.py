import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """Bank Management System Abstract: The bank management system project is a program that keeps track
of a client’s bank account. This project demonstrates the operation of a
banking account system and covers the essential functions of bank
management software. It develops a project for resolving a customer’s
financial applications in a banking environment to meet the needs of an end
banking user by providing multiple ways to complete banking chores.
Additionally, this project is to provide additional features to the user’s
workspace that are not available in a traditional banking project. The project’s
bank management system is built on cutting-edge technologies. This project’s
main goal is to create software for a bank account management system. This
project was designed to make it simple and quick to complete previously
impossible processes with manual systems which are now possible with this
software.
Project Description: The Bank Management System (BMS) is a web-based
tool that is used to reimburse financial institutions for services rendered to the
Bureau of the Fiscal Service. In addition, BMS provides analytical tools for
reviewing and approving salaries, budgets, and outflows.
Project Objectives: The goal of the bank management system project is to
create an organic and optimal software of interaction between the various
banking components. This is to maximize the profit of the banking
mechanism. The implementation of competent bank management procedures
is significantly responsible for the successful optimization of the bank’s
productivity and activities.
The project’s main goal is to create an online banking system for banks. All
banking work is done manually in the current system. To withdraw or deposit
money, the user must go to the bank. Today, it is also hard to find account
information for people who have accounts in the banking system """

#print(text)

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    #print(stopwords)

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    #print(doc)
    tokens = [token.text for token in doc]
    #print(tokens)

    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    #print(word_freq)

    max_freq = max(word_freq.values())
    #print(max_freq)

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    #print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    #print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    #print(sent_scores)

    select_len = int(len(sent_tokens)*0.3)
    #print(select_len)

    summary = nlargest(select_len,sent_scores,key = sent_scores.get)
    #print(summary)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    #print(text)
    #print(summary)
    #print("Length of original text",len(text.split(' ')))
    #print("Length of summary text",len(summary.split(' ')))

    return summary, doc,len(rawdocs.split(' ')),len(summary.split(' '))