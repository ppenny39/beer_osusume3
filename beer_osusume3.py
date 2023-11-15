
import streamlit as st
import openai
from googletrans import Translator

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

# OpenAI GPT-3를 사용한 맥주 추천 로직
def recommend_beer_gpt3(bitterness, sweetness, alcohol):
    # Create a prompt for the OpenAI API
    prompt = f"Recommend a beer with bitterness {bitterness}, sweetness {sweetness}, and alcohol content {alcohol}."

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        model="text-davinci-003",  # Adjust the engine name as needed
        prompt=prompt,
        max_tokens=50,  # Adjust max_tokens as needed
        temperature=0.7,  # Adjust temperature as needed
    )

    # Extract and return the recommended beer name from the API response
    recommended_beer = response['choices'][0]['text'].strip()

    # Assuming the recommended beer name is the first line of the response
    recommended_beer_name = recommended_beer.split('\n')[0]

    # Translate the beer name to Korean
    translator = Translator()
    recommended_beer_korean = translator.translate(recommended_beer_name, src='en', dest='ko').text

    return recommended_beer_korean

# 사용자로부터 입력을 받는 스트림릿 애플리케이션을 생성합니다.
st.title('맥주 추천 앱')

# 사용자로부터 입력을 받는 부분
st.header('맛 프로필 입력')
bitterness = st.slider('쓴맛 (Bitterness)', 0, 10, 5)
sweetness = st.slider('단맛 (Sweetness)', 0, 10, 5)
alcohol = st.slider('알콜 함량 (Alcohol Content)', 0, 100, 5)

# 사용자 입력을 기반으로 맥주 추천
if st.button('맥주 추천'):
    recommended_beer = recommend_beer_gpt3(bitterness, sweetness, alcohol)
    st.subheader('추천 맥주')
    st.write(recommended_beer)
