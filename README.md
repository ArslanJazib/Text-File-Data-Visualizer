# Text-File-Data-Visualizer
This python application uses a text file containing strings and visualizes its content in bar, pie, and line graph on a web application interface created using streamlit

1: Text_File_Data_Visualizer.py has the main program for this project it uses the modules described below through different functions.

2: File Handler is a custom class that returns the content from the text file as either tokens or strings and also allows the user to get the total number of lines in a given text file.

3: Content Analyzer is a custom class that allows user to get the needed stats from the text file such as total words etc

4: Data Visualizer Initializes all the matplotlib graphs that are to be displayed on the streamlit dashboard

Once the user enters the name of their text file the graphs are reflected on streamlit in your browser
