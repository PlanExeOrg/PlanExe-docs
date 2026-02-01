# Agents

This document describes the different types of contributors ("agents") who can help improve PlanExe and how to get started in each role.

## Overview

PlanExe is an open-source project that benefits from contributions across multiple disciplines. Whether you're a developer, designer, or domain expert, there's a way for you to contribute.

## Getting Started

1. Join the [PlanExe Discord](https://planexe.org/discord) and introduce yourself
2. Browse the [GitHub repository](https://github.com/PlanExeOrg/PlanExe) to understand the codebase
3. Check open issues and discussions to find areas where you can help
4. Start with small contributions to get familiar with the project

## Agent Types

### Python Developer

**What you'll do:**
- Develop and maintain the core Python codebase
- Implement new features and fix bugs
- Improve code quality, performance, and maintainability
- Write and maintain tests
- Review pull requests from other contributors

**Skills needed:**
- Python programming experience
- Familiarity with LlamaIndex (or willingness to learn)
- Understanding of AI/LLM integrations
- Experience with software development best practices

**Where to start:**
- Review the codebase structure in the main repository
- Look for issues labeled `good first issue` or `help wanted`
- Check the existing code style and patterns
- Start with small bug fixes or documentation improvements

**Key areas:**
- Core planning logic
- AI provider integrations (OpenRouter, Ollama, LM Studio)
- Report generation and templating
- CLI and user interface
- Testing infrastructure

### Prompt Engineer

**What you'll do:**
- Design and refine system prompts for better plan generation
- Optimize prompts for different use cases and industries
- Test and validate prompt changes
- Document prompt strategies and best practices
- Collaborate with developers to integrate prompt improvements

**Skills needed:**
- Understanding of LLM behavior and prompt engineering
- Ability to write effective prompts
- Understanding of different AI models and their characteristics
- Analytical skills to evaluate prompt effectiveness

**Where to start:**
- Review existing prompts in the codebase
- Test current prompts with various inputs
- Experiment with prompt variations
- Document your findings and suggestions

**Key areas:**
- System prompts for plan generation
- Prompt templates for different plan types
- Error handling and edge case prompts
- User instruction processing

### Project Manager

**What you'll do:**
- Provide feedback on what's missing in generated plans
- Identify gaps in the planning process
- Suggest improvements to plan structure and content
- Test the tool with real-world scenarios
- Help prioritize features and improvements

**Skills needed:**
- Experience with project planning and management
- Understanding of business planning processes
- Ability to evaluate plan quality and completeness
- Communication skills to provide clear feedback

**Where to start:**
- Use PlanExe to generate plans for real or hypothetical projects
- Document what works well and what's missing
- Compare generated plans with your own planning experience
- Share feedback through GitHub issues or Discord

**Key areas:**
- Plan completeness and structure
- Missing sections or information
- Real-world usability testing
- Feature prioritization
- Documentation improvements

### Designer

**What you'll do:**
- Improve the visual design of generated reports
- Create better report templates and layouts
- Enhance user interface and user experience
- Design icons, graphics, and visual elements
- Ensure consistent branding and visual identity

**Skills needed:**
- Graphic design skills
- Understanding of typography and layout
- Experience with design tools (Figma, Adobe Creative Suite, etc.)
- Knowledge of print and digital design best practices
- Understanding of user experience principles

**Where to start:**
- Review current report templates
- Identify areas for visual improvement
- Create mockups or prototypes of improved designs
- Share your designs for feedback

**Key areas:**
- Report template design (HTML/CSS)
- Visual hierarchy and readability
- Brand consistency
- User interface improvements
- Icon and graphic design

## Contribution Workflow

1. **Find an area of interest** - Choose a role that matches your skills
2. **Join the community** - Introduce yourself on Discord
3. **Pick a task** - Start with small, well-defined tasks
4. **Create a branch** - Work on your changes in a feature branch
5. **Submit a pull request** - Share your work for review
6. **Iterate** - Incorporate feedback and improve

## Communication

- **Discord**: For real-time discussions and questions
- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For longer-form discussions and proposals
- **Pull Requests**: For code and documentation contributions

## Code of Conduct

All contributors are expected to:
- Be respectful and inclusive
- Welcome newcomers and help them get started
- Provide constructive feedback
- Follow the project's coding standards and guidelines

## Recognition

Contributors are recognized through:
- GitHub contributor list
- Release notes for significant contributions
- Community appreciation on Discord

## Questions?

If you're unsure where to start or have questions:
1. Check the [GitHub repository](https://github.com/PlanExeOrg/PlanExe) for documentation
2. Ask on [Discord](https://planexe.org/discord)
3. Open a GitHub Discussion for longer questions

---

**Ready to contribute?** Join us on [Discord](https://planexe.org/discord) and let's build better planning tools together!

## Docs conventions (PlanExe-docs)

- **Tone**: keep docs factual and direct; avoid marketing language.
- **Social cards**: configured in `mkdocs.yml` via the `social` plugin; titles come from page front matter (`title:`) when needed.
- **Branding**: social cards use the PlanExe logo from `PlanExe/docs/assets/logo.svg` (copied during build).
