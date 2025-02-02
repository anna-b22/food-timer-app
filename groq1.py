from groq import Groq

client = Groq( api_key='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',)
a=input('Enter the dish name: ')
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "For the dish mentioned by the user, create a recipe in 10 sentences or less on how it should be made."
        },
        
        {
            "role": "user",
            "content": a
        },
        '''{
            "role": "assistant",
            "content": "To make an omelette, crack 2 eggs into a bowl and whisk them together. Add a pinch of salt and pepper to taste. Heat a non-stick pan over medium heat and add 1 tablespoon of butter. Once the butter has melted, pour in the egg mixture. Let the eggs cook for about 2 minutes, until the edges start to set. Add any desired fillings, such as diced vegetables or shredded cheese. Use a spatula to gently fold the omelette in half. Cook for another minute, until the eggs are fully set and the fillings are heated through. Slide the omelette out of the pan onto a plate and serve hot. Enjoy your delicious homemade omelette!"
        },
        {
            "role": "user",
            "content": "For the dish mentioned by the user, create a recipe in 10 sentences or less on how it should be made.\n"
        },
        {
            "role": "assistant",
            "content": "To make an omelette, crack 2 eggs into a bowl and whisk them together. Add a pinch of salt and pepper to taste. Heat a non-stick pan over medium heat and add 1 tablespoon of butter. Once the butter has melted, pour in the egg mixture. Let the eggs cook for about 2 minutes, until the edges start to set. Add any desired fillings, such as diced vegetables or shredded cheese. Use a spatula to gently fold the omelette in half. Cook for another minute, until the eggs are fully set. Slide the omelette out of the pan onto a plate and serve hot. This simple recipe yields a delicious and fluffy omelette."
        },
        {
            "role": "user",
            "content": "give code to do the same for any food entered by the user\n"
        },
        {
            "role": "assistant",
            "content": "Here's a simple Python code snippet that generates a recipe based on the user's input. Please note that this is a simplified example and doesn't cover all possible food items. For a more comprehensive solution, you would need to use a large database of recipes or Natural Language Processing (NLP) techniques.\n\n```python\nclass RecipeGenerator:\n    def __init__(self):\n        self.recipes = {\n            \"omelette\": \"Crack eggs into a bowl, whisk them together, add salt and pepper, heat a non-stick pan, pour in egg mixture, add fillings, fold in half, cook until set.\",\n            \"pasta\": \"Boil pasta, heat a saucepan with olive oil, add garlic, add tomato sauce, combine cooked pasta and sauce.\",\n            \"salad\": \"Chop vegetables, combine in a bowl, add dressing, toss to coat.\",\n            # Add more recipes here\n        }\n\n    def generate_recipe(self, dish):\n        if dish.lower() in self.recipes:\n            return self.recipes[dish.lower()]\n        else:\n            return \"Sorry, we don't have a recipe for that dish.\"\n\ndef main():\n    generator = RecipeGenerator()\n    print(\"Welcome to the Recipe Generator!\")\n    while True:\n        dish = input(\"Enter a dish name (or 'exit' to quit): \")\n        if dish.lower() == 'exit':\n            break\n        recipe = generator.generate_recipe(dish)\n        print(\"Here's a simple recipe for {}: {}\".format(dish, recipe))\n\nif __name__ == \"__main__\":\n    main()\n```\n\nHowever, to create a more robust system, you could use a Natural Language Processing (NLP) library like NLTK or spaCy to parse user input and generate recipes based on that.\n\nHere's an example using NLTK and a simple recipe database:\n\n```python\nimport nltk\nfrom nltk.tokenize import word_tokenize\nfrom nltk.corpus import stopwords\n\n# Ensure the necessary NLTK data is downloaded\nnltk.download('punkt')\nnltk.download('stopwords')\n\nclass RecipeGenerator:\n    def __init__(self):\n        self.recipes = {\n            \"omelette\": \"Crack eggs into a bowl, whisk them together, add salt and pepper, heat a non-stick pan, pour in egg mixture, add fillings, fold in half, cook until set.\",\n            \"pasta\": \"Boil pasta, heat a saucepan with olive oil, add garlic, add tomato sauce, combine cooked pasta and sauce.\",\n            \"salad\": \"Chop vegetables, combine in a bowl, add dressing, toss to coat.\",\n            # Add more recipes here\n        }\n\n    def generate_recipe(self, dish):\n        stop_words = set(stopwords.words('english'))\n        tokenized_dish = word_tokenize(dish)\n        keywords = [word for word in tokenized_dish if word.lower() not in stop_words]\n\n        for keyword in keywords:\n            if keyword.lower() in self.recipes:\n                return self.recipes[keyword.lower()]\n        return \"Sorry, we don't have a recipe for that dish.\"\n\ndef main():\n    generator = RecipeGenerator()\n    print(\"Welcome to the Recipe Generator!\")\n    while True:\n        dish = input(\"Enter a dish name (or 'exit' to quit): \")\n        if dish.lower() == 'exit':\n            break\n        recipe = generator.generate_recipe(dish)\n        print(\"Here's a simple recipe for {}: {}\".format(dish, recipe))\n\nif __name__ == \"__main__\":\n    main()\n```\n\nThis code is still quite simple and would need to be expanded upon to cover more dishes and recipe variations. For a fully-fledged recipe generator, consider using a machine learning model or integrating with a large recipe database."
        }'''
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
