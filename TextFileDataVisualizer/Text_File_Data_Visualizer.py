import os
import sys
import streamlit as st
from streamlit import runtime
from streamlit.web import cli as stcli

# Custom Classes
import FileHandler as fileLibrary
import ContentAnalyzer as analyzerLibrary
import DataVisualizer as visualizerLibrary

# This function takes the content from a text file
def get_file_content(fileHandlerObj):
    # Get Content function returns tokenized string when True flag is passed
    fileContent = fileHandlerObj.get_content(True)
    return fileContent

# This function uses text file content and return a dictionary to web application
def get_analyzed_content(analyzerObj,fileHandlerObj):
    # Get number of words in the text file
    totalNumberOfWords = analyzerObj.get_word_count()

    # Get frequency of words in the text file
    frequencyOfWords = analyzerObj.get_word_frequency()

    # Get freqency of nouns
    frequencyOfNouns = analyzerObj.get_noun_frequency()

    # Get freqency of adjectives
    frequencyOfAdjectives = analyzerObj.get_adjectives_frequency()

    # Get total number of lines

    totalNumberOfLines = fileHandlerObj.get_total_lines()
    st.write("Total Lines In File "+str(totalNumberOfLines))


    # Get 10 least used words
    totalLeastUsedWords = analyzerObj.get_least_used_words()

    # A dictionary of analyzed content
    analyzedContent = {
        "totalNumberOfWords": totalNumberOfWords,
        "frequencyOfWords": frequencyOfWords,
        "frequencyOfNouns": frequencyOfNouns,
        "frequencyOfAdjectives": frequencyOfAdjectives,
        "totalNumberOfLines": totalNumberOfLines,
        "totalLeastUsedWords": totalLeastUsedWords
    }

    return analyzedContent

# This function uses text file content and intalizes streamlit content
def initialize_web_app_content(visualizerObj):
    visualizerObj.generate_bar_graph()

    visualizerObj.generate_pie_graph()

    visualizerObj.generate_line_graph()

    visualizerObj.generate_line_graph_per_word()

    visualizerObj.generate_least_bar_graph()

def main():
    fileName = input("Please enter your text file name ending with .txt: ")

    # Streamlit Header
    st.title("Text File Data Analysis Dashboard")

    # Creaing File Handler Object
    fileHandlerObj = fileLibrary.FileHandler(fileName)

    fileContent = get_file_content(fileHandlerObj)

    # Creaing and intializing Content Visualizer Object
    analyzerObj = analyzerLibrary.ContentAnalyzer(fileContent)

    analyzedContent = get_analyzed_content(analyzerObj,fileHandlerObj)

    # Creaing and intializing Data Visualizer Object For Web Interface
    visualizerObj = visualizerLibrary.DataVisualizer(analyzedContent)

    initialize_web_app_content(visualizerObj)
    
    os.system('pause')

if __name__ == "__main__":
    if runtime.exists():
        a = None
    else:
        sys.argv = ["streamlit", "run", "Text_File_Data_Visualizer.py"]
        sys.exit(stcli.main())

    main()
