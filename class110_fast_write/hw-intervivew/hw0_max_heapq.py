import sys
import heapq

def dynamic_priority_experience_replay():
    """
     solves the dynamic priority experience replay problem.
    """
    try:
        # Read all lines at once to easily check for N mismatch
        lines = sys.stdin.readlines()
        if not lines:
            print("null")
            return

        # The first line is N
        n_str = lines[0].strip()
        if not n_str:
            print("null")
            return
        N = int(n_str)

        operations = lines[1:]

        # Validate if the number of operations matches N
        if N != len(operations):
            print("null")
            return

        # A dictionary to store the master list of all experiences and their latest scores.
        # Provides O(1) access for updates.
        all_experiences = {}

        # A min-heap to efficiently get the top K experiences.
        # We store (-score, id) to simulate a max-heap on score,
        # with id as a tie-breaker (ascending).
        active_pool = []

        # To store the results of each 'extract' operation
        outputs = []
        has_extract_op = False

        for line in operations:
            parts = line.strip().split()
            if not parts:
                continue

            op = parts[0]

            if op == '+':
                # Insert operation: + id score
                _, id_str, score_str = parts
                exp_id = int(id_str)
                score = int(score_str)

                # Add to master list
                all_experiences[exp_id] = score
                # Add to the currently available pool
                heapq.heappush(active_pool, (-score, exp_id))

            elif op == '=':
                # Update operation: = id newScore
                _, id_str, new_score_str = parts
                exp_id = int(id_str)
                new_score = int(new_score_str)

                # Update the master list
                all_experiences[exp_id] = new_score

                # Per problem description, after an update, the pool is reset
                # to contain ALL experiences with their latest priorities.
                active_pool = [(-s, i) for i, s in all_experiences.items()]
                heapq.heapify(active_pool) # O(N) operation to build the heap

            elif op == '-':
                # Extract operation: - k
                has_extract_op = True
                _, k_str = parts
                k = int(k_str)

                if len(active_pool) < k:
                    outputs.append("-1")
                else:
                    extracted_ids = []
                    # Pop k times from the heap to get the top k elements
                    for _ in range(k):
                        # The heap returns the tuple (-score, id)
                        _, exp_id = heapq.heappop(active_pool)
                        extracted_ids.append(str(exp_id))
                    outputs.append(" ".join(extracted_ids))

        # Final output based on problem rules
        if not has_extract_op:
            print("null")
        else:
            # Print each result on a new line
            print("\n".join(outputs))

    except (ValueError, IndexError):
        # Handle cases with malformed input lines
        print("null")

# Execute the solution
dynamic_priority_experience_replay()