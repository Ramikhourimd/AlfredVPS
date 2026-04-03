# Your Comprehensive Guide to Installing and Using Alfred (Claude Code Edition)

Hello! Following up on our discussion about security, I have rewritten the entire guide from the ground up. This version focuses exclusively on the safest and most straightforward path for running Alfred locally: using **Claude Code** as the AI backend.

This approach avoids the security complexities of OpenClaw while still giving you the powerful, self-organizing knowledge base you’re looking for. We will still cover the one-click AlfredOS cloud deployment as a simpler alternative, but the main focus will be on the secure, local Alfred Vault setup.

Let's begin!

---

## The Two Paths to Alfred: A Quick Overview

1.  **Path A: Alfred Vault with Claude Code (Recommended)**: This is a powerful, secure, and local-first setup. It integrates the Alfred command-line tools directly with your Obsidian vault and uses the sandboxed Claude Code CLI as its brain. This is the path we will focus on in this guide.

2.  **Path B: AlfredOS on Railway (The Easy Cloud Option)**: This is an all-in-one, cloud-based platform that bundles a chat assistant with several useful applications (n8n, Ghost, etc.). It’s a great starting point if you want a simple, managed environment without a local setup.

---

## Path A: Alfred Vault with Claude Code (The Secure, Local-First Way)

This is the recommended path for turning your local Obsidian notes into an intelligent, self-organizing knowledge base. It uses the official Claude Code CLI, which is sandboxed and doesn’t require exposing any services to the internet, making it a much more secure choice.

### What It Is

The Alfred Vault suite consists of four main tools that run on your local machine, watching and improving your notes in the background [1]:

| Tool | Description |
| :--- | :--- |
| **Curator** | Watches your `inbox/` folder and automatically processes new notes, transcripts, and emails. It extracts entities (people, projects, companies), links them to existing notes, and enriches them with information. |
| **Janitor** | Periodically scans your entire vault for issues like broken links, missing information, or empty notes, and uses an AI agent to fix them. |
| **Distiller** | Reads your notes and conversations to identify and extract higher-level knowledge, such as decisions, assumptions, and contradictions, creating a structured graph of your reasoning. |
| **Surveyor** | Embeds your notes into vectors to understand their semantic meaning, then clusters related notes and automatically tags them, revealing hidden connections in your knowledge. |

### Step 1: Prerequisites

This setup has a few key requirements:

1.  **Python 3.11 or later**.
2.  **An Obsidian Vault**: A local folder on your computer that you use as your Obsidian vault.
3.  **Claude Code CLI**: This is the official command-line tool from Anthropic.
4.  **A Claude Max Subscription**: To handle the volume of tasks Alfred will delegate, a subscription to the Claude Max plan is strongly recommended. The Pro plan has lower usage limits that you will likely hit quickly. As of early 2026, the Max plan starts at around $100/month [2].
5.  **(Optional) For the Surveyor Tool**: To enable the most advanced features for finding connections between your notes, you will also need:
    *   **Ollama**: A tool for running embedding models locally. You can download it from [ollama.com](https://ollama.com/).
    *   **An OpenRouter API Key**: The Surveyor uses this for labeling the clusters it finds. You can get a free key from [OpenRouter.ai](https://openrouter.ai/).

### Step 2: Install and Configure Claude Code

First, let's get the brain of our operation set up.

1.  **Install the Claude Code CLI**: Open your terminal and run the official installer script [3]:

    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

2.  **Log In to Your Anthropic Account**: Authenticate the CLI with your Claude account.

    ```bash
    claude login
    ```

    This will open a browser window for you to log in. This is how Alfred gets its permissions securely, without needing you to handle API keys directly for the core tools.

3.  **Verify the Installation**: Check that the CLI is installed and on your system's PATH.

    ```bash
    claude --version
    ```

### Step 3: Install and Configure Alfred Vault

Now, we install the Alfred tools themselves.

1.  **Install Alfred Vault**: We recommend installing with the `[all]` extra to include the dependencies for the Surveyor tool.

    ```bash
    pip install "alfred-vault[all]"
    ```

2.  **Run the Quickstart Wizard**: This interactive wizard is the easiest way to get everything configured.

    ```bash
    alfred quickstart
    ```

    The wizard will ask you a series of questions:
    *   **Vault Path**: Point it to your existing Obsidian vault folder.
    *   **Agent Backend**: This is the most important step. When prompted, **select `claude`** as your agent backend.
    *   **Surveyor Setup**: If you installed Ollama and have an OpenRouter key, you can configure the Surveyor here.

    The wizard will then automatically create the necessary folder structure in your vault (`inbox/`, `person/`, `project/`, etc.) and generate your `config.yaml` and `.env` files.

### Step 4: Verify the Configuration

Let's double-check that Alfred is set to use Claude Code.

1.  **Open `config.yaml`**: This file will be in the directory where you ran the quickstart (or in `~/.config/alfred/`).
2.  **Check the `agent` section**: It should look like this, confirming that `claude` is the backend [4].

    ```yaml
    agent:
      backend: "claude"
      claude:
        command: "claude"
        args: ["-p"]
        timeout: 600
    ```

3.  **(Optional) Configure `.env`**: If you are using the Surveyor, open the `.env` file and add your OpenRouter API key:

    ```
    OPENROUTER_API_KEY=sk-or-...
    ```

### Step 5: Run Alfred

With everything configured, starting Alfred is a single command. Unlike other setups, you do not need to run a separate gateway or server.

```bash
alfred up --live
```

This command starts all four Alfred daemons in the background and launches a beautiful terminal dashboard. In this live view, you can see the tools waking up, scanning your notes, and processing information in real-time.

### Step 6: Using Your Alfred-Powered Vault

Your workflow is now supercharged. You can simply use Obsidian as you normally would, but with an AI assistant working tirelessly for you.

*   **Drop files into `inbox/`**: Save an email, a meeting transcript, or a quick note into the `inbox` folder. Alfred's **Curator** will see it, use Claude Code to analyze it, create structured notes, and link it to relevant people and projects.
*   **Write Messy Notes**: Don't worry about perfect formatting. The **Janitor** will periodically scan your vault and use Claude Code to fix broken links, fill in missing metadata, and enrich your notes.
*   **Discover Hidden Connections**: Over time, the **Distiller** and **Surveyor** will build a rich, interconnected graph of your knowledge, helping you discover insights and patterns you never would have seen otherwise.

This setup gives you the full power of Alfred in a secure, local-first environment. Enjoy your new AI-powered personal knowledge system!

---

### References
[1] David Szabo-Stuban. (n.d.). *alfred* [GitHub repository]. Retrieved from https://github.com/ssdavidai/alfred

[2] Inventive. (2026, February 13). *Claude Code Pricing Explained: Pro vs Max vs API*. Retrieved from https://inventivehq.com/blog/claude-code-pricing-explained

[3] Anthropic. (n.d.). *Set up Claude Code*. Claude Code Docs. Retrieved from https://code.claude.com/docs/en/setup

[4] David Szabo-Stuban. (n.d.). *config.yaml.example*. alfred GitHub repository. Retrieved from https://raw.githubusercontent.com/ssdavidai/alfred/master/config.yaml.example
