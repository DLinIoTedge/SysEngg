

class TraceabilityMatrix:
    def __init__(self, requirements, designs, test_cases, source_code):
        self.requirements = requirements
        self.designs = designs
        self.test_cases = test_cases
        self.source_code = source_code

    def generate_traceability_matrix(self):
        matrix = [["Requirement", "Design", "Test Case", "Source Code"]]

        for req in self.requirements:
            matrix.append([req, "", "", ""])

        for i in range(len(self.designs)):
            matrix[i + 1][1] = self.designs[i]

        for i in range(len(self.test_cases)):
            matrix[i + 1][2] = self.test_cases[i]

        for i in range(len(self.source_code)):
            matrix[i + 1][3] = self.source_code[i]

        return matrix


# Example Usage:
requirements_list = ["REQ-001", "REQ-002", "REQ-003"]
designs_list = ["Design-001", "Design-002", "Design-003"]
test_cases_list = ["TC-001", "TC-002", "TC-003"]
source_code_list = ["Code-001", "Code-002", "Code-003"]

traceability_matrix_generator = TraceabilityMatrix(requirements_list, designs_list, test_cases_list, source_code_list)
traceability_matrix = traceability_matrix_generator.generate_traceability_matrix()

# Print the generated traceability matrix
for row in traceability_matrix:
    print(row)




