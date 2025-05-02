# Contributing to the Faith-Based Relationships AI Dataset

Thank you for your interest in contributing to this dataset! Your contributions will help build a valuable resource for AI applications focused on relationship guidance from a Christian perspective.

## How to Contribute

Contributions are managed through GitHub Pull Requests (PRs).

1.  **Fork the Repository:** Create your own copy of this repository.
2.  **Create a Branch:** Create a new branch in your fork for your contribution (e.g., `add-communication-scriptures`).
3.  **Add or Modify Data:**
    *   Add new JSON files or entries to existing files within the appropriate `/data` subdirectory (e.g., `/data/scripture`, `/data/counseling`).
    *   Ensure your data adheres strictly to the format defined in `docs/data_schema.json`.
    *   Provide clear `source_reference` information.
    *   Use concise but informative `content_summary` and detailed `content_detailed` fields.
    *   Add relevant `keywords`.
    *   Set the `moderation_status` in the metadata to `Pending`.
4.  **Commit Changes:** Commit your changes with clear and descriptive messages.
5.  **Submit a Pull Request:** Open a PR from your branch to the `main` branch of the original repository.
    *   Clearly describe the changes you made and the sources used.

## Data Format and Schema

All data must conform to the JSON schema defined in `docs/data_schema.json`. Please validate your JSON before submitting.

Key fields to pay attention to:

*   `entry_id`: Create a unique and descriptive ID.
*   `topic`: Assign relevant topic(s).
*   `source_type` and `source_reference`: Accurately document the origin of the information.
*   `content_summary` and `content_detailed`: Provide clear and distinct summaries and detailed explanations.
*   `metadata`: Fill in creation date, contributor name, and set `moderation_status` to `Pending`.

## Moderation Process

1.  **Submission:** Contributors submit data via Pull Requests.
2.  **Review:** Designated moderators will review the submitted PR.
    *   **Accuracy:** Verify the faithfulness of the content to the cited source and alignment with Christian doctrine (as understood within the project's scope).
    *   **Formatting:** Ensure the data conforms to the JSON schema.
    *   **Clarity:** Check for clear and understandable language in summaries and details.
    *   **Duplication:** Check for significant overlap with existing entries.
3.  **Feedback/Approval:**
    *   If changes are needed, moderators will provide feedback via PR comments.
    *   If the contribution meets the criteria, the moderator will approve the PR, update the `moderation_status` to `Approved`, and merge it into the `main` branch.
4.  **Rejection:** Contributions may be rejected if they are significantly out of scope, inaccurate, poorly formatted, or cannot be verified.

## Scope

The primary focus is on relationship advice, principles, and interpretations grounded in Christian doctrine. While drawing from various sources (scripture, theology, counseling), the content should maintain this focus.

## Questions?

If you have questions about the contribution process or data format, please open an issue in the repository.

