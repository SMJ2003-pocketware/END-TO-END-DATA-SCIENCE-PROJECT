# END-TO-END-DATA-SCIENCE-PROJECT

*COMPANY*: CODTECH IT SOLUTIONS PVT.LTD

*NAME*: SOHAM MAJUMDER

*INTERN ID*: CT6WMIS

*DOMAIN*: DATA SCIENCE

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

For this task, I developed an ATS (Applicant Tracking System) Resume Analyzer using Streamlit, Google Gemini API, and various Python libraries to help job seekers optimize their resumes for better chances of getting shortlisted. I implemented this project in Google Colab, utilizing its Jupyter Notebook environment to write and test my code efficiently. The main objective of this project was to analyze resumes against job descriptions, extract key information, provide match percentages, and generate detailed feedback, including missing keywords, formatting suggestions, and resume summaries.
To achieve this, I used Streamlit to create a user-friendly web interface that allows users to upload their resumes in PDF format and enter a job description. The system then processes the resume and compares it against the job description using Natural Language Processing (NLP) techniques. The Google Gemini API was integrated to enhance resume analysis by leveraging AI-powered insights for evaluating strengths, weaknesses, and overall suitability.
The project starts by uploading a resume, which is then converted from PDF to an image using the pdf2image library. The image is processed and converted into text, which is later analyzed using NLP techniques. A key part of this project was keyword extraction, where I used regular expressions (re module in Python) to extract essential terms from the job description and compare them with those found in the resume. The system calculates the match percentage, highlighting the missing keywords that could enhance a candidate’s resume.
The Google Gemini AI model plays a crucial role in generating human-like responses based on different prompts. The system can:

  1.Analyze resume suitability by providing feedback on strengths and weaknesses.
  2.Check resume match percentage with job descriptions and highlight missing keywords.
  3.Evaluate resume formatting for ATS compliance.
  4.Generate a concise professional summary based on the extracted information.
  
One of the most important features of this project is the ability to generate a downloadable ATS Resume Analysis Report. The report includes the match percentage, missing keywords, and an AI-generated analysis of the resume. This feature was implemented using the ReportLab library, which allowed me to dynamically generate PDFs.
This Resume Analyzer can be widely applied in career coaching, recruitment agencies, and personal job application strategies. It helps job seekers optimize their resumes based on ATS-friendly formatting and provides valuable insights that can improve job search outcomes. Since many companies use ATS to filter resumes, this project offers a practical solution for increasing a candidate's chances of passing initial screenings.
Working on this project allowed me to gain hands-on experience in Natural Language Processing (NLP), API integration, data extraction, and building interactive web applications. Using Google Colab helped me quickly test different functionalities, and Streamlit made it easy to turn the Python script into a functional web-based Resume Analyzer. Overall, this project was an exciting blend of AI, NLP, and web application development, making it highly relevant in today's job market.

*OUTPUT*

![Image](https://github.com/user-attachments/assets/895e94ce-73cf-42c3-b8ef-e72b1ca024a7)

*Output of Tell me about the Resume*

![Image](https://github.com/user-attachments/assets/36c8f5b2-714a-41ba-932c-59199113e2cf)

![Image](https://github.com/user-attachments/assets/74294d99-098d-4429-8745-ad58116b1c24)

![Image](https://github.com/user-attachments/assets/92bf1328-6719-4958-8a90-d1ebe1a4ad16)

*Ouput of Resume Match Analysis*

![Image](https://github.com/user-attachments/assets/288c91a6-5685-4bdd-853b-67f6621afb33)






