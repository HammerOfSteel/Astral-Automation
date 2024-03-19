from fastapi import FastAPI, BackgroundTasks
from typing import Dict
from random import choices
import json
import os
import io
import csv

# Assume `interpretations` dictionary is already defined as provided.
# Assume `issues_data` is loaded from 'agile_fengShui.json'

app = FastAPI()

# Load the JSON data with the issues
with open('agile_fengShui.json', 'r') as file:
    issues_data = json.load(file)

# Interpret the hexagram
def interpret_hexagram(number):
    """
    Provide a basic interpretation of the hexagram based on its number.
    This is a simplified interpretation.
    """
    interpretations = {
    1: "Software Development: Embrace leadership in a groundbreaking development project.",
    2: "Infrastructure and Security: Adapt your infrastructure to support a major new initiative.",
    3: "Project and Product Management: Navigate initial challenges in a complex project.",
    4: "Innovation and Learning: Mentor new team members or adopt new learning resources.",
    5: "Monitoring and Operations: Strategically plan for system scalability and robustness.",
    6: "Testing and Quality Assurance: Resolve conflicts or bugs discovered in testing phases.",
    7: "Deployment and Integration: Organize and deploy a critical update or new system feature.",
    8: "Collaboration and Communication: Strengthen team unity and improve collaborative processes.",

    9: "Software Development: Focus on small but crucial code improvements.",
    10: "Infrastructure and Security: Tread carefully while implementing new security measures.",
    11: "Project and Product Management: Enjoy a phase of harmony and productivity in project management.",
    12: "Innovation and Learning: Identify and pause unproductive approaches or technologies.",
    13: "Monitoring and Operations: Foster better communication within operations teams.",
    14: "Testing and Quality Assurance: Capitalize on abundant resources to enhance testing processes.",
    15: "Deployment and Integration: Emphasize humility and careful planning in your deployment strategy.",
    16: "Collaboration and Communication: Harness team enthusiasm for an upcoming project launch.",

    17: "Software Development: Adapt development practices following team or leadership changes.",
    18: "Infrastructure and Security: Address and rectify legacy issues in your infrastructure.",
    19: "Project and Product Management: Approach new project phases with careful planning.",
    20: "Innovation and Learning: Take time to reflect on recent technological advancements.",
    21: "Monitoring and Operations: Act decisively to resolve a critical system issue.",
    22: "Testing and Quality Assurance: Focus on refining the aesthetics and user interface of a product.",
    23: "Deployment and Integration: Be cautious of potential breakdowns during system integration.",
    24: "Collaboration and Communication: Celebrate a return to effective team communication.",

    25: "Software Development: Maintain an honest and straightforward approach in coding practices.",
    26: "Infrastructure and Security: Control and manage the resources effectively for a major upgrade.",
    27: "Project and Product Management: Focus on nurturing client relationships and user feedback.",
    28: "Innovation and Learning: Tackle significant challenges with innovative solutions.",
    29: "Monitoring and Operations: Stay vigilant and persistent in monitoring challenging situations.",
    30: "Testing and Quality Assurance: Shine a light on the most critical testing needs.",
    31: "Deployment and Integration: Influence your deployment strategy with subtle, careful adjustments.",
    32: "Collaboration and Communication: Establish long-term team goals and stable communication practices.",

    33: "Software Development: Strategically withdraw from outdated development practices.",
    34: "Infrastructure and Security: Assertively upgrade system infrastructure for enhanced performance.",
    35: "Project and Product Management: Make visible progress in your project management approach.",
    36: "Innovation and Learning: Protect innovative ideas during challenging times for the organization.",
    37: "Monitoring and Operations: Focus on the family of services and their health.",
    38: "Testing and Quality Assurance: Address opposing views or conflicts within QA processes.",
    39: "Deployment and Integration: Navigate around obstacles in your integration strategy.",
    40: "Collaboration and Communication: Liberate your team from communication barriers.",

    41: "Software Development: Decrease complexity in your code for better maintainability.",
    42: "Infrastructure and Security: Expand and enrich your IT infrastructure effectively.",
    43: "Project and Product Management: Make decisive moves to advance project goals.",
    44: "Innovation and Learning: Be cautious about hastily adopting unproven technologies.",
    45: "Monitoring and Operations: Gather your team to address a critical operational issue.",
    46: "Testing and Quality Assurance: Progress steadily in improving your testing methodologies.",
    47: "Deployment and Integration: Overcome constraints in resource-limited deployment scenarios.",
    48: "Collaboration and Communication: Deepen team knowledge and shared understanding.",
    
    49: "Software Development: Initiate transformative changes in your development approach.",
    50: "Infrastructure and Security: Utilize innovative strategies for system optimization and security.",
    51: "Project and Product Management: Address sudden changes or challenges in your projects.",
    52: "Innovation and Learning: Emphasize the importance of focus and discipline in learning new technologies.",
    53: "Monitoring and Operations: Develop gradual improvements in system monitoring and operational efficiency.",
    54: "Testing and Quality Assurance: Adapt to changing roles or requirements in the QA process.",
    55: "Deployment and Integration: Manage and utilize abundant resources for efficient system integration.",
    
    56: "Collaboration and Communication: Navigate through unfamiliar team dynamics or external partnerships.",
    57: "Software Development: Apply gentle but persistent efforts to improve coding practices.",
    58: "Infrastructure and Security: Foster a positive and open environment for discussing security concerns.",
    59: "Project and Product Management: Disperse any misunderstandings and align on project objectives.",
    60: "Innovation and Learning: Set clear boundaries for experimenting with new technologies.",
    61: "Monitoring and Operations: Focus on transparency and truthfulness in reporting system performance.",
    62: "Testing and Quality Assurance: Pay attention to minor but crucial details in your testing processes.",
    63: "Deployment and Integration: Successfully complete deployments, but remain vigilant for any minor issues.",
    64: "Collaboration and Communication: Prepare for future challenges and changes in team dynamics or communication."
    }
    return interpretations.get(number, "Interpretation not available.")

