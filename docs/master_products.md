# master_products.csv

## Master Product Database Schema (V1)

This file acts as the primary lookup database for the application.

Every model must appear exactly once.

The parser will use this file to determine:

* Brand
* Tank Type
* Shape

Power and Category will be calculated using capacity rules.

---

## Columns

| Column Name | Description                              |
| ----------- | ---------------------------------------- |
| Product_ID  | Unique internal identifier               |
| Brand       | Brand name                               |
| Model       | Standardized model name                  |
| Tank_Type   | SS Tank / Polymer / Glassline            |
| Shape       | Horizontal / Instant / Square / Vertical |
| Is_Active   | Y/N                                      |
| Notes       | Optional comments                        |

---

## Example Records

| Product_ID | Brand   | Model       | Tank_Type | Shape      | Is_Active | Notes |
| ---------- | ------- | ----------- | --------- | ---------- | --------- | ----- |
| P0001      | Orient  | Rapidus     | SS Tank   | Instant    | Y         |       |
| P0002      | Orient  | Aquator Neo | Glassline | Vertical   | Y         |       |
| P0003      | Orient  | Instaflo    | SS Tank   | Instant    | Y         |       |
| P0004      | Johnson | Aquasys     | Polymer   | Instant    | Y         |       |
| P0005      | Surya   | Speedy      | SS Tank   | Horizontal | Y         |       |
| P0006      | RR      | Calid Pro   | SS Tank   | Instant    | Y         |       |
| P0007      | Kenstar | Elix        | Glassline | Vertical   | Y         |       |

---

# Derived Fields (Not Stored)

The following values are generated during parsing and therefore should NOT be stored in master_products.csv.

## Category

Rule:

Capacity < 6L

→ IWH

Capacity ≥ 6L

→ SWH

---

## Power

Rule:

Capacity < 6L

→ 3 kW

Capacity ≥ 6L

→ 2 kW

---

# Example

Input:

Aquator Neo 25L

Master Lookup:

Brand = Orient

Tank Type = Glassline

Shape = Vertical

Capacity = 25

Derived:

Category = SWH

Power = 2 kW

Final Row:

| Brand  | Model       | Tank Type | Shape    | Capacity | Category | Power |
| ------ | ----------- | --------- | -------- | -------- | -------- | ----- |
| Orient | Aquator Neo | Glassline | Vertical | 25       | SWH      | 2 kW  |

---

# Lookup Priority

1. Exact Model Match
2. Case-Insensitive Match
3. Fuzzy Match
4. User Confirmation

---

# Future Extension

Additional columns may be added later:

* Alias Names
* Common Misspellings
* Legacy Models
* Product Family
* SKU Code

without changing parser architecture.
