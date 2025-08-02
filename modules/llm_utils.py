def compose_generation(context_list, user_query):
    """
    Join retrieved context with user question, 
    optionally using an external LLM for answer generation.
    """
    context_string = "\n".join(context_list)
    answer = f"Based on the geographic context:\n{context_string}\n\nQuery: {user_query}\n"
    # Here, you could hook in a local LLM or OpenAI API call for natural language generation.
    return answer
