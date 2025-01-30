import base64
import streamlit as st
import os
import io
import re
import pdf2image
from collections import Counter
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import google.generativeai as genai

# Manually set the API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBxRbGXI8uHU-NMb4eDbPOUunf2aNKoPDU"

# Now configure Gemini API with the key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content, prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        pdf_parts = []
        for image in images:
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()
            pdf_parts.append({
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            })
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

def extract_keywords(job_description):
    words = re.findall(r'\b\w{4,}\b', job_description.lower())
    return set(words)

def check_keywords_match(resume_text, job_description):
    job_keywords = extract_keywords(job_description)
    resume_keywords = extract_keywords(resume_text)
    missing_keywords = job_keywords - resume_keywords
    match_percentage = (len(job_keywords & resume_keywords) / len(job_keywords)) * 100 if job_keywords else 0
    return match_percentage, missing_keywords

def generate_pdf_report(response_text, match_percentage, missing_keywords):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 750, "ATS Resume Analysis Report")
    pdf.drawString(100, 730, f"Match Percentage: {match_percentage:.2f}%")
    pdf.drawString(100, 710, f"Missing Keywords: {', '.join(missing_keywords)}")
    text = pdf.beginText(100, 690)
    text.setFont("Helvetica", 10)
    text.textLines(response_text)
    pdf.drawText(text)
    pdf.save()
    buffer.seek(0)
    return buffer

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")
submit4 = st.button("Check Resume Formatting")
submit5 = st.button("Generate Resume Summary")
submit6 = st.button("Download Report")

input_prompt1 = """
You are an experienced Technical HR Manager. Review the resume against the job description.
Highlight strengths, weaknesses, and overall suitability.
"""

input_prompt3 = """
You are an ATS scanner. Compare the resume against the job description.
Provide match percentage, missing keywords, and final thoughts.
"""

input_prompt4 = """
You are an expert in resume formatting and ATS optimization. Analyze readability, structure, and ATS compatibility.
"""

input_prompt5 = """
You are a professional career coach. Summarize the resume into a compelling professional summary (max 5 sentences).
"""

if submit1 or submit3 or submit4 or submit5:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        prompt = input_prompt1 if submit1 else input_prompt3 if submit3 else input_prompt4 if submit4 else input_prompt5
        response = get_gemini_response(input_text, pdf_content[0], prompt)
        
        if submit3:
            resume_text = response.lower()
            match_percentage, missing_keywords = check_keywords_match(resume_text, input_text)
            st.subheader("📊 Resume Match Analysis")
            st.write(f"✅ **Match Percentage:** {match_percentage:.2f}%")
            st.write(f"🔴 **Missing Keywords:** {', '.join(missing_keywords)}")
        
        st.subheader("📄 Response")
        st.write(response)
    else:
        st.warning("Please upload a resume before proceeding.")

if submit6:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content[0], input_text)
        resume_text = response.lower()
        match_percentage, missing_keywords = check_keywords_match(resume_text, input_text)
        pdf_buffer = generate_pdf_report(response, match_percentage, missing_keywords)
        st.download_button(label="📄 Download Report", data=pdf_buffer, file_name="ATS_Resume_Report.pdf", mime="application/pdf")
    else:
        st.warning("Please upload a resume before proceeding.")