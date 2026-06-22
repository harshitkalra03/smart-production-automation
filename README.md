# Production Automation Desktop

A desktop application designed to automate production data entry from manually shared WhatsApp production reports.

The system transforms unstructured production messages into structured production records, reducing manual data entry effort, minimizing errors, and improving reporting efficiency.

---

## Features

### Master Data Management

* Product master database
* Brand management
* Model management
* Tank type mapping
* Shape mapping
* Power rating mapping

### Production Data Processing

* Paste WhatsApp production messages
* Intelligent message parsing
* Product identification
* Capacity detection
* Production quantity extraction
* Validation before saving

### Data Storage

* SQLite database backend
* Product master records
* Production history records
* Audit-friendly structure

### Reporting & Export

* Excel export
* Production history
* Daily production summaries
* Monthly production summaries

---

## Technology Stack

### Frontend

* PyQt6

### Backend

* Python 3.12

### Database

* SQLite

### Data Processing

* Pandas
* OpenPyXL

### Matching Engine

* RapidFuzz

---

## Project Structure

```text
Production Automation/

data/
├── production.db
├── master_products.json
├── parser_config.json
├── validation_report.txt

src/
├── database/
├── parser/
├── ui/
├── utils/
└── app.py

docs/
└── architecture.md
```

---

## Current Status

### Completed

* Master data architecture
* Excel master validation
* Product database generation
* SQLite database creation
* Product import pipeline

### In Progress

* Desktop application UI
* WhatsApp message parser
* Production entry workflow

### Planned

* Advanced parsing engine
* Excel export automation
* Reporting dashboard
* User management
* Production analytics

---

## Workflow

```text
WhatsApp Message
        ↓
Message Parser
        ↓
Product Identification
        ↓
Preview & Validation
        ↓
SQLite Database
        ↓
Excel Export
```

---

## Author

Harshit Kalra

B.Tech Electrical Engineering, IIT Ropar

Interests:

* Industrial Automation
* Robotics
* Embedded Systems
* Production Digitization
