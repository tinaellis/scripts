# -*- coding: utf-8 -*-
"""
@author: tbird
"""
# The following program takes panopto captions that have been copied and pasted into
# a txt file named "captions.txt" and removes the timestamps and extra newlines. 
# Paragraphs are grouped by 5 sentences and separated by extra lines.
# The output is then saved to a new file "cleaned-notes.txt".

import re

def remove_timestamps(text):
    return re.sub(r'\d+:\d+\n?', '', text)

def remove_newlines(text):
    # Replace newlines with spaces and collapse multiple spaces
    return re.sub(r'\s+', ' ', text)

def restore_newlines(text):
    # Restore newlines after punctuation marks
    return re.sub(r'([.?!])\s+', r'\1\n', text)

def group_sentences(sentences, group_size=5):
    result = []
    for i in range(0, len(sentences), group_size):
        group = sentences[i:i+group_size]
        result.append(' '.join(group))
    return '\n\n'.join(result)

# Read the input file
with open('captions.txt', 'r') as file:
    content = file.read()

# Remove timestamps
cleaned_content = remove_timestamps(content)

# Remove newlines and restore newlines after punctuation marks
cleaned_content = remove_newlines(cleaned_content)
cleaned_content = restore_newlines(cleaned_content)

# Divide the sentences into paragraphs with an extra newline after every group of 5 sentences
sentences = cleaned_content.split('\n')
cleaned_content = group_sentences(sentences)

# Save the cleaned content to a new file
with open('cleaned-notes.txt', 'w') as output_file:
    output_file.write(cleaned_content)