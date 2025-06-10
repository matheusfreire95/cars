from openai import OpenAI


client = OpenAI(
    api_key='API_KEY'
)


def get_car_ai_bio(model, brand, year):
    prompt = ''''
    Me mostre uma descrição de venda do carro {} {} {} em apenas 250 caracteres. 
    Fale coisas específicas sobre esse modelo.
    '''
    prompt = prompt.format(model, brand, year)

    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        max_tokens=1000,
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ],
    )

    return completion.choices[0].message;
