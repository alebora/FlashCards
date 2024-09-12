import json

class FlashcardApp:        
    def __init__(self):
        self.flashcards = []
        self.load_flashcards()

    def load_flashcards(self):   
        try:
            with open('flashcards.json', 'r') as file:   
                self.flashcards = json.load(file)
        except FileNotFoundError:
            self.flashcards = []  

    def save_flashcards(self):
        with open('flashcards.json', 'w') as file:  
            json.dump(self.flashcards, file)

    def add_flashcard(self):
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        self.flashcards.append({'question': question, 'answer': answer})
        self.save_flashcards()
        print("Flashcard added!")

    def quiz(self):
        if not self.flashcards:
            print("No flashcards available. Please add some first.")
            return

        score = 0
        for flashcard in self.flashcards:
            user_answer = input(f"Q: {flashcard['question']} ")
            if user_answer.strip().lower() == flashcard['answer'].strip().lower():
                print("Correct!:)")
                score += 1
            else:
                print(f"Incorrect, the correct answer is: {flashcard['answer']}")
        
        print(f"Your final score is: {score}/{len(self.flashcards)}")

    def run(self):
        while True:
            print("\nFlashcard Quiz App")
            print("1. Add Flashcard")
            print("2. Take Quiz")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_flashcard()
            elif choice == '2':
                self.quiz()
            elif choice == '3':
                print("Thank you, keep studying hard! Byebye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = FlashcardApp()
    app.run()