# Function to flip coins and determine the hexagram
def flip_coins():
    return [sum(choices([2, 3], k=3)) for _ in range(6)]

def calculate_hexagram_number(flips):
    return int(''.join(['0' if flip in [6, 8] else '1' for flip in flips]), 2)

def get_opposite_hexagram(hexagram):
    return hexagram ^ 0b111111  # XOR with 63 to flip all bits

def get_nuclear_hexagram(hexagram):
    # Shift to get the inner four trigrams, which form the nuclear hexagram
    nuclear = ((hexagram >> 1) & 0b000111) | ((hexagram & 0b111000) << 1)
    return nuclear

def get_mutual_hexagram(hexagram):
    # The first line becomes the last, and all others move up one position
    mutual = ((hexagram & 0b001001) << 2) | (hexagram & 0b010010) | ((hexagram & 0b100100) >> 2)
    return mutual

def get_issues(hexagram):
    return issues_data[str(hexagram)]

def generate_sprints(i):
    if i == 0:
        i = 1

    sprint_data = {}
    
    # Week 1: Random hexagrams
    week1_hexagrams = [calculate_hexagram_number(flip_coins()) for _ in range(4)]
    sprint_data['week1'] = {
        'hexagrams': {hexagram: interpret_hexagram(hexagram) for hexagram in week1_hexagrams},
        'issues': {hexagram: get_issues(hexagram) for hexagram in week1_hexagrams}
    }
    
    # Week 2: Mutual hexagrams from week 1
    week2_hexagrams = [get_mutual_hexagram(hexagram) for hexagram in week1_hexagrams]
    sprint_data['week2'] = {
        'hexagrams': {hexagram: interpret_hexagram(hexagram) for hexagram in week2_hexagrams},
        'issues': {hexagram: get_issues(hexagram) for hexagram in week2_hexagrams}
    }
    
    week3_hexagrams = []
    for hexagram in week2_hexagrams:
        nuclear_hex = get_nuclear_hexagram(hexagram)
        # Validate the nuclear hexagram is within the valid range, adjust if not.
        valid_nuclear_hex = nuclear_hex if 1 <= nuclear_hex <= 64 else (nuclear_hex % 64) + 1
        week3_hexagrams.append(valid_nuclear_hex)
        if len(week3_hexagrams) == 4:
            break  # Stop when we have 4 nuclear hexagrams

    sprint_data['week3'] = {
        'hexagrams': {hexagram: interpret_hexagram(hexagram) for hexagram in week3_hexagrams},
        'issues': {hexagram: get_issues(hexagram) for hexagram in week3_hexagrams}
    }
        
    # Week 4: Opposite hexagrams from week 1
    week4_hexagrams = [get_opposite_hexagram(hexagram) for hexagram in week1_hexagrams]
    sprint_data['week4'] = {
        'hexagrams': {hexagram: interpret_hexagram(hexagram) for hexagram in week4_hexagrams},
        'issues': {hexagram: get_issues(hexagram) for hexagram in week4_hexagrams}
    }
    
    # save sprint data to file
    with open(f'./UI/data/sprints_{i}.json', 'w') as file:
        json.dump(sprint_data, file)
    
    return sprint_data

async def read_data(i: int) -> Dict:
    with open(f'./UI/data/sprints_{i}.json', 'r') as file:
        data = json.load(file)
    return data

def generate_azure_devops_csv(sprint_data: Dict) -> str:
    headers = ["ID", "Work Item Type", "State", "Assigned To", "Title", "Tags"]
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(headers)
    
    issue_id = 1043  # Starting issue ID
    for week, details in sprint_data.items():
        for hex_key, hex_info in details['hexagrams'].items():
            # Write the Epic for the hexagram
            writer.writerow([issue_id, "Epic", "To Do", "", f"Hexagram {hex_key}: {hex_info}", ""])
            issue_id += 1
            
            # Iterate over the issues for each hexagram
            for issue in details['issues'][hex_key]['issues']:
                # Here, issue is expected to be a dictionary with 'element' and 'description'
                writer.writerow([issue_id, "Issue", "To Do", "", issue['description'], issue['element']])
                issue_id += 1

    csv_content = output.getvalue()
    output.close()
    return csv_content


@app.get("/export-azure-devops")
async def export_azure_devops(background_tasks: BackgroundTasks):
    # In a real scenario, fetch data asynchronously and properly await it
    for i in range(1, 5):  # Assuming you have 4 sprints to export
        sprint_data = await read_data(i)  # Properly await the async function
        csv_content = generate_azure_devops_csv(sprint_data)
        
        # Save the CSV content to a file
        directory_path = f'./UI/data/export/azure/'

        # Check if the directory exists, and create it if it doesn't
        os.makedirs(directory_path, exist_ok=True)

        # Now, safely write the CSV content to the file
        with open(f'{directory_path}sprints_{i}.csv', 'w') as file:
            file.write(csv_content)
        
        # For demonstration, printing CSV content to console. In practice, save or return this content.
        print(f"Sprint {i} Azure DevOps CSV:\n{csv_content}\n")
        
    return {"message": "Sprints exported to Azure DevOps format."}

# Route to generate sprints for 4 weeks
@app.get("/generate-sprints")
async def save_sprints():
    for i in range(5):
        generate_sprints(i)
    return {"message": "Sprints generated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
