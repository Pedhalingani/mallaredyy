# Function to compute the result of the logical gate operation
def compute_gate_output(gate_type, input1, input2):
    if gate_type == 'AND':
        return input1 & input2
    elif gate_type == 'OR':
        return input1 | input2
    elif gate_type == 'NAND':
        return 1 - (input1 & input2)  # NOT (input1 AND input2)
    elif gate_type == 'NOR':
        return 1 - (input1 | input2)  # NOT (input1 OR input2)
    elif gate_type == 'XOR':
        return input1 ^ input2
    else:
        raise ValueError("Unknown gate type")

def solve():
    # Read the number of gates
    N = int(input().strip())
    
    # Create a dictionary to store gate operations
    gates = {}
    
    # Read the gates' details
    for _ in range(N):
        gate_line = input().strip()
        gate_name, gate_operation = gate_line.split('=')
        gate_type, inputs = gate_operation.split('(')
        input1, input2 = inputs[:-1].split(',')
        gates[gate_name.strip()] = {
            'operation': gate_type.strip(),
            'inputs': (input1.strip(), input2.strip())
        }
    
    # Read the number of cycles
    T = int(input().strip())
    
    # Read the input variables
    inputs = {}
    for _ in range(T):
        input_line = input().strip().split()
        var_name = input_line[0]
        values = list(map(int, input_line[1:]))
        inputs[var_name] = values
    
    # Read the name of the gate whose output is required
    target_gate = input().strip()
    
    # Initialize the output dictionary for gates
    gate_outputs = {gate: [0] * T for gate in gates}
    
    # Start calculating the outputs for each gate
    for cycle in range(1, T):
        # For each gate, calculate its output based on its inputs from previous cycle
        for gate, info in gates.items():
            input1, input2 = info['inputs']
            # Get the value for input1 and input2 at the previous cycle (cycle - 1)
            input1_value = inputs[input1][cycle - 1] if input1 in inputs else gate_outputs[input1][cycle - 1]
            input2_value = inputs[input2][cycle - 1] if input2 in inputs else gate_outputs[input2][cycle - 1]
            gate_outputs[gate][cycle] = compute_gate_output(info['operation'], input1_value, input2_value)
    
    # Output the result for the target gate
    print(" ".join(map(str, gate_outputs[target_gate])))

