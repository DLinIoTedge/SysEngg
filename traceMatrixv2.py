
# Define actual data for each field
data = {
    'Requirement ID': 'REQ123',
    'Type': 'Functional',
    'Description': 'This is a sample requirement',
    'Test case ID': 'TC001',
    'Test Design Status': 'In Progress',
    'Test Execution Run and Status': 'Not Started',
    'Unit Tests': 'Passed',
    'Integration Tests': 'Not Run',
    'System Tests': 'Not Run',
    'User Acceptance Testing Status': 'Not Started',
    'Defects, list': 'No defects',
    'Defect Status': 'N/A',
}

# Define groups
requirement_fields = ['Requirement ID', 'Type', 'Description']
test_fields = [
    'Test case ID',
    'Test Design Status',
    'Test Execution Run and Status',
    'Unit Tests',
    'Integration Tests',
    'System Tests',
    'User Acceptance Testing Status',
    'Defects, list',
    'Defect Status',
]

# Create an empty traceability matrix
traceability_matrix = {requirement: {test: 'Not Covered' for test in test_fields} for requirement in requirement_fields}

# Fill in the traceability matrix based on the actual data
for requirement in requirement_fields:
    for test in test_fields:
        if data.get(test) == requirement:
            traceability_matrix[requirement][test] = 'Covered'

# Print the traceability matrix
print("Traceability Matrix:")
print("\t" + "\t".join(test_fields))
for requirement in requirement_fields:
    print(requirement + "\t" + "\t".join(traceability_matrix[requirement].values()))
    
    
    


# Print the traceability matrix
print("Traceability Matrix:")
print("\t" + "\t".join(requirement_fields))  # Print requirements on the horizontal axis
for test in test_fields:
    print(test, end="\t")
    for requirement in requirement_fields:
        print(traceability_matrix[requirement][test], end="\t")
    print()


