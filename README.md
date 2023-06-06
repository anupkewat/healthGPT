# HealthGPT

Text-to-Speech Medical Assistant Chatbot implemented using the ChatGPT API and Flask framework. The chatbot allows users to enter their symptoms and receive relevant medical advice and information.

## Features

1. **User Interface**: The chatbot provides a web-based user interface where users can interact with the system.

2. **Input Selection**: Users can select their health condition and severity using dropdown menus.

3. **Chat History**: The chatbot maintains a chat history in the form of a list. Each entry in the list represents a message exchanged between the user and the chatbot.

4. **Text-to-Speech Conversion**: The chatbot is equipped with text-to-speech functionality. Users can click on the "Speak" button associated with each message to have the text spoken out loud using a human-like voice.

5. **API Integration**: The chatbot leverages the ChatGPT API to generate responses based on user inputs. It sends requests to the API, retrieves the generated response, and displays it in the chat history.

6. **Medical Advice**: The chatbot provides medical advice and information based on the user's symptoms. It utilizes the capabilities of the ChatGPT model to generate contextually relevant and helpful responses.

## Implementation Details

The implementation of the Text-to-Speech Medical Assistant Chatbot involves the following components:

- **HTML/CSS**: The user interface is designed using HTML and CSS. It includes input fields, dropdown menus, a chat history display, and a "Speak" button associated with each message.

- **JavaScript/jQuery**: JavaScript and jQuery are used to handle user interactions and dynamically update the chat history. The "Speak" button's click event triggers the text-to-speech functionality.

- **Flask**: The Flask framework is utilized to build the web application. It handles routing, request handling, and communication with the ChatGPT API.

- **ChatGPT API**: The ChatGPT API is integrated into the Flask application. When the user submits their symptoms, a request is sent to the API with the user's input. The API responds with a generated response, which is then displayed in the chat history.

- **Text-to-Speech (TTS) Integration**: The TTS functionality is implemented using the Web Speech API. When the "Speak" button is clicked, the associated message's text is converted to speech using a human-like voice.

