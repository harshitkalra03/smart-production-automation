import sqlite3
import json
from pathlib import Path


class ProductImporter:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parent.parent.parent

        self.db_path = self.project_root / "data" / "production.db"

        self.master_file = (
            self.project_root
            / "data"
            / "master_products.json"
        )

    def import_products(self):

        with open(
            self.master_file,
            "r",
            encoding="utf-8"
        ) as f:

            products = json.load(f)

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        inserted = 0
        skipped = 0

        for model, data in products.items():

            try:

                cursor.execute(
                    """
                    INSERT INTO products
                    (
                        brand,
                        model,
                        tank_type,
                        shape,
                        power,
                        active
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        data["brand"],
                        model,
                        data["tank_type"],
                        data["shape"],
                        data["power"],
                        "Y"
                    )
                )

                inserted += 1

            except sqlite3.IntegrityError:

                skipped += 1

        conn.commit()
        conn.close()

        print("\nPRODUCT IMPORT COMPLETE")
        print("-" * 40)
        print(f"Inserted : {inserted}")
        print(f"Skipped  : {skipped}")


if __name__ == "__main__":

    ProductImporter().import_products()