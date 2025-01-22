from local_ai_utils_core import LocalAIUtilsCore

def generate_embeddings(prompt):
    core = LocalAIUtilsCore()
    client = core.clients.open_ai()

    response = client.embeddings.create(
        input=prompt,
        model="text-embedding-3-small"
    )

    return response.data[0].embedding