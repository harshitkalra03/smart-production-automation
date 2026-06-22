# WhatsApp Production Data Automation System

## Architecture.md (V1)

---

# Objective

Build a Windows desktop application that converts production updates copied from WhatsApp into structured Excel entries automatically.

The system should:

* Parse semi-structured production messages
* Handle typos and format variations
* Extract production data
* Enrich missing information using master datasets
* Allow user verification
* Update Excel automatically

---

# System Flow

```text
WhatsApp Message
        ↓
Copy & Paste
        ↓
Message Normalization
        ↓
Production Parser
        ↓
Master Data Lookup
        ↓
Confidence Check
        ↓
Editable Preview
        ↓
Excel Update
        ↓
Backup & Audit Log
```

---

# Input Example

```text
10/06/2026
Line No 6

Orient Instaflo 3ltr
Fitting 96
Packing 136

Johnson Aquasys 5ltr
Fitting 453
Packing 453
```

One message may generate:

* Single row
* Multiple rows

depending on the number of products present.

---

# Master Data Files

## 1. Brand Models.csv

Purpose:

```text
Model → Brand
```

Examples:

```text
Rapidus → Orient
Aquasys → Johnson
Speedy → Surya
```

---

## 2. Brand_Model_Tank.csv

Purpose:

```text
Model → Tank Type
```

Tank Types:

* SS Tank
* Polymer
* Glassline

---

## 3. Model_power.csv

Purpose:

```text
Model → Power Rating
```

Power Values:

* 2 kW
* 3 kW
* 4.5 kW

---

## 4. Model_shape.csv

Purpose:

```text
Model → Shape
```

Shape Values:

* Horizontal
* Instant
* Square
* Vertical

---

# Extracted Fields

| Field     |
| --------- |
| Sr No     |
| Date      |
| Month     |
| Year      |
| Line      |
| Brand     |
| Model     |
| Capacity  |
| Fitting   |
| Packaging |
| Remarks   |

---

# Auto-Filled Fields

Using Master CSV Files:

| Field     | Source               |
| --------- | -------------------- |
| Brand     | Brand Models.csv     |
| Tank Type | Brand_Model_Tank.csv |
| Power     | Model_power.csv      |
| Shape     | Model_shape.csv      |

---

# Category Rule

```text
1L  → IWH
3L  → IWH
5L  → IWH
5.5L → IWH
5.9L → IWH

6L and above → SWH
```

---

# Final Output Columns

| Sr No |
| Date |
| Month |
| Year |
| Line |
| Category |
| Tank Type |
| Brand |
| Model |
| Power |
| Shape |
| Capacity |
| Fitting |
| Packaging |
| Remarks |
| Day Total |
| Cumulative Total |

---

# Parser Stages

### Stage 1 — Normalize Message

* Remove extra spaces
* Standardize units
* Standardize dates

### Stage 2 — Extract Header

* Date
* Production Line

### Stage 3 — Detect Products

Identify individual products inside the message.

### Stage 4 — Extract Data

* Brand
* Model
* Capacity
* Fitting
* Packaging
* Remarks

### Stage 5 — Master Lookup

Populate:

* Tank Type
* Power
* Shape
* Missing Brand

### Stage 6 — Category Assignment

Apply IWH / SWH rule.

### Stage 7 — Generate Preview

User verifies extracted rows.

### Stage 8 — Excel Update

Write validated rows to Excel workbook.

---

# Confidence Levels

### 100%

Exact match

```text
Rapidus
```

### 95%

Brand inferred

```text
Rapidus 5.5
```

### 85%

Fuzzy correction

```text
Rapiduss
→ Rapidus
```

### <85%

Manual verification required.

---

# Technology Stack

### Frontend

* Python
* PyQt6

### Backend

* Pandas
* OpenPyXL
* SQLite

### Matching Engine

* RapidFuzz

### Deployment

* Windows Desktop Application

---

# MVP Goal

Achieve 90–95% extraction accuracy using:

* Rule Engine
* Master CSV Files
* Fuzzy Matching
* User Verification

without requiring cloud AI services.