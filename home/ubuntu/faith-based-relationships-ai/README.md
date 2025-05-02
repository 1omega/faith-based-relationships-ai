# Faith-Based Relationships AI Dataset

This repository aims to collect and structure information related to faith-based relationships, with an initial focus on Christian doctrine, for the purpose of training AI models.

## Goal

To create a comprehensive, structured, and community-driven dataset that can power AI applications for relationship coaching, counseling, and guidance from a faith perspective.

## Structure

The repository is organized as follows:

-   `/data`: Contains the core dataset in JSON format, categorized by source type:
    -   `scripture/`: Data derived directly from scripture interpretation.
    -   `theology/`: Data from theological sources/commentary.
    -   `counseling/`: Data related to counseling principles/practices.
    -   `practical_advice/`: General relationship advice from a faith perspective.
    -   `user_submissions/`: Moderated contributions (staging area).
-   `/docs`: Contains documentation:
    -   `repository_design.md`: Detailed design of the repository structure and data format.
    -   `data_schema.json`: Formal JSON schema definition for validation.
    -   `ai_agent_concept.md`: Conceptual outline for an AI counselor agent using this data.
-   `/scripts`: May contain utility scripts for data validation, processing, etc. (Currently empty).
-   `CONTRIBUTING.md`: Guidelines for contributing to the dataset, including the moderation process.
-   `LICENSE`: The license under which the data is distributed (CC BY-NC-SA 4.0).
-   `README.md`: This file.

## Data Format

Data is stored in JSON format, with each file typically containing an array of data entries. Each entry adheres to the structure defined in `docs/data_schema.json`. Key fields include:

-   `entry_id`: Unique identifier.
-   `topic`, `sub_topic`: Categorization.
-   `faith_perspective`: Currently "Christian".
-   `source_type`, `source_reference`: Origin of the information.
-   `content_summary`, `content_detailed`: Core information.
-   `keywords`: For searchability.
-   `related_scripture`, `related_entries`: Links to other relevant data.
-   `qa_pairs`, `instruction_response`: Formats suitable for AI training.
-   `metadata`: Information about the entry's creation, modification, and status.

### Example Entry Snippet (from `/data/scripture/proverbs_15_1.json`):

```json
{
  "entry_id": "SCRPT_PROV_15_1_GENTLE_ANSWER",
  "topic": ["Conflict Resolution", "Communication", "Anger Management", "Wisdom"],
  "sub_topic": "Responding Gently",
  "faith_perspective": "Christian",
  "source_type": "Scripture",
  "source_reference": {
    "text": "Proverbs 15:1 (NIV)",
    "url": "https://www.biblegateway.com/passage/?search=Proverbs+15%3A1&version=NIV"
  },
  "content_summary": "Contrasts the effect of gentle versus harsh communication in conflict: a gentle answer defuses anger (\"turns away wrath\"), while a harsh word escalates it (\"stirs up anger\").",
  // ... other fields like content_detailed, keywords, qa_pairs, metadata ...
}
```

## Usage

This dataset can be used for various purposes, including:

1.  **AI Training:** Fine-tuning or providing context (via RAG) for Large Language Models (LLMs) to create AI-powered relationship coaches, counselors, or chatbots grounded in Christian principles. See `docs/ai_agent_concept.md` for ideas.
2.  **Research:** Analyzing patterns in faith-based relationship advice, scriptural interpretations, or counseling themes.
3.  **Content Creation:** Serving as a structured knowledge base for articles, study guides, or educational materials on Christian relationships.
4.  **Personal Study:** Exploring interconnected concepts and scriptures related to relationship topics.

To use the data, you can parse the JSON files in the `/data` directory using standard programming tools.

## Contributing

We welcome contributions to expand and enrich this dataset! Please carefully read the `CONTRIBUTING.md` file for detailed guidelines on data formatting, submission via Pull Requests, and the moderation process.

## License

This dataset is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](LICENSE) (CC BY-NC-SA 4.0). Please review the `LICENSE` file for full details.

