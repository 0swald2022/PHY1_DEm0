# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:28:26 2025

@author: Oswald Roberts
"""

import streamlit as st
import pandas as pd
import io
import MyAppFunctions as MAF
from docx import Document

# Page title
st.title(":red[PHYSICS] FOUNDATION :red[PRACTICALS]")
st.subheader("**First :red[Year] Students**")

# University entrance page
st.image("University-of-Fort-Hare.jpg",caption = "Alice Branch entrance")

# University logo on the right corner
st.logo("UFHlogo.png", size = "large")

# Welcoming message
st.write("Tread carefully because wherever light strikes there are always shadows to be found as well")

# Navigator on the side with radio selction or buttons
# side bar menu
st.sidebar.title(":red[Navigation]")

# Options in the sidebar to chose and navigate to
options_navigate = ["Demonstrator Profile", "Practicals 1st Semester","Practicals 2nd Semester", "Contact details","About author(s)"]

# Navigates using pill selection
menu = st.sidebar.radio("Select your interest:", options_navigate)


# Selection options
# First selection choice
if menu == "Demonstrator Profile":
    
    st.header(":red[Demonstrator] Profile", divider = "red")
    st.sidebar.header(":red[Profile] Options")

    # Collect basic information
    name = "Mr. Oswald Roberts"
    field = "Physics (Material Science)"
    institution = "University of Fort Hare"
    study_level = "PhD Candidate"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Study:** {field}")
    st.write(f"**Institution:** {institution}")
    st.write(f"**Study level:** {study_level}")
    
    
# Second selection choice
elif menu == "Practicals 1st Semester":
    
    st.header(":red[Practicals] First :red[Semester]", divider = "red")
    st.sidebar.header(":red[Practicals]")
    
    # Side bar for the practical names in the first Semester
    # The first number represent the semester number, 1 for first semester
    prac_11 = "Measurement 1" 
    prac_12 = None
    prac_13 = None
    prac_14 = None
    prac_15 = None
    
    # list to store the practicals
    prac_1_semester = [prac_11, prac_12, prac_13, prac_14, prac_15]
    
    # select box to select the practical you want to view
    practicals_first_semester = st.sidebar.selectbox(
        "Choose a practical to view",prac_1_semester )
    
    # What happens after selecting the practical
    # Create tabs for information under practicals
    alltabs = ["Marks", "Memorundum","Summary", "Key skills learned", "Common Errors", "Final Remarks"]
    tab11, tab12, tab13, tab14, tab15, tab16 = st.tabs(alltabs) # first number represent the semester
    
    # What happens when you choose a practical from the select box
    if practicals_first_semester == prac_11: # If the first practical is selected
        
        # Use with notation to add/insert elements into each tab
        with tab11:
            
            st.header(":red[Practical] Marks", divider = "red")
            
            # Text input for the user to access their marks
            user1 = str(st.text_input("Enter your student number"))
            
            # if nothing is entered
            if user1 == "":
                
                st.write("Student number not entered")
             
            # When a string is entered
            elif len(user1) != 0:
                
                data = pd.read_excel("Practicals_First_Semester/Prac_1/Dummy_data.xlsx",dtype={'STUDENT_NUMBER': str})
                
                # check who entered the student number
                if user1 == "Sikhonza1001001":
                    
                    # If Sikhonza entered their surname along with unique code
                    st.success("WELCOME Mr. :red[**SIKHONZA**]")
                    st.write("Here are the student records")
                    st.dataframe(data)
                    
                    st.write("Click on the buttons below to download the data in your preferred format.")
                    
                    # Create download buttons
                    col1, col2, col3 = st.columns(3)  # Arrange buttons horizontally
                    
                    with col1:
                        st.download_button(label=" Download Excel",data = MAF.to_excel(data),
                                           file_name="Practical_1.xlsx",
                                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                        
                    with col2:
                        st.download_button(label=" Download Word",data = MAF.to_word(data),
                                           file_name="Practical_1.docx",
                                           mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                        
                    with col3:
                        st.download_button(label=" Download Text",data= MAF.to_text(data),
                                           file_name="Practical_2.txt", mime="text/plain")
                        
                                        
                elif user1 == "Roberts73":
                    
                    st.success("WELCOME Mr. :red[**ROBERTS**]")
                    st.write("Here are the student records")
                    st.dataframe(data)
                    
                # when an incorrect student number was entered
                elif data[data['STUDENT_NUMBER'] == user1].empty:
                    
                    st.warning(f"Student number '{user1}' does **NOT** exist in the record. check with your demonstrator")
                
                else:
                    record = MAF.check_studentnumber(data, user1)
                    st.success(f" Here is your record {user1} for Practical 1")
                    
                    st.dataframe(record)
            
        with tab12:
            
            st.header(":red[Memorundum]", divider = "red")
            
            doc_path = "Practicals_First_Semester/Prac_1/Memo1.docx"
            content = MAF.extract_list_items_word(doc_path)
            
            # Displaying the aim, apparatus, theory of the experiment in word
            if content:
                
                for item in content:
                    
                    st.write(f"- {item}")
                st.image("Practicals_First_Semester/Prac_1/equation1.png", caption = "equation 1")
            
            # Displaying Experiment data table
            excel_path = "Practicals_First_Semester/Prac_1/experimentdatatable.xlsx"
            experimentdf = pd.read_excel(excel_path, dtype = {"h (cm)": float, "D (cm)": float, "m (g)": float})
            st.subheader("**Experiment Data**")
            st.dataframe(experimentdf)
            
        with tab13:
            
            st.header(":red[Summary] of :red[the] Practical", divider = "red")
            
            doc_path = "Practicals_First_Semester/Prac_1/summary.docx"
            content = MAF.extract_list_items_word(doc_path)
            
            if content:
                
                for item in content:
                    
                    st.write(f"- {item}")
                st.subheader("Equations")
                st.image("Practicals_First_Semester/Prac_1/equation1.png", caption = "equation 1")
            
        with tab14:
            
            st.header(":red[Key] Skills :red[Students] Learned", divider = "red")
        
        
        with tab15:
            
            st.header(":red[Common] Errors :red[Students] Made", divider = "red")
            
            
        with tab16:
            
            st.header(":red[Final] Remark", divider = "red")
        
      # if the second practical is selected  
    elif practicals_first_semester == prac_12:
        
        # Use with notation to add/insert elements into each tab
        with tab11:
            
            st.header(":red[Practical] Marks", divider = "red")
            
            # Text input for the user to access their marks
            user1 = st.text_input("Enter your student number")
            # data = pd.read_excel("Dummy_data.xlsx")
            
            
            if user1 == "":
                
                st.write("Student number not entered")
                
            elif len(user1) != 0:
                
                st.subheader(f"Student number Entered: :red[{user1}]")
            
           
            
        with tab12:
            
            st.header(":red[Memorundum]", divider = "red")
            
            
        with tab13:
            
            st.header(":red[Summary] of :red[the] Practical", divider = "red")
            
            
        with tab14:
            
            st.header(":red[Key] Skills :red[Students] Learned", divider = "red")
        
        
        with tab15:
            
            st.header(":red[Common] Errors :red[Students] Made", divider = "red")
            
            
        with tab16:
            
            st.header(":red[Final] Remark", divider = "red")
     
    # if the third practical is selected
    elif practicals_first_semester == prac_13:
        
        # Use with notation to add/insert elements into each tab
        with tab11:
            
            st.header(":red[Practical] Marks", divider = "red")
            
            # Text input for the user to access their marks
            user1 = st.text_input("Enter your student number")
            # data = pd.read_excel("Dummy_data.xlsx")
            
            
            if user1 == "":
                
                st.write("Student number not entered")
                
            elif len(user1) != 0:
                
                st.subheader(f"Student number Entered: :red[{user1}]")
            
           
            
        with tab12:
            
            st.header(":red[Memorundum]", divider = "red")
            
            
        with tab13:
            
            st.header(":red[Summary] of :red[the] Practical", divider = "red")
            
            
        with tab14:
            
            st.header(":red[Key] Skills :red[Students] Learned", divider = "red")
        
        
        with tab15:
            
            st.header(":red[Common] Errors :red[Students] Made", divider = "red")
            
            
        with tab16:
            
            st.header(":red[Final] Remark", divider = "red")
        
       
    # if the fourth practical is selected
    elif practicals_first_semester == prac_14:
        
        # Use with notation to add/insert elements into each tab
        with tab11:
            
            st.header(":red[Practical] Marks", divider = "red")
            
            # Text input for the user to access their marks
            user1 = st.text_input("Enter your student number")
            # data = pd.read_excel("Dummy_data.xlsx")
            
            
            if user1 == "":
                
                st.write("Student number not entered")
                
            elif len(user1) != 0:
                
                st.subheader(f"Student number Entered: :red[{user1}]")
            
           
            
        with tab12:
            
            st.header(":red[Memorundum]", divider = "red")
            
            
        with tab13:
            
            st.header(":red[Summary] of :red[the] Practical", divider = "red")
            
            
        with tab14:
            
            st.header(":red[Key] Skills :red[Students] Learned", divider = "red")
        
        
        with tab15:
            
            st.header(":red[Common] Errors :red[Students] Made", divider = "red")
            
            
        with tab16:
            
            st.header(":red[Final] Remark", divider = "red")
        
        
    # if the fifth practical is selected   
    elif practicals_first_semester == prac_15:
        
      # Use with notation to add/insert elements into each tab
      with tab11:
          
          st.header(":red[Practical] Marks", divider = "red")
          
          # Text input for the user to access their marks
          user1 = st.text_input("Enter your student number")
          # data = pd.read_excel("Dummy_data.xlsx")
          
          
          if user1 == "":
              
              st.write("Student number not entered")
              
          elif len(user1) != 0:
              
              st.subheader(f"Student number Entered: :red[{user1}]")
          
         
          
      with tab12:
          
          st.header(":red[Memorundum]", divider = "red")
          
          
      with tab13:
          
          st.header(":red[Summary] of :red[the] Practical", divider = "red")
          
          
      with tab14:
          
          st.header(":red[Key] Skills :red[Students] Learned", divider = "red")
      
      
      with tab15:
          
          st.header(":red[Common] Errors :red[Students] Made", divider = "red")
          
          
      with tab16:
          
          st.header(":red[Final] Remark", divider = "red")  
        
        


# Third selection choice in the radio selection
elif menu == "Practicals 2nd Semester":
    
    st.header(":red[Practicals] Second :red[Semester]", divider = "red")
    st.sidebar.header(":red[Practicals]")
    
    # Side bar for the practical names in the Second Semester
    # The first number represent the semester number, 2 for Second semester
    prac_21 = None
    prac_22 = None
    prac_23 = None
    prac_24 = None
    prac_25 = None
    
    # list to store the practicals
    prac_2_semester = [prac_21, prac_22, prac_23, prac_24, prac_25]
    
    # select box to select the practical you want to view
    practicals_second_semester = st.sidebar.selectbox(
        "Choose a practical to view",prac_2_semester )
    
    # What happens after selecting the practical
    # Create tabs for information under practicals
    alltabs = ["Marks", "Memorundum","Summary", "Key skills learned", "Common Errors", "Final Remarks"]
    tab21, tab22, tab23, tab24, tab25, tab26 = st.tabs(alltabs)
    
    # When the practical is chosen, what is displayed after
    if practicals_second_semester == prac_21:
        
        with tab21:
            
            st.header(":red[Practical] Marks", divider = "red")
            
            # Text input for the user to access their marks
            user2 = st.text_input("Enter your student number") # the number on user represent the semester
            st.subheader(f"Student number Entered: :red[{user2}]")
            
            
        with tab22:
            
            st.header(":red[Memorundum]", divider = "red")
            
            
        with tab23:
            
            st.header(":red[Summary] of :red[the] Practical", divider = "red")
            
            
        with tab24:
            
            st.header(":red[Key] Skills :red[Students] Learned", divider = "red")
        
        
        with tab25:
            
            st.header(":red[Common] Errors :red[Students] Made", divider = "red")
            
            
        with tab26:
            
            st.header(":red[Final] Remark", divider = "red")
            
    # if the second practical is selected  
    elif practicals_first_semester == prac_12:
        
        with tab21:
            
            st.header(":red[Practical] Marks", divider = "red")
            
            # Text input for the user to access their marks
            user2 = st.text_input("Enter your student number") # the number on user represent the semester
            st.subheader(f"Student number Entered: :red[{user2}]")
            
            
        with tab22:
            
            st.header(":red[Memorundum]", divider = "red")
            
            
        with tab23:
            
            st.header(":red[Summary] of :red[the] Practical", divider = "red")
            
            
        with tab24:
            
            st.header(":red[Key] Skills :red[Students] Learned", divider = "red")
        
        
        with tab25:
            
            st.header(":red[Common] Errors :red[Students] Made", divider = "red")
            
            
        with tab26:
            
            st.header(":red[Final] Remark", divider = "red")
     
    # if the third practical is selected
    elif practicals_first_semester == prac_13:
        
        with tab21:
            
            st.header(":red[Practical] Marks", divider = "red")
            
            # Text input for the user to access their marks
            user2 = st.text_input("Enter your student number") # the number on user represent the semester
            st.subheader(f"Student number Entered: :red[{user2}]")
            
            
        with tab22:
            
            st.header(":red[Memorundum]", divider = "red")
            
            
        with tab23:
            
            st.header(":red[Summary] of :red[the] Practical", divider = "red")
            
            
        with tab24:
            
            st.header(":red[Key] Skills :red[Students] Learned", divider = "red")
        
        
        with tab25:
            
            st.header(":red[Common] Errors :red[Students] Made", divider = "red")
            
            
        with tab26:
            
            st.header(":red[Final] Remark", divider = "red")
        
       
    # if the fourth practical is selected
    elif practicals_first_semester == prac_14:
        
        with tab21:
            
            st.header(":red[Practical] Marks", divider = "red")
            
            # Text input for the user to access their marks
            user2 = st.text_input("Enter your student number") # the number on user represent the semester
            st.subheader(f"Student number Entered: :red[{user2}]")
            
            
        with tab22:
            
            st.header(":red[Memorundum]", divider = "red")
            
            
        with tab23:
            
            st.header(":red[Summary] of :red[the] Practical", divider = "red")
            
            
        with tab24:
            
            st.header(":red[Key] Skills :red[Students] Learned", divider = "red")
        
        
        with tab25:
            
            st.header(":red[Common] Errors :red[Students] Made", divider = "red")
            
            
        with tab26:
            
            st.header(":red[Final] Remark", divider = "red")
        
        
    # if the fifth practical is selected   
    elif practicals_first_semester == prac_15:
        
        with tab21:
            
            st.header(":red[Practical] Marks", divider = "red")
            
            # Text input for the user to access their marks
            user2 = st.text_input("Enter your student number") # the number on user represent the semester
            st.subheader(f"Student number Entered: :red[{user2}]")
            
            
        with tab22:
            
            st.header(":red[Memorundum]", divider = "red")
            
            
        with tab23:
            
            st.header(":red[Summary] of :red[the] Practical", divider = "red")
            
            
        with tab24:
            
            st.header(":red[Key] Skills :red[Students] Learned", divider = "red")
        
        
        with tab25:
            
            st.header(":red[Common] Errors :red[Students] Made", divider = "red")
            
            
        with tab26:
            
            st.header(":red[Final] Remark", divider = "red")
    
    



# Last selection choice
elif menu == "Contact details":
    
    st.header(":red[How] to :red[get] a :red[hold] of :red[me]", divider = "red")
    email = "201716358@ufh.ac.za"
    num = "+27 (0) 71 990 3873"
    st.write(f"You can reach Mr Oswald Roberts at {num} or send an email to {email} ")
    
elif menu == "About author(s)":
    
    st.header(":red[Brief] Introduction :red[of] Authors :red[Research] Field", divider = "red")
    
    # Read content from the .castep file
    with open("About_author.txt", 'r') as file:
        content = file.read()
    
    st.write(content)
    
    
  
  # Name of each practical
    
    # Each practical will have file of the memorundum
    
    # Summary of the practical
    
    # Key skills to have picted up
    
    # Errors students made when writing the report
    
    # Final remarks
    
    # Input box to display the marks of the inluded student
    
    # If Demonstrators added their names, the will receive marks for all students in the app and as a file
    
    # Give unique code to demonstrators to access the information
    
  # My contact details
  
  