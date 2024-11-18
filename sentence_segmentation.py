import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def segment_sentences(text):
    # Process the text with spaCy
    doc = nlp(text)
    # Extract sentences
    sentences = [sent.text for sent in doc.sents]
    return sentences

if __name__ == "__main__":
    # Take user input
    text_input = input("Enter a paragraph of text: ")
    sentences = segment_sentences(text_input)

    # Display segmented sentences
    print("\nSegmented Sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")
