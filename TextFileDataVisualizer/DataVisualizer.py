import streamlit as st
import matplotlib.pyplot as plt

class DataVisualizer(object):
    """This class creates an object that manages the graphs for web application"""
    
    def __init__(self,analyzedContent):
        self.analyzedContent = analyzedContent

    def generate_bar_graph(self):
        # Since we are only taking input from one file
        # x-axis is defined statically here
        numberOfFiles = [1,2,3,4,5,6,7,8,9,10]
        totalWordsInFile = [self.analyzedContent.get('totalNumberOfWords'),0,0,0,0,0,0,0,0,0]

        fig, ax = plt.subplots()
        ax.bar(numberOfFiles,totalWordsInFile)
        plt.xlabel("Files")
        plt.ylabel("Words")
        plt.title("Total words in file")
        st.write("Total Words In Files: "+str(self.analyzedContent.get('totalNumberOfWords')))
        st.pyplot(fig)

    def generate_least_bar_graph(self):
        leastUsedWords = self.analyzedContent.get('totalLeastUsedWords')
        words = []
        for word in leastUsedWords:
            words.append(word[0])

        fig, ax = plt.subplots()
        ax.bar([0,1,2,3,4,5,6,7,8,9],words)
        plt.xlabel("Count")
        plt.ylabel("Words")
        plt.title("10 Least Used Words In Text File")
        st.pyplot(fig)

    def generate_pie_graph(self):
        data = self.analyzedContent.get('frequencyOfWords')
        words = data.keys()
        counts = data.values()
        
        fig, ax = plt.subplots()
        ax.pie(counts, labels = None)
        plt.title("Frequency of word in file")
        fig.legend(loc=7, prop={'size': 3}, labels=words)
        fig.subplots_adjust(right=0.75)
        st.pyplot(fig)


    def generate_line_graph(self):
        totalNouns = self.analyzedContent.get('frequencyOfNouns')
        totalNouns = list(totalNouns.values())
        
        totalAdjectives = self.analyzedContent.get('frequencyOfAdjectives')
        totalAdjectives = list(totalAdjectives.values())
        
        fig, ax = plt.subplots()
        ax.plot([0,1],[0,len(totalNouns)],label = "Nouns")
        ax.plot([0,1],[0,len(totalAdjectives)],label = "Adjectives")
        plt.legend()
        plt.title("Number of nouns and adjectives in the file")
        st.pyplot(fig)
        
    def generate_line_graph_per_word(self):
        totalNouns = self.analyzedContent.get('frequencyOfNouns')        
        totalAdjectives = self.analyzedContent.get('frequencyOfAdjectives')
        
        fig, ax = plt.subplots()

        # Iterating through each noun and adjective in dictionary
        # and plotting its respective line
        for noun in totalNouns:
            ax.plot([0,1],[0,totalNouns[noun]],label = noun)

        for adjective in totalAdjectives:
            ax.plot([0,1],[0,totalAdjectives[adjective]],label = adjective)
        
        fig.legend(loc=7)
        fig.subplots_adjust(right=0.75)
        plt.title("Occurance of indiviual nouns and adjectives in the text file")
        st.pyplot(fig)
