# Repository Design: Faith-Based Relationships AI

## 1. Goal

To create a structured, comprehensive, and extensible dataset of faith-based relationship information, primarily focused on Christian doctrine, suitable for training AI models (like LLMs) for applications such as relationship coaching, counseling, and advice.

## 2. Inspiration

The design draws inspiration from existing structured data repositories, particularly `BradyStephenson/bible-data`, for its methodical approach to linking entities (people, places, events) and referencing sources within biblical texts.

## 3. Directory Structure

The proposed directory structure organizes data by source type and includes documentation and potential scripts:

```
faith-based-relationships-ai/
├── data/                  # Main directory for structured data files (JSON format)
│   ├── scripture/         # Data derived directly from scripture interpretation
│   ├── theology/          # Data from theological sources/commentary
│   ├── counseling/        # Data related to counseling principles/practices
│   ├── practical_advice/  # General relationship advice from a faith perspective
│   └── user_submissions/  # Moderated contributions (initially empty or staging area)
├── docs/                  # Documentation files
│   ├── repository_design.md # This document
│   └── data_schema.json   # Formal JSON schema definition
├── scripts/               # Optional: Scripts for data validation, processing, contribution management, etc.
├── CONTRIBUTING.md        # Contribution guidelines and moderation process
├── LICENSE                # License file (To be determined, likely CC BY-NC-SA 4.0)
└── README.md              # Project overview, goals, structure, usage instructions
```

## 4. Data Format (JSON)

Data will be stored in JSON format. Each logical entry (representing a piece of advice, interpretation, concept, etc.) will be a JSON object. Files within the `data/` subdirectories might contain arrays of these objects.

The proposed structure for each JSON object is as follows:

```json
{
  "entry_id": "string", // Unique identifier (e.g., SCRPT_GEN_2_24_COMM, COUNSEL_COMM_LISTEN_01)
  "topic": ["string"], // List of primary topics (e.g., ["Marriage", "Communication", "Conflict Resolution"])
  "sub_topic": "string", // Optional: More specific sub-topic (e.g., "Active Listening")
  "faith_perspective": "Christian", // Primary perspective (can be extended later)
  "source_type": "string", // Enum: Scripture, Theology, Counseling Guide, Book Summary, Article, User Submission
  "source_reference": {
    "text": "string", // e.g., "Genesis 2:24", "Book Title, Author, Chapter/Page", "Article Title, URL"
    "url": "string" // Optional: Direct URL to the source if available
  },
  "content_summary": "string", // Brief summary of the core teaching, advice, or concept.
  "content_detailed": "string", // Detailed explanation, interpretation, application, context, nuances.
  "keywords": ["string"], // List of relevant keywords for search and filtering.
  "related_scripture": [ // Optional: List of related scripture references
    {
      "text": "string", // e.g., "Ephesians 5:31"
      "url": "string" // Optional: URL
    }
  ],
  "related_entries": ["string"], // Optional: List of entry_ids for related concepts within this dataset.
  "qa_pairs": [ // Optional: Specific Q&A pairs for training conversational AI
    {
      "question": "string",
      "answer": "string"
    }
  ],
  "instruction_response": [ // Optional: Examples formatted for instruction-following models
    {
      "instruction": "string",
      "response": "string"
    }
  ],
  "metadata": {
    "creation_date": "YYYY-MM-DD",
    "last_modified_date": "YYYY-MM-DD",
    "contributor": "string", // Name/ID of contributor or "Initial Seed"
    "version": "number", // Version number for this entry
    "moderation_status": "string" // Enum: Pending, Approved, Rejected, Needs Review
  }
}
```

## 5. Schema Definition

A formal JSON Schema will be created in `docs/data_schema.json` to validate the structure of the data files.

## 6. Contribution and Moderation

Contributions will be accepted via pull requests. A clear process outlined in `CONTRIBUTING.md` will detail submission guidelines, data formatting requirements, and the moderation workflow (review by designated moderators) to ensure quality, consistency, and alignment with the project's focus on Christian doctrine.

## 7. Licensing

Given the goal of broad usability for AI training while potentially incorporating diverse sources, a license like Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) seems appropriate, similar to the `BradyStephenson/bible-data` repository. This needs final confirmation.

