# PP1 Dessert Scraper
print("Dessert Recipe Scraper.\n")

#-------------------------------------

# Imports
import requests
from bs4 import BeautifulSoup
import json
import time
import re
import logging

#-------------------------------------

# Set Up Logging
logging.basicConfig(
    filename="main.log",
    filemode="a",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#-------------------------------------

# Load Config
with open("config.json", "r") as file:
    config = json.load(file)

#-------------------------------------
#Main Function
def main(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Failed to fetch page: {url} - {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    ## Saving the HTML source of the initial page
    # with open ("main_url.html", "w", encoding="utf-8") as file:
    #     file.write(soup.prettify())

    recipes = soup.find_all(class_="fl-post")
    print(f"Found {len(recipes)} sweet recipes on page.\n")
    logging.info(f"Found {len(recipes)} sweet recipes on page.")

    # Extracts Key Information From Each Recipe
    recipe_data = []
    for recipe in recipes:
        title = recipe.h2.a["title"]
        image = recipe.img["src"]
        link = recipe.h2.a["href"]

        # Going Deeper Into Each Recipe
        try:
            recipe_response = requests.get(link)
            recipe_response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Failed to fetch recipe page: {link} - {e}")
            continue

        recipe_soup = BeautifulSoup(recipe_response.content, "html.parser")

        # Getting Additional Data From Each Recipe
        ingredients = []
        for n in recipe_soup.select(".wprm-recipe-ingredient"):
            text_one = " ".join(n.stripped_strings)
            cleaned = re.sub(r"(\d+)\s+(g|ml|kg|oz|tbsp|tsp|l)", r"\1\2", text_one)
            ingredients.append(cleaned)

        # Collecting And Cleaning Instructions From Recipies
        instructions = []
        for m in recipe_soup.select(".wprm-recipe-instruction-text"):
            text_two = " ".join(m.stripped_strings)
            cleaned = re.sub(r"(\d+)\s+(g|ml|kg|oz|tbsp|tsp|l)", r"\1\2", text_two)
            instructions.append(cleaned)

        # Saving data to dict
        recipe_data.append({
            "Title": title,
            "Image_url": image,
            "Ingredients": ingredients,
            "Instructions": instructions
        })

    return recipe_data

# -------------------------------------

if __name__ == "__main__":
    all_recipes = []

    # Web To Scrape (first page, no /page/1/)
    first_page_url = config["start_url"]
    print("🍰 Starting dessert hunt on page 1...")
    logging.info("🍰 Starting dessert hunt on page 1...")
    all_recipes.extend(main(first_page_url))
    time.sleep(config["delay_seconds"])  # pause after page

    # Base URL + Scrape Additional Pages
    base_url = config["base_url"]
    for page_number in range(2, config["pages_to_scrape"] + 1):
        print(f"🍰 Starting dessert hunt on page {page_number}...")
        logging.info(f"🍰 Starting dessert hunt on page {page_number}...")
        page_url = base_url.format(page_number)
        all_recipes.extend(main(page_url))
        time.sleep(config["delay_seconds"])

    # Saving Data
    with open("desserts.json", "w", encoding="utf-8") as file:
        json.dump(all_recipes, file, indent=4, ensure_ascii=False)

    # Representing Data
    with open("desserts.json", "r", encoding="utf-8") as file:
        data = json.load(file)

#-------------------------------------

print("The scraping process has been completed.")
# print(f"Data:\n {all_recipes}")