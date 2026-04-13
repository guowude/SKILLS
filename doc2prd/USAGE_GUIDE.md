# Usage Guide for doc2prd Tool

The `doc2prd` tool is designed for creating and managing product requirement documents (PRDs) efficiently. This guide provides step-by-step instructions, input requirements, output structures, examples, and best practices to help you get started.

## Step-by-Step Instructions

### Step 1: Installation

Ensure you have the required dependencies installed. You can install `doc2prd` via npm or download it directly from the repository:

```bash
npm install doc2prd
```

### Step 2: Preparing Input

Prepare your input in the required format. The tool accepts input in either Markdown or structured text format. Here’s a basic example:

```markdown
# Product Title

## Overview
- Brief description of the product.

## Features
- Feature 1
- Feature 2
```

Make sure your input document includes the following sections:
- Product Title
- Overview
- Features
- User Stories (if applicable)

### Step 3: Running the Tool

Once your input is ready, run the tool using the following command:

```bash
doc2prd input-file.md output-file.prd
```

Replace `input-file.md` with the path to your input file and `output-file.prd` with your desired output filename.

### Step 4: Reviewing Output

The output will be a structured PRD file based on your input. Review the structure to ensure all necessary information has been included.

## Input Requirements

- Input format: Markdown or structured text
- Minimum sections required: Title, Overview, Features
- Optional sections: User Stories, Acceptance Criteria

## Output Structure

The tool generates a `.prd` file with the following structure:
- Title: (from input)
- Overview: (from input)
- Features: (listed from input)
- User Stories: (if provided)
- Appendices: (optional)

## Examples

```bash
doc2prd example-input.md example-output.prd
```

Example input markdown:

```markdown
# Sample Product

## Overview
This product solves X by...

## Features
- Feature A
- Feature B
```

## Best Practices
- Keep your input structured and clean for best output results.
- Use comments in your markdown to annotate sections clearly.
- Regularly update your PRD based on team feedback.

By following this guide, you can effectively utilize the `doc2prd` tool to streamline your PRD creation process. Happy documenting!