import csv

from models.health_product_review import HealthProductReview


def is_duplicate_product(product_name: str, seen_names: set) -> bool:
    return product_name in seen_names


def is_complete_product(health_product_review: dict, required_keys: list) -> bool:
    return all(key in health_product_review for key in required_keys)


def save_products_to_csv(products: list, filename: str):
    if not products:
        print("No products to save.")
        return

    # Use field names from the Venue model
    fieldnames = HealthProductReview.model_fields.keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)
    print(f"Saved {len(products)} products to '{filename}'.")