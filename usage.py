from IntelliPatch import IntelliPatchSystem

# Example query and initial response from a language model
query = "What is the future of AI in healthcare?"
initial_response = "The future of AI in healthcare includes unrelated content and contradictory statements."

# Initialize IntelliPatch
system = IntelliPatchSystem()

# Process the initial response to refine and correct nonsensical elements
final_response = system.process_response(query, initial_response)
print("Final Corrected Response:", final_response)
