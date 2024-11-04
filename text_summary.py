import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text = """Global Warming is definitely the single greatest
environmental challenge that the planet earth is facing at 
present. It is essential to understand the gravity of the
situation. The fuel which you use in order to power your homes,
cars, businesses and more is heating up the planet faster than
expected. We are recording the hottest days and decades ever.
What’s alarming is that the temperature of the earth has climbed
to the highest point it has ever been in the past 12,000 years.
It only gets worse from here if we don’t stop it now."""
def summarizer(rawdocs):

    stopwords=list(STOP_WORDS)
    #print(stopwords)

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    #print(doc)

    tokens = [token.text for token in doc]

    #print(tokens)

    word_freq={}

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
        word_freq[word]= word_freq[word]/max_freq

    #print(word_freq)

    sent_tokens = [sent for sent in doc.sents]

    #print(sent_tokens)

    sent_scores= {}

    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
                    #print(sent_scores)

    select_len = int(len(sent_tokens) * 0.3)

    #print(select_len)

    summary= nlargest(select_len, sent_scores, key = sent_scores.get)
    #print(summary)
    final_summary= [word.text for word in summary]
    summary =' ' .join(final_summary)
    #print(text)
    #print(summary)
    #print("Length of orignal text", len(text.split(' ')))
    #print("Length of summary text", len(summary.split(' ')))

    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))