# parser_rules.md

## WhatsApp Production Data Parser Rules (V1)

---

# Objective

Convert semi-structured production messages into structured records suitable for Excel insertion.

The parser must handle:

* Multiple message formats
* Missing brands
* Typing mistakes
* Inconsistent spacing
* Multiple products per message
* Remarks mixed with production data

---

# Parsing Pipeline

```text
Raw Message
    ↓
Normalization
    ↓
Header Extraction
    ↓
Product Detection
    ↓
Field Extraction
    ↓
Master Lookup
    ↓
Derived Calculations
    ↓
Confidence Scoring
    ↓
Preview Table
```

---

# Rule 1: Date Extraction

Supported formats:

```text
10/06/2026
10/06/26
10.06.2026
Date - 10/06/2026
Date:-10/06/2026
```

Output format:

```text
DD/MM/YYYY
```

Example:

```text
10/06/26
```

becomes

```text
10/06/2026
```

---

# Rule 2: Line Number Extraction

Supported formats:

```text
Line No 5
Line no. 5
Line-:01
Line 01
Lino no - 03
```

Output:

```text
1
2
3
4
5
6
```

Only numeric value stored.

---

# Rule 3: Product Detection

A new product starts when:

* A known model is detected
* A known brand is detected
* A capacity value appears beside a valid model

Example:

```text
Instaflo 3ltr
Fitting 96
Packing 136

Aquasys 5ltr
Fitting 453
Packing 453
```

Creates:

Product 1

```text
Instaflo
```

Product 2

```text
Aquasys
```

---

# Rule 4: Brand Extraction

Priority:

### 1. Direct Brand Detection

Example:

```text
Orient Rapidus
```

Brand = Orient

---

### 2. Master Lookup

Example:

```text
Rapidus
```

Lookup:

```text
Rapidus → Orient
```

Brand automatically assigned.

---

# Rule 5: Model Extraction

Priority:

### Exact Match

```text
Aquator Neo
```

---

### Case-Insensitive Match

```text
aquator neo
```

---

### Fuzzy Match

```text
Aquator Nio
```

↓

```text
Aquator Neo
```

---

### Manual Review

If confidence too low.

---

# Rule 6: Capacity Extraction

Supported formats:

```text
3ltr
3 ltr
3L
03 ltr

25ltr
25 ltr
25L
```

Output:

```text
3
5
5.5
5.9
10
15
25
```

Stored as numeric value.

---

# Rule 7: Fitting Extraction

Supported formats:

```text
Fitting - 100
Fitting=100
Fit 100
Only fitting 100
```

Output:

```text
100
```

Default:

```text
NULL
```

if missing.

---

# Rule 8: Packaging Extraction

Supported formats:

```text
Packing - 100
Packing=100
Pack 100
```

Output:

```text
100
```

Default:

```text
NULL
```

if missing.

---

# Rule 9: Remarks Extraction

Store any operational notes not used elsewhere.

Examples:

```text
Without show plate
Without hologram
Hologram shortage
Connection pipe shortage
Outer box shortage
Inner box shortage
Dummy
Slate Grey
```

Output:

Stored in Remarks column.

---

# Rule 10: Category Calculation

Based on Capacity.

```text
Capacity < 6
```

↓

```text
IWH
```

```text
Capacity ≥ 6
```

↓

```text
SWH
```

---

# Rule 11: Power Calculation

Based on Capacity.

```text
Capacity < 6
```

↓

```text
3 kW
```

```text
Capacity ≥ 6
```

↓

```text
2 kW
```

---

# Rule 12: Month Extraction

Derived from Date.

Example:

```text
10/06/2026
```

↓

```text
June
```

---

# Rule 13: Year Extraction

Derived from Date.

Example:

```text
10/06/2026
```

↓

```text
2026
```

---

# Rule 14: Tank Type Lookup

Lookup from:

```text
Brand_Model_Tank.csv
```

Output:

```text
SS Tank
Polymer
Glassline
```

---

# Rule 15: Shape Lookup

Lookup from:

```text
Model_shape.csv
```

Output:

```text
Horizontal
Instant
Square
Vertical
```

---

# Rule 16: Confidence Scoring

### 100%

Exact model match.

```text
Rapidus
```

---

### 95%

Brand inferred from model.

```text
Rapidus 5.5
```

---

### 85%

Fuzzy correction applied.

```text
Rapiduss
```

↓

```text
Rapidus
```

---

### Below 85%

Requires user verification.

Highlighted in Preview Screen.

---

# Rule 17: Excel Update Eligibility

Rows can be inserted into Excel only if:

* Date found
* Line found
* Model found
* Capacity found

Otherwise:

```text
Status = Needs Review
```

---

# Rule 18: Audit Logging

Every Excel update should log:

* Timestamp
* User
* Message Source
* Number of Rows Inserted
* Number of Corrections

Stored in SQLite database.

---

# MVP Success Criteria

Parser should correctly process:

* Multiple products per message
* Missing brands
* Minor spelling errors
* Different date formats
* Different line number formats
* Common production remarks

Target Accuracy:

90–95%
