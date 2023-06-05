import openai

openai.api_key = open("key.txt","r").read().strip('\n')

def askGPT(prompt):
    print("asked prompt : ", prompt)
    chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'{prompt}'}            
        ]
    )

    try:
        answer= chat.choices[0].message.content.replace('\n' , '<br>')
    except:
        answer= "Cannot find results,try again later."
    
    return answer

# prompt = "say 1"

# reply = askGPT(prompt)

# print ( f' response : {reply}')


