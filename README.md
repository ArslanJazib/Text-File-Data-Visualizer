# Text-File-Data-Visualizer
This python application uses a text file containing strings and visualizes its content in bar, pie, and line graph on a web application interface created using streamlit

1: Text_File_Data_Visualizer.py has the main program for this project it uses the modules described below through different functions.

2: File Handler Module is a custom class that returns the content from the text file as either tokens or strings and also allows the user to get the total number of lines in a given text file.

3: Content Analyzer Module is a custom class that allows user to get the needed stats from the text file such as total words etc

4: Data Visualizer Module Initializes all the matplotlib graphs that are to be displayed on the streamlit dashboard

The program can be invoked via command line the person has to type pathToFile.Text_File_Data_Visualizer.py TextFileName.txt. Steamlit is initialized from within main python script
