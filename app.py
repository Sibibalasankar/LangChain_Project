from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

print("Bot:")
while True:
    user_input=input("\nYou:")
    
    
    if user_input.lower() in ['exit','quit','bye']:
        print("Good Bye!")
        break
    response = model.invoke(user_input)
    print(response.content)