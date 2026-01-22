from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from flask import Flask,render_template,request


load_dotenv()

app=Flask(__name__)

model=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

@app.route("/",methods=["GET","POST"])
def Ai():
    reply=""
    if request.method=="POST":
        user_msg=request.form.get("msg")
        reply=model.invoke(user_msg).content
    return render_template("index.html",reply=reply)


if __name__ == "main":
    app.run()

# print("Bot:")
# while True:
#     user_input=input("\nYou:")
    
    
#     if user_input.lower() in ['exit','quit','bye']:
#         print("Good Bye!")
#         break
#     response = model.invoke(user_input)
#     print(response.content)


