# We have these numbers
# 1 -> 2 -> 3 -> 4 ........ 20

N = 20
LOGS = 5 # 2^5 = 32 which is enough to cover 20

# Up Table for the fast loopkup
up_table = [[0]*LOGS for _ in range(N)]

# Fill up for the Base case: 2^0
for node in range(N):
  # A single jump from node i will land to i+1
  up_table[node][0] = min(node+1, N-1)

# Filling up the rest of the up_table
for k in range(1, LOGS):
  for node in range(N):
    # k will be broken down into two steps, firt to halfway and second to the target k
    halfway_node = up_table[node][k-1]
    up_table[node][k] = up_table[halfway_node][k-1]

# Given a starting node and the number of steps to take, return the target node
def jump_k_steps(start_node, k_steps):
  print(f"Starting node: {start_node}, Steps: {k_steps}")
  current = start_node
  for k in range(LOGS-1, -1, -1):
    if (k_steps>>k)&1:
      current = up_table[current][k]
  return current

print(jump_k_steps(0, 11))
print(jump_k_steps(5, 20))