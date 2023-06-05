import openai

# messages = [ 
#     { "role" : "system" , "content" : "You are a medical assistant."}
# ]
# def send_message(message):
#     messages.append( 
#         {"role" : "user", "content" : message},
#     )
#     response = openai.Completion.create(
#         engine='gpt-3.5-turbo', prompt = message
#     )

#     reply = response.choices[0].message.content
#     return reply

# user_input = input("You: ")
# bot_response = send_message(user_input)
# print("GPT:", bot_response)

openai.api_key = open("key.txt","r").read().strip('/n')

chat = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "i have severe symptoms of cold, suggest actions"}
        
    ]
)
reply = chat.choices[0].message.content
print ( f' response : {reply}')


# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Write a tagline for an ice cream shop."
# )
# print(response)