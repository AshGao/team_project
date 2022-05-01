This team project folder includes everything that required to run the code. The recipe_app_for_running.py is the code that you run for openning the web app. To run this code, make sure that Flask is installed in your command prompt. The functions code used in recipe_app_for_running.py are imported from the recipe_helper.py. The functions in recipe_helper could output the intended output on webapp (The title and steps of recipes) when the expected kinds of inputs (ingredient and calories) are input by users. 

For the functions in recipe_helper.py, the first function we need is a get_json function to help us get the requested data from the dataset. Then, we build functions get_id to filter recipes with an ingredient and return the ID of the recipes. With the IDs, we are able to use them to do a search again in the dataset to find the recipe title and cooking instructions. Then we added the if statement in the function to filter these recipes that do not meet the calories requirement. To find the calories, we build the get_cal function. The final output data is the title and steps of the recipe that contain the ingredient and meet the calories requirement. They are achieved seperately by two function: get_recipes_title and get_recipes_step.

Have fun with our code!

To access the application, please copy and paste the link below to your web browser.
https://babson-recipe-generator.herokuapp.com/recipe/


To view our website, please visit:
https://sites.google.com/babson.edu/recipe-generator/