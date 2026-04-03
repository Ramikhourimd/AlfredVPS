# Step-by-Step Guide: Installing Alfred (MoAI-ADK) with Claude Code

This guide provides a comprehensive walkthrough for installing and configuring Claude Code with the MoAI-ADK (Modular AI Agent Development Kit), which provides the "Alfred the Butler" orchestration layer. This setup enhances Claude Code with a powerful framework of specialized AI agents and skills, enabling more structured and efficient AI-driven development.

## Introduction

**Claude Code** is an agentic coding assistant from Anthropic that helps with various development tasks directly in your terminal [1]. **MoAI-ADK**, often referred to as "Alfred," is an open-source framework that acts as a strategic orchestrator for Claude Code. Instead of handling all tasks itself, it intelligently delegates them to a team of specialized AI agents, such as `expert-backend` or `manager-tdd`, to improve the quality and structure of the output [2].

This guide will walk you through the necessary prerequisites and the installation process for both tools.

## Prerequisites

Before you begin the installation, please ensure your system meets the following requirements for both Claude Code and MoAI-ADK.

| Requirement | Specification |
| :--- | :--- |
| **Operating System** | macOS 13.0+, Windows 10 1809+, Ubuntu 20.04+, Debian 10+ |
| **Hardware** | 4 GB RAM or more |
| **Python** | Version 3.11 or newer (for MoAI-ADK) |
| **Windows Specific** | Git for Windows must be installed [3] |
| **Claude Account** | A paid subscription is required (Pro, Max, Teams, or Enterprise). The free Claude.ai plan does not include Claude Code access [4]. |

## Step 1: Install Claude Code

Claude Code must be installed first. The recommended method is the native installer, which is fast and handles updates automatically. The previous `npm` based installation is now deprecated [5].

Choose the command that corresponds to your operating system:

*   **macOS, Linux, or Windows Subsystem for Linux (WSL):**

    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

*   **Windows (PowerShell):**

    ```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

After installation, you must log in to your Anthropic account. Run the following command in your terminal and follow the browser-based authentication prompts:

```bash
claude
```

This only needs to be done once. Your credentials will be stored for future sessions.

## Step 2: Install MoAI-ADK (Alfred)

With Claude Code installed, you can now install the MoAI-ADK. This is a single binary written in Go with zero dependencies, making for a simple installation.

*   **macOS, Linux, or WSL:**

    ```bash
    curl -fsSL https://raw.githubusercontent.com/modu-ai/moai-adk/main/install.sh | bash
    ```

*   **Windows (PowerShell 7.x+):**

    ```powershell
    irm https://raw.githubusercontent.com/modu-ai/moai-adk/main/install.ps1 | iex
    ```

This script will detect your platform and install the appropriate binary.

## Step 3: Initialize Your Project with MoAI-ADK

Once MoAI-ADK is installed, you need to initialize it within your project directory. This is done using the `moai init` command, which launches an interactive setup wizard.

1.  Navigate to your project's root directory in the terminal:

    ```bash
    cd /path/to/your/project
    ```

2.  Run the initialization command:

    ```bash
    moai init
    ```

3.  The wizard will guide you through a 9-step configuration process, which includes [6]:
    *   Selecting your preferred language for communication.
    *   Setting up your project name and Git integration mode.
    *   Configuring the output language for commit messages and code comments.

This process creates a `.moai` directory in your project, containing the configuration files that tailor the behavior of the Alfred orchestrator.

## Getting Started

With the installation and initialization complete, you can now start using the `/moai` commands within a Claude Code session. Launch Claude Code from your project directory:

```bash
claude
```

From here, you can use the MoAI-ADK workflow commands to manage your project:

*   `/moai project`: Generate documentation for your project (product, structure, tech).
*   `/moai plan "Your task description"`: Create a detailed SPEC document for a new feature or task.
*   `/moai run SPEC-ID`: Begin implementation based on the created SPEC, using the appropriate development methodology (TDD or DDD).
*   `/moai sync SPEC-ID`: Sync documentation and create a pull request upon completion.

This structured workflow, orchestrated by Alfred (MoAI-ADK), ensures high-quality, well-documented code.

## References

[1] Claude Code Docs. (n.d.). *Quickstart*. Retrieved from https://code.claude.com/docs/en/quickstart

[2] GitHub - modu-ai/moai-adk. (n.d.). *MoAI - Agentic Development Kit*. Retrieved from https://github.com/modu-ai/moai-adk

[3] Claude Code Docs. (n.d.). *Advanced setup*. Retrieved from https://code.claude.com/docs/en/setup

[4] Anthropic. (n.d.). *Claude Pro*. Retrieved from https://www.anthropic.com/claude-pro

[5] Claude Code Docs. (n.d.). *Advanced setup - Deprecated npm installation*. Retrieved from https://code.claude.com/docs/en/setup#deprecated-npm-installation

[6] PyPI. (n.d.). *moai-adk*. Retrieved from https://pypi.org/project/moai-adk/
