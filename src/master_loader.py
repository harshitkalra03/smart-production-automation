from pathlib import Path
import pandas as pd


class MasterLoader:
    def __init__(self):
        self.project_root = Path(__file__).resolve().parent.parent

        self.data_dir = self.project_root / "data"

        self.brand_file = self.data_dir / "Brand Models.csv"
        self.tank_file = self.data_dir / "Brand_Model_Tank.csv"
        self.shape_file = self.data_dir / "Model_shape.csv"

        self.output_file = self.data_dir / "master_products.csv"
        self.validation_file = self.data_dir / "validation_report.txt"

        self.brands = [
            "ORIENT",
            "KENSTAR",
            "SURYA",
            "POLYCAB",
            "CROMA",
            "HINDWARE",
            "RR",
            "GOLDMEDAL",
            "LAZER",
            "KROMO",
            "SUNFLAME",
            "VETO",
            "JOHNSON",
            "GM ELEKTRA",
            "BPL",
            "VENUS",
            "BLACK DECKER",
            "LIFELONG",
            "GLEN",
            "MCCOY",
            "ACCURA",
            "ALLOMAX",
            "INALSA",
            "SMART",
            "SAKASH",
            "SUJATA",
            "SAMEER",
        ]

        self.tank_types = [
            "SS TANK",
            "POLYMER",
            "GLASSLINE",
        ]

        self.shapes = [
            "HORIZONTAL",
            "INSTANT",
            "SQUARE",
            "VERTICAL",
        ]

    def load_single_column(self, file_path):
        df = pd.read_csv(file_path, header=None)
        return (
            df.iloc[:, 0]
            .fillna("")
            .astype(str)
            .str.strip()
            .tolist()
        )

    def build_brand_mapping(self):
        data = self.load_single_column(self.brand_file)

        mapping = {}

        current_brand = None

        for item in data:

            if item.upper() in self.brands:
                current_brand = item.title()
                continue

            if current_brand and item:
                mapping[item] = current_brand

        return mapping

    def build_tank_mapping(self):
        data = self.load_single_column(self.tank_file)

        mapping = {}

        current_tank = None

        for item in data:

            if item.upper() in self.tank_types:
                current_tank = item.title()
                continue

            if current_tank and item:
                mapping[item] = current_tank

        return mapping

    def build_shape_mapping(self):
        data = self.load_single_column(self.shape_file)

        mapping = {}

        current_shape = None

        for item in data:

            if item.upper() in self.shapes:
                current_shape = item.title()
                continue

            if current_shape and item:
                mapping[item] = current_shape

        return mapping

    def generate_master_products(self):

        brand_map = self.build_brand_mapping()
        tank_map = self.build_tank_mapping()
        shape_map = self.build_shape_mapping()

        all_models = (
            set(brand_map.keys())
            | set(tank_map.keys())
            | set(shape_map.keys())
        )

        rows = []

        missing_brand = []
        missing_tank = []
        missing_shape = []

        for idx, model in enumerate(sorted(all_models), start=1):

            brand = brand_map.get(model, "")
            tank = tank_map.get(model, "")
            shape = shape_map.get(model, "")

            if not brand:
                missing_brand.append(model)

            if not tank:
                missing_tank.append(model)

            if not shape:
                missing_shape.append(model)

            rows.append(
                {
                    "Product_ID": f"P{idx:04d}",
                    "Brand": brand,
                    "Model": model,
                    "Tank_Type": tank,
                    "Shape": shape,
                    "Is_Active": "Y",
                    "Notes": "",
                }
            )

        master_df = pd.DataFrame(rows)

        master_df.to_csv(
            self.output_file,
            index=False
        )

        with open(self.validation_file, "w") as f:

            f.write("MASTER PRODUCT VALIDATION REPORT\n")
            f.write("=" * 50 + "\n\n")

            f.write(
                f"Total Products : {len(master_df)}\n\n"
            )

            f.write(
                f"Missing Brand : {len(missing_brand)}\n"
            )
            for item in missing_brand:
                f.write(f"  - {item}\n")

            f.write("\n")

            f.write(
                f"Missing Tank Type : {len(missing_tank)}\n"
            )
            for item in missing_tank:
                f.write(f"  - {item}\n")

            f.write("\n")

            f.write(
                f"Missing Shape : {len(missing_shape)}\n"
            )
            for item in missing_shape:
                f.write(f"  - {item}\n")

        print("\nSUCCESS")
        print("-" * 50)
        print(f"Master File : {self.output_file}")
        print(f"Validation Report : {self.validation_file}")
        print(f"Total Products : {len(master_df)}")


if __name__ == "__main__":
    loader = MasterLoader()
    loader.generate_master_products()