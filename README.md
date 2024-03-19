# Astral Automation Project Management Tool

## Description
Astral Automation is a dynamic project management tool designed to generate and visualize sprints following the principles of the I Ching hexagrams, infused with DevOps best practices, and inspired by Feng Shui elements. This web application provides a dashboard view and a detailed sprint view with the capability of exporting the generated sprints to various formats such as CSV for Azure DevOps, Jira, ServiceNow, or pure JSON.

## Features
- **Dashboard View:** Presents an overview of the project with a tranquil pond effect in the background.
- **Sprint View:** Displays the sprints in a multi-carousel format, with each sprint linked to a detailed modal view.
- **Export Functionality:** Offers the capability to export the entire project into different formats suitable for integration with popular project management tools.
- **Dynamic Sprint Modals:** Generates detailed sprint information dynamically with a visually appealing interface.

## Demo setup
- Clone this repo
- From the root folder run:
docker build . -f ./dockerfile -t astral_automation --no-cache
docker run -d -p 8000:8000 -t astral_automation