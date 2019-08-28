import CodaClient
import pandas as pd

# GraphQL client on localhost:8000
coda = CodaClient.Client(graphql_host="localhost", graphql_port="8000")

# Get all the blocks
c = coda.get_blocks()

data = []

for value in c["blocks"]["nodes"]:
    jobs = value["snarkJobs"]
    if jobs:
        # Loop through all jobs
        for j in jobs:
            data.append([j["prover"], j["fee"]])

df = pd.DataFrame(data)
df.columns = ["ProverKey", "Fee"]

producers = df.groupby("ProverKey").size().sort_values(ascending=False)

print(producers)