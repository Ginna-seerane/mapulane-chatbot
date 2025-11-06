class MapulaneChatbot:
    def __init__(self):
        self.name = "Mapulane Historian Bot : Rea Makelela!!"
        self.knowledge_base = {
            "who": "The Mapulane are a Southern Bantu ethnic group from South Africa.",
            "where": "They mainly live in the Bushbuckridge region of Mpumalanga, South Africa.",
            "history": "The Mapulane have a long history and are part of the larger Sotho-Tswana language group.",
            "culture": "Their culture includes traditional music, dance, storytelling, and ceremonies passed down through generations.",
            "language": "They speak SePulana (also called SeKutswe), a dialect of Northern Sotho spoken in Mpumalanga and Limpopo provinces of South Africa.",
            "greetings": "In SePulana, people greet each other by saying 'Dumelang' (Hello to more than one person) or 'Dumela' (Hello to one person).",
            "words": "Here are a few SePulana words:\n- 'Tlala' means hunger\n- 'Yetsela' means sleep\n- 'Poto' means pot\n- 'Metsi' means water\n- 'Ntlo' means house"
        }

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        words = user_input.split()

        # Greeting
        if any(word in ["hi", "hello", "hey", "greetings"] for word in words):
            return "Hello! I’m the Mapulane Historian Bot. Ask me about the Mapulane tribe."

        # Farewell
        elif any(word in ["bye", "exit", "goodbye"] for word in words):
            return "Goodbye! Thanks for chatting about the Mapulane tribe."

        # Help
        elif "help" in words:
            return (
                "You can ask about the Mapulane tribe’s history, culture, greetings, language, or where they live."
            )

        # Knowledge base lookup
        elif "who" in user_input:
            return self.knowledge_base["who"]
        elif "where" in user_input:
            return self.knowledge_base["where"]
        elif "history" in user_input:
            return self.knowledge_base["history"]
        elif "culture" in user_input:
            return self.knowledge_base["culture"]
        elif "language" in user_input:
            return self.knowledge_base["language"]
        elif "greet" in user_input or "greeting" in user_input:
            return self.knowledge_base["greetings"]
        # Multiple triggers for SePulana words
        elif any(keyword in user_input for keyword in ["word", "words", "vocabulary", "say"]):
            return self.knowledge_base["words"]

        # Default response
        else:
            return "I'm not sure about that. Try asking about the Mapulane's history, culture, greetings, or language."

    def start_chat(self):
        print(f"Welcome to {self.name}!")
        print("Type 'bye' anytime to end the chat.\n")

        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)
            print(f"Bot: {response}")

            if "bye" in user_input.lower() or "exit" in user_input.lower():
                break


# Run the chatbot
if __name__ == "__main__":
    chatbot = MapulaneChatbot()
    chatbot.start_chat()
